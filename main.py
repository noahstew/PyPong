# Initial setup
import pygame
import random
import time

pygame.init()
pygame.font.init()

# Window setup
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WINDOW_DIM = (WINDOW_WIDTH, WINDOW_HEIGHT)
DISPLAY = pygame.display.set_mode(WINDOW_DIM)
pygame.display.set_caption("PyPong")
FPS = 60
# ----------------------------------------------
# Game Variables

# Colors
TENNIS_BALL = (210, 255, 28)
NET = (192, 192, 192)
COURT = (104, 204, 0)
SCOREBOARD = (76, 153, 0)
PLAYER_ONE = (204, 0, 0)
PLAYER_TWO = (0, 51, 102)

# Paddle
PADDLE_INSET = 10  # how far in from edge of window the paddle will be
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 60
PADDLE_SPEED = 7

# Ball
BALL_SIZE = 10
ball_speed_x = 5
ball_speed_y = 4

# Scoreboard
left_score = 0
right_score = 0
scoreboard_font_size = 400
scoreboard_font = pygame.font.SysFont("Arial", scoreboard_font_size)

# Logic
start = True

# Clock setup
clock = pygame.time.Clock()
# ----------------------------------------------
# Gameplay Loop

# Running loop begins
running = True

# Set initial position of paddles and ball
left_paddle_y = (WINDOW_HEIGHT / 2) - (PADDLE_HEIGHT / 2)
right_paddle_y = (WINDOW_HEIGHT / 2) - (PADDLE_HEIGHT / 2)

ball_x_start = (WINDOW_WIDTH / 2)
ball_y_start = (WINDOW_HEIGHT / 2) - (BALL_SIZE / 2)
ball_x = ball_x_start
ball_y = ball_y_start


while running:
    # Create paddle objects
    left_paddle_rect = pygame.Rect(PADDLE_INSET, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle_rect = pygame.Rect(WINDOW_WIDTH - PADDLE_INSET - PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH,
                                    PADDLE_HEIGHT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display court backdrop
    DISPLAY.fill(COURT)

    # Paddle movement
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= PADDLE_SPEED
    if keys_pressed[pygame.K_s] and left_paddle_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        left_paddle_y += PADDLE_SPEED
    if keys_pressed[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= PADDLE_SPEED
    if keys_pressed[pygame.K_DOWN] and right_paddle_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        right_paddle_y += PADDLE_SPEED

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Paddle physics
    # Player 1
    if PADDLE_WIDTH + PADDLE_INSET >= ball_x > PADDLE_INSET:
        if left_paddle_y < ball_y < left_paddle_y + PADDLE_HEIGHT:
            ball_speed_x = abs(ball_speed_x - 0.25)
            ball_speed_y = random.randint(-5, 5)
    # Player 2
    if WINDOW_WIDTH - PADDLE_INSET - PADDLE_WIDTH <= ball_x < WINDOW_WIDTH - PADDLE_INSET:
        if right_paddle_y < ball_y < right_paddle_y + PADDLE_HEIGHT:
            ball_speed_x = -abs(ball_speed_x + 0.25)
            ball_speed_y = random.randint(-5, 5)

    # Ball physics
    if ball_y < BALL_SIZE:
        ball_speed_y = abs(ball_speed_y)
    elif ball_y > WINDOW_HEIGHT - BALL_SIZE:
        ball_speed_y = -abs(ball_speed_y)

    # Scoring
    if ball_x < 0:
        right_score += 1
        ball_x = ball_x_start
        ball_y = ball_y_start
        ball_speed_x = 7
        ball_speed_y = random.randint(-7, 7)
        left_paddle_y = (WINDOW_HEIGHT / 2) - (PADDLE_HEIGHT / 2)
        right_paddle_y = (WINDOW_HEIGHT / 2) - (PADDLE_HEIGHT / 2)
        start = True
    elif ball_x > WINDOW_WIDTH:
        left_score += 1
        ball_x = ball_x_start
        ball_y = ball_y_start
        ball_speed_x = -7
        ball_speed_y = random.randint(-7, 7)
        left_paddle_y = (WINDOW_HEIGHT / 2) - (PADDLE_HEIGHT / 2)
        right_paddle_y = (WINDOW_HEIGHT / 2) - (PADDLE_HEIGHT / 2)
        start = True

    # Setup scoreboard
    scoreboard_text_surface = scoreboard_font.render(str(left_score), True, SCOREBOARD)
    scoreboard_text_rect = scoreboard_text_surface.get_rect()
    # Displaying it centered
    if left_score < 10:
        scoreboard_text_rect.center = (WINDOW_WIDTH/8, WINDOW_HEIGHT/8)
    else:
        scoreboard_text_rect.center = (WINDOW_WIDTH/40, WINDOW_HEIGHT/8)
    DISPLAY.blit(scoreboard_text_surface, scoreboard_text_rect.center)

    scoreboard_text_surface = scoreboard_font.render(str(right_score), True, SCOREBOARD)
    scoreboard_text_rect = scoreboard_text_surface.get_rect()
    # Displaying it centered
    if right_score < 10:
        scoreboard_text_rect.center = (WINDOW_WIDTH * 5 / 8, WINDOW_HEIGHT / 8)
    else:
        scoreboard_text_rect.center = (WINDOW_WIDTH * 21/40, WINDOW_HEIGHT / 8)
    DISPLAY.blit(scoreboard_text_surface, scoreboard_text_rect.center)

    # Draw all objects
    pygame.draw.line(DISPLAY, NET, (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT), 6)

    pygame.draw.rect(DISPLAY, PLAYER_ONE, left_paddle_rect)
    pygame.draw.rect(DISPLAY, PLAYER_TWO, right_paddle_rect)
    pygame.draw.circle(DISPLAY, TENNIS_BALL, (ball_x, ball_y), BALL_SIZE)

    # ----------------------------------------------
    # Closing program
    clock.tick(FPS)
    pygame.display.update()

    if start:
        time.sleep(2)
        start = False

pygame.font.quit()
pygame.quit()
