import pygame
import random
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
ROAD_WIDTH = 400
ROAD_X = (WIDTH - ROAD_WIDTH) // 2
PLAYER_SPEED = 5
ENEMY_SPEED = 5
COIN_SPEED = 3
COIN_INCREASE_THRESHOLD = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

script_dir = os.path.dirname(__file__)
car_img = pygame.image.load(os.path.join(script_dir, "car.png"))
car_img = pygame.transform.scale(car_img, (50, 100))

enemy_img = pygame.image.load(os.path.join(script_dir, "enemy.jpeg"))
enemy_img = pygame.transform.scale(enemy_img, (50, 100))

player_x = WIDTH // 2 - 25
player_y = HEIGHT - 120

enemy_x = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - 50)
enemy_y = -100

enemy_speed = ENEMY_SPEED

coins = []



def generate_coin():
    x = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - 30)
    y = random.randint(-500, -50)
    weight = 1
    return [x, y, weight]

def update_coins():
    global coin_count, enemy_speed
    for coin in coins[:]:
        coin[1] += COIN_SPEED
        if coin[1] > HEIGHT:
            coins.remove(coin)
        elif player_x < coin[0] < player_x + 50 and player_y < coin[1] < player_y + 100:
            coin_count += 1
            coins.remove(coin)
            if coin_count % COIN_INCREASE_THRESHOLD == 0:
                enemy_speed += 1
                coin_count = 0

coin_count = 0
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    screen.blit(car_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))
    
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin[0] + 15, coin[1] + 15), 15)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > ROAD_X:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < ROAD_X + ROAD_WIDTH - 50:
        player_x += PLAYER_SPEED
    
    enemy_y += enemy_speed
    if player_x < enemy_x + 50 and player_x + 50 > enemy_x and player_y < enemy_y + 100 and player_y + 100 > enemy_y:
        running = False
        break
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - 50)
        enemy_y = -100
        enemy_x = random.randint(ROAD_X, ROAD_X + ROAD_WIDTH - 50)
    
    if random.randint(1, 100) > 98:
        coins.append(generate_coin())
    

    
    score_text = pygame.font.Font(None, 36).render(f"Coins: {coin_count}", True, YELLOW)
    screen.blit(score_text, (WIDTH - 150, 10))
    
    pygame.display.update()
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
