'''This file displays and runs the game SNAKE'''
import sys
import random
import pygame
# from pygame.locals import *

MAP_HEIGHT = 600
MAP_WIDTH = 800
CELL_SIZE = 20
REAL_HEIGHT = int(MAP_HEIGHT/CELL_SIZE)
REAL_WIDTH = int(MAP_WIDTH/CELL_SIZE)
# color
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 166)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACK_COLOR = BLACK

SNAKE_SPEED = 15

# 定义方向
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

HEAD = 0 #贪吃蛇头部下标
X = 0
Y = 1

def main():
    '''run the game'''
    pygame.init()
    win = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT), pygame.RESIZABLE)
    snake_speed_clock = pygame.time.Clock()
    win.fill(WHITE)
    pygame.display.set_caption("Python 贪吃蛇小游戏")
    show_start_screen(win)
    while True:
        pygame.event.get()
        start_game(win, snake_speed_clock)
        show_result_screen(win)

def show_start_screen(win):
    font = pygame.font.Font('/System/Library/Fonts/AquaKana.ttc', 40)
    # tip = font.render('按任意键开始'， True, (65, 100, 100))
    tip = font.render("Type Any Key to Start!", True, RED)
    gamestart = pygame.image.load("/Users/WangZheng/Desktop/Game/gamestart.png")
    win.blit(gamestart, (140, 30))
    win.blit(tip, (170, 550))
    pygame.display.update()

    while True:
        pygame.event.get()
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                else:
                    return

def start_game(win, snake_speed_clock):
    '''initialize snake position, food position, direction'''
    start_pos = [random.randint(3, REAL_WIDTH - 5), random.randint(3, REAL_HEIGHT - 5)]

    food_pos = [random.randint(0, REAL_WIDTH - 1), random.randint(0, REAL_HEIGHT - 1)]

    snake_body = [start_pos, [start_pos[0]-1, start_pos[1]], [start_pos[0]-2, start_pos[1]]]

    direction = 'right'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != 'down':
                    direction = 'up'
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != 'up':
                    direction = 'down'
                elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != 'right':
                    direction = 'left'
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != 'left':
                    direction = 'right'
                elif event.key == pygame.K_ESCAPE:
                    terminate()

        move_snake(direction, snake_body)

        alive = snake_alive(snake_body)
        if not alive:
            break
        eat_food(snake_body, food_pos)
        win.fill(BACK_COLOR)

        # draw snake, food, and else
        draw_snake(win, snake_body)
        draw_food(win, food_pos)
        draw_score(win, len(snake_body) - 3)
        pygame.display.update()
        snake_speed_clock.tick(SNAKE_SPEED)


def show_result_screen(win):
    # font = pygame.font.Font('/System/Library/Fonts/AquaKana.ttc', 40)
    # tip = font.render("Nice Work!", True, (65, 100, 100))
    gamestart = pygame.image.load("/Users/WangZheng/Desktop/Game/gameover.png")
    win.blit(gamestart, (80, 10))
    # win.blit(tip, (240, 500))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                else:
                    return


def draw_food (win, food_pos):
    x = food_pos[X] * CELL_SIZE
    y = food_pos[Y] * CELL_SIZE
    foodRect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(win, RED, foodRect)

def draw_score(win, score):
    temp = "Your score is: %s"
    font = pygame.font.Font('/System/Library/Fonts/AquaKana.ttc', 20)
    scoreSurf = font.render(temp % score, True, GREEN)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (MAP_WIDTH - 200, 10)
    win.blit(scoreSurf, scoreRect)


def draw_snake(win, snake_body):
    for coor in snake_body:
        x = coor[X] * CELL_SIZE
        y = coor[Y] * CELL_SIZE
        segmentRect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(win, BLUE, segmentRect)
        innersegRect = pygame.Rect(x + 3,y + 3,CELL_SIZE - 6,CELL_SIZE - 6)
        pygame.draw.rect(win, GREEN, innersegRect)



def eat_food(snake_body, food_pos):
    '''If snake eats food, then sign a new food position, else snake moves by del the last body'''
    if snake_body[HEAD][X] == food_pos[X] and snake_body[HEAD][Y] == food_pos[Y]:
        food_pos[X] = random.randint(0, REAL_WIDTH - 1)
        food_pos[Y] = random.randint(0, REAL_HEIGHT - 1)
    else:
        del snake_body[-1]

def snake_alive(snake_body):
    alive = True
    if snake_body[HEAD][X] == -1 or snake_body[HEAD][X] == REAL_WIDTH or \
        snake_body[HEAD][Y] == -1 or snake_body[HEAD][Y] == REAL_HEIGHT:
        alive = False
    #check if any body segments crash the head position
    for body in snake_body[1:]:
        if body[X] == snake_body[HEAD][X] and body[Y] == snake_body[HEAD][Y]:
            alive = False
    return alive

def move_snake(direction, snake_body):
    if direction == 'right' :
        newhead = [snake_body[HEAD][X] + 1, snake_body[HEAD][Y] ]

    elif direction == 'left':
        newhead = [snake_body[HEAD][X] - 1, snake_body[HEAD][Y] ]

    elif direction == 'up' :
        newhead = [snake_body[HEAD][X], snake_body[HEAD][Y] - 1 ]

    elif direction == 'down':
        newhead = [snake_body[HEAD][X], snake_body[HEAD][Y] + 1 ]

    snake_body.insert(0, newhead)

def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
