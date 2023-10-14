import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BALL_SPEED = 5
PADDLE_SPEED = 10

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PygameBreakout")

# Initial ball position and velocity
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

# Initial paddle position
paddle_x, paddle_y = (WIDTH - 100) // 2, HEIGHT - 20

# Paddle width and height
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10

# Brick dimensions
BRICK_WIDTH, BRICK_HEIGHT = 80, 20

# Create bricks
bricks = []
for row in range(5):
    for col in range(10):
        brick = pygame.Rect(col * (BRICK_WIDTH + 5), row * (BRICK_HEIGHT + 5), BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        paddle_x += PADDLE_SPEED

    # Ball collisions with walls
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy

    # Ball collision with paddle
    if (
        paddle_x < ball_x < paddle_x + PADDLE_WIDTH
        and paddle_y < ball_y < paddle_y + PADDLE_HEIGHT
    ):
        ball_dy = -ball_dy

    # Ball out of bounds (game over)
    if ball_y > HEIGHT:
        running = False

    # Check for collisions with bricks
    collision_index = ball.colliderect(bricks)
    if collision_index >= 0:
        del bricks[collision_index]
        ball_dy = -ball_dy

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Clear the screen
    screen.fill(WHITE)

    # Draw paddle, ball, and bricks
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x - 10, ball_y - 10, 20, 20))
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
