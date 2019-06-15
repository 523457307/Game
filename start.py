import pygame, random, sys
from pygame.locals import *


def main():
    pygame.init()

    win = pygame.display.set_mode((700,700),pygame.RESIZABLE)
    win.fill(while)
    pygame.display.set_caption("贪吃蛇")

    sneak_speed = pygame.time.Clock()

    show_start_screen(win)
    while True:

        # run game
        # show result
        return

def show_start_screen(win):

    font = pygame.font.Font('System/Library/Fonts/Bodoni 72 Smallcaps Book.ttf', 40)
    tip = font.render('按任意键开始'， True, (65,100,100))
    gamestart = pygame.image.load("开始游戏.jpg")
    win.blit(gamestart, (140, 30))
    win.blit(tip, (240, 550))
    pygame.display.update()

    while True:
        for event in  pygame.event.get():
            if (event.type == QUIT):
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_ESCAPE):
                    terminate()
                else:
                    return

def start_game(screen):
    # initialize snake position, food position, direction
    snake_pos = [random.randint(0,500),random.randint(0, 500)]
    food_pos = [random.randint(0,700),random.randint(0, 700)]

    snake_body = [[100,100], [100, 80], [100,60]]

    direction = 'right'

    change_dir = direction

    food = 1

    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                
            if event == K_UP and not direction == 'down':
                change_dir = 'up'
            elif event == K_DOWN and not direction == 'up':
                change_dir = 'down'
            elif event == K_LEFT and not direction == 'right':
                change_dir = 'left'
            elif event == K_RIGHT and not direction == 'left':
                change_dir = 'right'




        if direction == 'right' :
            snake_pos[0] += 20

        elif direction == 'left':
            snake_pos[0] -= 20

        elif direction == 'up' :
            snake_pos[1] -= 20

        elif direction == 'down':
            snake_pos[1] += 20

        snake_body.insert(0, snake_pos)
        snake_body.pop()


        if eat_food(snake_pos, food_pos) == True:


        return


def eat_food(snake_pos, food_pos):
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        return True
    else:
        return False
