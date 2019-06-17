import pygame, random, sys
from pygame.locals import *

map_height = 700
map_width = 700
cell_size = 20

def main():
    pygame.init()

    win = pygame.display.set_mode((map_width,map_height),pygame.RESIZABLE)
    win.fill(white)
    pygame.display.set_caption("贪吃蛇")

    sneak_speed = pygame.time.Clock()

    show_start_screen(win)
    while True:

        # run game
        # show result
        return

def show_start_screen(win):

    font = pygame.font.Font('System/Library/Fonts/Bodoni 72 Smallcaps Book.ttf', 40)
    # tip = font.render('按任意键开始'， True, (65,100,100))
    tip = font.render("Hello World", True, (65,100,100))
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

def start_game(win, sneak_speed):
    # initialize snake position, food position, direction
    snake_pos = [random.randint(0,500),random.randint(0, 500)]
    food_pos = [random.randint(0,700),random.randint(0, 700)]

    snake_body = [[100,100], [100, 80], [100,60]]

    direction = 'right'

    change_dir = direction

    food = 1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_UP and not direction == 'down':
                    change_dir = 'up'
                elif event.key == K_DOWN and not direction == 'up':
                    change_dir = 'down'
                elif event.key == K_LEFT and not direction == 'right':
                    change_dir = 'left'
                elif event.key == K_RIGHT and not direction == 'left':
                    change_dir = 'right'
                elif event.key == K_ESCAPE:
                    terminate()

        move_snake(direction, snake_pos, snake_body)

        alive = snake_alive()

        if not alive:
            break

        # if eat_food then
        if eat_food(snake_pos, food_pos) == True:
            food_pos = [random.randint(0,map_width - 1),random.randint(0, map_height - 1 )]
            continue
        else:
            snake_body.pop()

        # draw snake, food, and else





        return
def draw_food (screen, food_pos):
    x = food_pos[0] * cell_size
    y = food_pos[1] * cell_size
    foodRect = pygame.Rect(x,y,cell_size,cell_size)
    pygame.draw.rect(screen, Red, foodRect)

def draw_score(screen, score):
    temp = "Your score is: %s"
    font pygame.font.Font('System/Library/Fonts/Bodoni 72 Smallcaps Book.ttf', 20)
    scoreSurf = font.render(temp % score, True, Green)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (map_width - 120, 10)
    screen.blit(scoreSurf, scoreRect)

def eat_food(snake_pos, food_pos):
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        return True
    else:
        return False

def snake_alive(snake_pos):
    alive = True
    if snake_pos[0] == -1 or snake_pos[0] == map_width or \
        snake_pos[1] == -1 or snake_pos[1] == map_height:
        alive = False
    for body in snake_body:
        if body[0] = snake_pos[0] and body[1] == snake_pos[1]:
            alive = False

    return tag


def move_snake(direction, snake_pos, snake_body):
    if direction == 'right' :
        snake_pos[0] += cell_size

    elif direction == 'left':
        snake_pos[0] -= cell_size

    elif direction == 'up' :
        snake_pos[1] -= cell_size

    elif direction == 'down':
        snake_pos[1] += cell_size

    snake_body.insert(0, snake_pos)
