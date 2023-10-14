import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 288
WINDOW_HEIGHT = 512
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Set up the game clock
CLOCK = pygame.time.Clock()

# Load game assets
BACKGROUND_IMAGE = pygame.image.load("background.png").convert()
GROUND_IMAGE = pygame.image.load("ground.png").convert()
BIRD_IMAGES = [
    pygame.image.load("bird1.png").convert_alpha(),
    pygame.image.load("bird2.png").convert_alpha(),
    pygame.image.load("bird3.png").convert_alpha(),
]
PIPE_IMAGE = pygame.image.load("pipe.png").convert_alpha()
FONT = pygame.font.Font("04B_19.ttf", 40)

# Define game constants
GRAVITY = 0.25
BIRD_FLAP_VELOCITY = -6
PIPE_VELOCITY = -4
PIPE_SPACING = 150
PIPE_FREQUENCY = 120
GROUND_VELOCITY = -4
SCORE_INCREMENT = 1

# Define game variables
bird_rect = BIRD_IMAGES[0].get_rect(center=(50, WINDOW_HEIGHT / 2))
bird_velocity = 0
pipes = []
score = 0
high_score = 0

# Define game functions
def draw_background():
    WINDOW.blit(BACKGROUND_IMAGE, (0, 0))

def draw_ground():
    WINDOW.blit(GROUND_IMAGE, (0, WINDOW_HEIGHT - GROUND_IMAGE.get_height()))

def draw_bird():
    rotated_bird = pygame.transform.rotate(BIRD_IMAGES[bird_frame], bird_velocity * -3)
    WINDOW.blit(rotated_bird, bird_rect)

def draw_pipes():
    for pipe in pipes:
        if pipe.bottom >= WINDOW_HEIGHT - GROUND_IMAGE.get_height():
            WINDOW.blit(PIPE_IMAGE, pipe)
        else:
            flip_pipe = pygame.transform.flip(PIPE_IMAGE, False, True)
            WINDOW.blit(flip_pipe, pipe)

def move_bird():
    global bird_velocity
    bird_velocity += GRAVITY
    bird_rect.centery += bird_velocity

def create_pipe():
    random_pipe_pos = random.choice(PIPE_HEIGHTS)
    bottom_pipe = PIPE_IMAGE.get_rect(midtop=(WINDOW_WIDTH + 100, random_pipe_pos))
    top_pipe = PIPE_IMAGE.get_rect(midbottom=(WINDOW_WIDTH + 100, random_pipe_pos - PIPE_SPACING))
    return bottom_pipe, top_pipe

def move_pipes():
    for pipe in pipes:
        pipe.centerx += PIPE_VELOCITY
    visible_pipes = [pipe for pipe in pipes if pipe.right > -50]
    pipes.clear()
    pipes.extend(visible_pipes)

def check_collision():
    if bird_rect.top <= 0 or bird_rect.bottom >= WINDOW_HEIGHT - GROUND_IMAGE.get_height():
        return True
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return True
    return False

def update_score():
    global score, high_score
    if pipes:
        if bird_rect.centerx > pipes[0].centerx and not pipes[0].passed:
            pipes[0].passed = True
            score += SCORE_INCREMENT
            if score > high_score:
                high_score = score

def draw_score():
    score_surface = FONT.render(str(score), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(WINDOW_WIDTH / 2, 50))
    WINDOW.blit(score_surface, score_rect)

    high_score_surface = FONT.render(f"High Score: {high_score}", True, (255, 255, 255))
    high_score_rect = high_score_surface.get_rect(center=(WINDOW_WIDTH / 2, 100))
    WINDOW.blit(high_score_surface, high_score_rect)

# Define game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not check_collision():
                bird_velocity = BIRD_FLAP_VELOCITY

    # Draw game objects
    draw_background()
    draw_pipes()
    draw_ground()
    draw_bird()
    draw_score()

    # Update game objects
    bird_frame = (pygame.time.get_ticks() // 100) % 3
    move_bird()
    if len(pipes) == 0:
        pipes.extend(create_pipe())
    else:
        if pipes[-1].centerx < WINDOW_WIDTH - PIPE_FREQUENCY:
            pipes.extend(create_pipe())
    move_pipes()
    update_score()

    # Check for collisions
    if check_collision():
        pipes.clear()
        bird_rect.center = (50, WINDOW_HEIGHT / 2)
        bird_velocity = 0
        score = 0

    # Update the display
    pygame.display.update()

    # Set the game clock
    CLOCK.tick(60)
