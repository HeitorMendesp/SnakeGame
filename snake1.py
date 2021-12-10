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
    apple_pos = (random.randint(0,79) * 15, random.randint(0,51) * 15)
    return apple_pos

def collision(c1, c2):
    '''
    DOCTYPE - head X body or head X apple
    returns boolean value
    '''
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


#snake
snake = [(225,225), (240,225), (255,225)]
snake_skin = pygame.Surface((15,15)) # place sprite
snake_skin.fill((180,16,183))

#apple
apple_skin = pygame.Surface((15,15)) # place sprite
apple_skin.fill((255,0,0))
apple_pos = generate_apple_pos()

#directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#generating  display
screen = pygame.display.set_mode((1200,780))
pygame.display.set_caption('Snake Game Primitivo')
apple_pos = generate_apple_pos()

#direção inicial    
my_direction = RIGHT

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
        apple_pos = generate_apple_pos()
        snake.append((0,0))
        n += 0.5

    #collision body wall --> death --> quit
    for i in range(2, len(snake)):
        if collision(snake[0], snake[i]):
            pygame.quit()
        elif snake[0][0] > 1185 or snake[0][0] < 0:
            pygame.quit()
        elif snake[0][1] > 765 or snake[0][1] < 0:
            pygame.quit()


    #tail follows head
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i -1][1])


    screen.fill((51,112,65))
    
    screen.blit(apple_skin,apple_pos)


    for pos in snake:
        screen.blit(snake_skin,pos)
    
    pygame.display.update()