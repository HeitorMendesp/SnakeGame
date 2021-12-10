'''
Nesse arquivo está o mesmo jogo da cobra porém com imagens mais bonitas + score e etc
'''
#import libraries
import pygame, random
from pygame.locals import *
import random


pygame.init()
def generate_apple_pos():
    '''
    DOCTYPE - generates apple position in grid size 10
    '''
    apple_pos = (random.randint(1,79) * 15, random.randint(1,51) * 15)
    return apple_pos

def collision(c1, c2):
    '''
    DOCTYPE - head X body or head X apple
    returns boolean value
    '''
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def score_shower(x, y):
    '''
    DOCTYPE - shows the score
    '''
    score = font.render('Score : ' + str(score_value), True, (73,10,50))
    screen.blit(score, (x,y))

def game_over(x,y):
    '''
    DOCTYPE - shows message when you die than quit
    '''
    you_died = message_font.render(message, True, (0,0,0))
    screen.blit(you_died, (x,y))


#snake
snake = [(225,225), (240,225), (255,225)]
snake_skin = pygame.Surface((15,15)) # place sprite
snake_skin.fill((26,41,51))

#apple
apple_skin = pygame.image.load('projetoIP/apple_1.png')
apple_pos = generate_apple_pos()

#directions
UP = 0
RIGHT = 1   
DOWN = 2
LEFT = 3

#background
background = pygame.image.load('projetoIP/grass_1.png')

#generating  display
screen = pygame.display.set_mode((1200,780))
pygame.display.set_caption('Snake Game')
apple_pos = generate_apple_pos()

#direção inicial    
my_direction = RIGHT

#score
score_value=  0
font = pygame.font.SysFont('impact', 56)
score_x = 15
score_y = 15

#you died
message = 'GAME OVER'
message_font = pygame.font.SysFont('impact', 100)
message_x = 370
message_y = 320


clock = pygame.time.Clock()
#game
n = 18
while True:

    clock.tick(n)
    
    for event in pygame.event.get():

        #user get out
        if event.type == QUIT:
            pygame.quit()
        
        #input arrows
        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            elif event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            elif event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
            elif event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
    
    #head direction
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 15) 
    elif my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 15) 
    elif my_direction == RIGHT:
        snake[0] = (snake[0][0] + 15, snake[0][1]) 
    elif my_direction == LEFT:
        snake[0] = (snake[0][0] - 15, snake[0][1]) 
    
    #collision apple
    if collision(snake[0], apple_pos):
        score_value += 1
        apple_pos = generate_apple_pos()
        snake.append((0,0)) # increases snake size
        n += 0.6 # increases speed

    #collision body wall --> death --> quit
    for i in range(2, len(snake)):
        if collision(snake[0], snake[i]):
            for i in range(12000):
                game_over(message_x,message_y)
            pygame.quit()
        elif snake[0][0] > 1185 or snake[0][0] < 0:
            for i in range(12000):
                game_over(message_x,message_y)
            pygame.quit()
        elif snake[0][1] > 765 or snake[0][1] < 0:
            pygame.quit()
    

    #tail follows head
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i -1][1])

   

    screen.blit(background, (0, 0))
    screen.blit(apple_skin,apple_pos)


    for pos in snake:
        screen.blit(snake_skin,pos)
    

    score_shower(score_x,score_y)
    pygame.display.update()