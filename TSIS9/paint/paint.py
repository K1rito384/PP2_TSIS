import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
TOOLBAR_HEIGHT = 50
screen = pygame.display.set_mode((WIDTH, HEIGHT + TOOLBAR_HEIGHT))
pygame.display.set_caption("Paint App")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)

screen.fill(WHITE)
clock = pygame.time.Clock()

current_color = BLACK
brush_size = 10
mode = "brush"

buttons = {
    "Circle": pygame.Rect(10, HEIGHT + 10, 80, 30),
    "Square": pygame.Rect(100, HEIGHT + 10, 80, 30),
    "Right Triangle": pygame.Rect(190, HEIGHT + 10, 130, 30),
    "Equilateral Triangle": pygame.Rect(330, HEIGHT + 10, 160, 30),
    "Rhombus": pygame.Rect(500, HEIGHT + 10, 100, 30),
    "Brush": pygame.Rect(610, HEIGHT + 10, 80, 30),
    "Eraser": pygame.Rect(700, HEIGHT + 10, 80, 30)
}

def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, HEIGHT, WIDTH, TOOLBAR_HEIGHT))
    font = pygame.font.Font(None, 24)
    for text, rect in buttons.items():
        pygame.draw.rect(screen, WHITE, rect)
        label = font.render(text, True, BLACK)
        screen.blit(label, (rect.x + 5, rect.y + 5))

def draw_circle(pos):
    pygame.draw.circle(screen, current_color, pos, brush_size * 2)

def draw_square(pos):
    square_size = brush_size * 4
    pygame.draw.rect(screen, current_color, (pos[0] - square_size // 2, pos[1] - square_size // 2, square_size, square_size))

def draw_right_triangle(pos):
    x, y = pos
    size = brush_size * 5
    points = [(x, y), (x, y - size), (x + size, y)]
    pygame.draw.polygon(screen, current_color, points)

def draw_equilateral_triangle(pos):
    x, y = pos
    size = brush_size * 5
    points = [(x, y - size), (x - size, y + size), (x + size, y + size)]
    pygame.draw.polygon(screen, current_color, points)

def draw_rhombus(pos):
    x, y = pos
    size = brush_size * 5
    points = [(x, y - size), (x + size, y), (x, y + size), (x - size, y)]
    pygame.draw.polygon(screen, current_color, points)

def erase(pos):
    pygame.draw.circle(screen, WHITE, pos, brush_size * 3)

running = True
while running:
    draw_toolbar()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y > HEIGHT:
                for tool, rect in buttons.items():
                    if rect.collidepoint(event.pos):
                        mode = tool.lower()
            else:
                if mode == "eraser":
                    erase(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if mode == "circle":
                draw_circle(event.pos)
            elif mode == "square":
                draw_square(event.pos)
            elif mode == "right triangle":
                draw_right_triangle(event.pos)
            elif mode == "equilateral triangle":
                draw_equilateral_triangle(event.pos)
            elif mode == "rhombus":
                draw_rhombus(event.pos)
    
    if pygame.mouse.get_pressed()[0] and mode == "brush":
        draw_circle(pygame.mouse.get_pos())
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
