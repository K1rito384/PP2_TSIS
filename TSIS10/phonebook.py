import pygame
import random
import time
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="postgres",  
        user="postgres",           
        password="deti0609"   
    )

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_scores (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def get_or_create_user(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    if user:
        user_id = user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.execute("SELECT * FROM user_scores WHERE user_id = %s", (user_id,))
    score_row = cur.fetchone()
    if not score_row:
        cur.execute("INSERT INTO user_scores (user_id) VALUES (%s)", (user_id,))
        conn.commit()
        level = 1
    else:
        level = score_row[3]

    print(f"Добро пожаловать, {username}! Ваш текущий уровень: {level}")

    cur.close()
    conn.close()
    return user_id

def save_score(user_id, score):
    level = 1 + score // 5
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE user_scores SET score = %s, level = %s WHERE user_id = %s", (score, level, user_id))
    conn.commit()
    cur.close()
    conn.close()

pygame.init()

WIDTH, HEIGHT = 400, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = "RIGHT"
        self.next_direction = "RIGHT"
        self.grow = False

    def move(self):
        self.direction = self.next_direction
        head_x, head_y = self.body[0]
        if self.direction == "UP":
            head_y -= CELL_SIZE
        elif self.direction == "DOWN":
            head_y += CELL_SIZE
        elif self.direction == "LEFT":
            head_x -= CELL_SIZE
        elif self.direction == "RIGHT":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        self.body.insert(0, new_head)

    def check_collision(self):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            return True
        if (head_x, head_y) in self.body[1:]:
            return True
        return False

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self, snake_body):
        self.position = self.generate_food(snake_body)
        self.weight = random.randint(1, 3)
        self.spawn_time = time.time()
        self.color = self.get_color()

    def get_color(self):
        if self.weight == 1:
            return RED
        elif self.weight == 2:
            return ORANGE
        else:
            return YELLOW

    def generate_food(self, snake_body):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake_body:
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, self.color, (*self.position, CELL_SIZE, CELL_SIZE))

init_db()
username = input("Введите ваше имя: ")
user_id = get_or_create_user(username)

snake = Snake()
food = Food(snake.body)
score = 0
font = pygame.font.Font(None, 30)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_score(user_id, score)
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.next_direction = "UP"
            if event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.next_direction = "DOWN"
            if event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.next_direction = "LEFT"
            if event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.next_direction = "RIGHT"
            if event.key == pygame.K_p:
                save_score(user_id, score)
                print("Пауза. Нажмите P для продолжения.")
                paused = True
                while paused:
                    for e in pygame.event.get():
                        if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                            paused = False

    snake.move()

    if snake.check_collision():
        save_score(user_id, score)
        print("Игра окончена. Ваш счёт сохранён.")
        running = False

    if snake.body[0] == food.position:
        snake.grow = True
        score += food.weight
        food = Food(snake.body)

    if time.time() - food.spawn_time > 5:
        food = Food(snake.body)

    snake.draw()
    food.draw()

    level = 1 + score // 5
    score_text = font.render(f"Score: {score}", True, BLUE)
    level_text = font.render(f"Level: {level}", True, BLUE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.update()
    clock.tick(7 + score // 5)

pygame.quit()
