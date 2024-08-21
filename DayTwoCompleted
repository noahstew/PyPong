# Completed DayTwoTODO:

import pygame
import time

pygame.init()
pygame.font.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WINDOW_DIM = (WINDOW_WIDTH, WINDOW_HEIGHT)

DISPLAY = pygame.display.set_mode(WINDOW_DIM)
pygame.display.set_caption('PyPong')

FPS = 60
clock = pygame.time.Clock()

COURT = (255, 200, 0)
TENNIS_BALL = (163, 14, 0)
NET = (0, 0, 0)
SCOREBOARD = (130, 101, 14)
PLAYER_ONE = (3, 39, 105)
PLAYER_TWO = (34, 105, 3)

PADDLE_INSET = 10
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 60
PADDLE_SPEED = 7

left_paddle_y = (WINDOW_HEIGHT / 2) - (PADDLE_HEIGHT / 2)
right_paddle_y = (WINDOW_HEIGHT / 2) - (PADDLE_HEIGHT / 2)

BALL_SIZE = 16
ball_speed_x = 5
ball_speed_y = 4

ball_start_x = WINDOW_WIDTH / 2
ball_x = ball_start_x
ball_start_y = WINDOW_HEIGHT / 2
ball_y = ball_start_y

left_score = 0
right_score = 0
scoreboard_font_size = 400
scoreboard_font = pygame.font.SysFont("Arial", scoreboard_font_size)

running = True

while running:

    left_paddle_rect = pygame.Rect(PADDLE_INSET, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle_rect = pygame.Rect(WINDOW_WIDTH - PADDLE_INSET - PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    DISPLAY.fill(COURT)

    pygame.draw.line(DISPLAY, NET, (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT), 12)

    pygame.draw.rect(DISPLAY, PLAYER_ONE, left_paddle_rect)
    pygame.draw.rect(DISPLAY, PLAYER_TWO, right_paddle_rect)

    pygame.draw.circle(DISPLAY, TENNIS_BALL, (ball_x, ball_y), BALL_SIZE)

    clock.tick(FPS)
    pygame.display.update()
pygame.quit()
