import pygame, random, sys
from pygame.locals import *

map_height = 600
map_width = 800
cell_size = 20
real_height = int(map_height/cell_size)
real_width = int(map_width/cell_size)
# color
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
dark_blue = (0,0,166)
Black = (0,0,0)
White = (255,255,255)

Back_color = Black

snake_speed = 15

def main():
    pygame.init()
    win = pygame.display.set_mode((map_width,map_height),pygame.RESIZABLE)
    snake_speed_clock = pygame.time.Clock()
    win.fill(White)
    pygame.display.set_caption("Python 贪吃蛇")
    show_start_screen(win)
    while True:
        pygame.event.pump()
        start_game(win, snake_speed_clock)
        show_result_screen(win)

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()

def show_result_screen(win):
    font = pygame.font.Font('Avenir Next Condensed.ttc', 40)
    tip = font.render("Hello World", True, (65,100,100))
    gamestart = pygame.image.load("GameOver.jpg")
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

def show_start_screen(win):

    font = pygame.font.Font('Game/Avenir Next Condensed.ttc', 40)
    # tip = font.render('按任意键开始'， True, (65,100,100))
    tip = font.render("Hello World", True, (65,100,100))
    gamestart = pygame.image.load("Game/开始游戏.jpg")
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

def start_game(win, sneak_speed_clock):
    # initialize snake position, food position, direction
    snake_pos = [random.randint(0,real_width),random.randint(0, real_height)]
    food_pos = [random.randint(0,real_width),random.randint(0, real_height)]

    snake_body = [snake_pos, [snake_pos[0],snake_pos[1] - 1], [snake_pos[0],snake_pos[1] - 2]]

    direction = 'right'

    food = 1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_UP and not direction == 'down':
                    direction = 'up'
                elif event.key == K_DOWN and not direction == 'up':
                    direction = 'down'
                elif event.key == K_LEFT and not direction == 'right':
                    direction = 'left'
                elif event.key == K_RIGHT and not direction == 'left':
                    direction = 'right'
                elif event.key == K_ESCAPE:
                    terminate()

        move_snake(direction, snake_pos, snake_body)

        alive = snake_alive(snake_pos, snake_body)

        if not alive:
            break

        # if eat_food then
        if eat_food(snake_pos, food_pos) == True:
            food_pos = [random.randint(0,real_width - 1),random.randint(0, real_height - 1 )]
            draw_food(screen, food_pos)
        else:
            snake_body.pop()

        screen.fill(Back_color)
        # draw snake, food, and else
        draw_score(screen, score)
        draw_snake(screen, snake_body)
        pygame.display.update()
        snake_speed_clock.tick(snake_speed)

def draw_food (screen, food_pos):
    x = food_pos[0] * cell_size
    y = food_pos[1] * cell_size
    foodRect = pygame.Rect(x,y,cell_size,cell_size)
    pygame.draw.rect(screen, Red, foodRect)

def draw_score(screen, score):
    temp = "Your score is: %s"
    font = pygame.font.Font('Game/Avenir Next Condensed.ttc', 20)
    scoreSurf = font.render(temp % score, True, Green)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (map_width - 120, 10)
    screen.blit(scoreSurf, scoreRect)

def draw_snake(screen, snake_body):
    for coor in snake_body:
        x = coor[0] * cell_size
        y = coor[1] * cell_size
        segmentRect = pygame.Rect(x,y,cell_size,cell_size)
        pygame.draw.rect(screen, Blue, segmentRect)
        innersegRect = pygame.Rect(x + 3,y + 3,cell_size - 6,cell_size - 6)
        pygame.draw.rect(screen, dark_blue, innersegRect)

def eat_food(snake_pos, food_pos):
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        return True
    else:
        return False

def snake_alive(snake_pos,snake_body):
    alive = True
    if snake_pos[0] == -1 or snake_pos[0] == real_width or \
        snake_pos[1] == -1 or snake_pos[1] == real_height:
        alive = False
    for body in snake_body:
        if body[0] == snake_pos[0] and body[1] == snake_pos[1]:
            alive = False

    return alive

def move_snake(direction, snake_pos, snake_body):
    if direction == 'right' :
        snake_pos[0] += 1

    elif direction == 'left':
        snake_pos[0] -= 1

    elif direction == 'up' :
        snake_pos[1] -= 1

    elif direction == 'down':
        snake_pos[1] += 1

    snake_body.insert(0, snake_pos)

def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
