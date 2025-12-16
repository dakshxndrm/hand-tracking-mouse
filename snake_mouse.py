import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hand-Controlled Snake")

clock = pygame.time.Clock()

snake = [(250, 250)]
snake_size = 10
food = (100, 100)

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

def draw():
    screen.fill(WHITE)

    for x, y in snake:
        pygame.draw.rect(screen, GREEN, (x, y, snake_size, snake_size))

    pygame.draw.rect(screen, RED, (*food, snake_size, snake_size))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    head_x, head_y = snake[0]

    dx = mouse_x - head_x
    dy = mouse_y - head_y

    head_x += dx * 0.1
    head_y += dy * 0.1

    snake.insert(0, (int(head_x), int(head_y)))
    snake.pop()

    if abs(head_x - food[0]) < 10 and abs(head_y - food[1]) < 10:
        snake.append(snake[-1])
        food = (pygame.mouse.get_pos())

    draw()
    pygame.display.update()
    clock.tick(30)
