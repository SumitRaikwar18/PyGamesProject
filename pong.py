import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BALL_SPEED = 5
PADDLE_SPEED = 10

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PygamePong")

# Initial ball position and velocity
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

# Initial paddle positions
left_paddle_y, right_paddle_y = (HEIGHT - 100) // 2, (HEIGHT - 100) // 2
left_paddle_dy, right_paddle_dy = 0, 0

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right_paddle_dy = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                right_paddle_dy = PADDLE_SPEED
            elif event.key == pygame.K_w:
                left_paddle_dy = -PADDLE_SPEED
            elif event.key == pygame.K_s:
                left_paddle_dy = PADDLE_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_paddle_dy = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                left_paddle_dy = 0

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collisions with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_dy = -ball_dy

    # Ball collisions with paddles
    if (
        ball_x < 20 and left_paddle_y < ball_y < left_paddle_y + 100
    ) or (ball_x > WIDTH - 20 and right_paddle_y < ball_y < right_paddle_y + 100):
        ball_dx = -ball_dx

    # Ball out of bounds
    if ball_x < 0 or ball_x > WIDTH:
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx = BALL_SPEED
        ball_dy = BALL_SPEED

    # Update paddle positions
    left_paddle_y += left_paddle_dy
    right_paddle_y += right_paddle_dy

    # Keep paddles within the screen bounds
    left_paddle_y = max(0, min(HEIGHT - 100, left_paddle_y))
    right_paddle_y = max(0, min(HEIGHT - 100, right_paddle_y))

    # Clear the screen
    screen.fill(WHITE)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (10, left_paddle_y, 10, 100))
    pygame.draw.rect(screen, WHITE, (WIDTH - 20, right_paddle_y, 10, 100))
    pygame.draw.ellipse(screen, WHITE, (ball_x - 10, ball_y - 10, 20, 20))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
