import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
SNAKE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake and food
snake = [(5, 5)]
snake_direction = (1, 0)
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Move the snake
    x, y = snake[0]
    new_x = x + snake_direction[0]
    new_y = y + snake_direction[1]
    snake.insert(0, (new_x, new_y))

    # Check for collisions with food
    if snake[0] == food:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    # Check for collisions with the walls
    if (
        x < 0
        or x >= GRID_WIDTH
        or y < 0
        or y >= GRID_HEIGHT
        or snake.count(snake[0]) > 1
    ):
        running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(
            screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )

    # Draw the food
    pygame.draw.rect(
        screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(SNAKE_SPEED)

# Quit Pygame
pygame.quit()
sys.exit()
