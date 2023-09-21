import pygame
import time
import random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont(None, 30)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 10, dis_height / 3])



import time
import random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width/10, dis_height/3])

def gameLoop():
   game_over = False
   game_close = False
   x1 = dis_width / 2
   y1 = dis_height / 2
   x1_change = 0
   y1_change = 0
   foodx = random.randint(20,dis_width-20)
   foody =  random.randint(20,dis_height-20)

   while not game_over:
       while game_close == True:
           dis.fill(white)
           message("Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)
           pygame.display.update()
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_q:
                       game_over = True
                       game_close = False
                   if event.key == pygame.K_c:
                       gameLoop()
               if event.type == pygame.QUIT:
                   game_over = True
                   game_close=False
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               game_over = True
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_a:
                   x1_change = -snake_block
                   y1_change = 0
               elif event.key == pygame.K_d:
                   x1_change = snake_block
                   y1_change = 0
               elif event.key == pygame.K_w:
                   y1_change = -snake_block
                   x1_change = 0
               elif event.key == pygame.K_s:
                   y1_change = snake_block
                   x1_change = 0
       if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
           game_close = True
       x1 += x1_change
       y1 += y1_change
       dis.fill(white)
       if foodx-40<x1<foodx+40:
           foodx = random.randint(20, dis_width - 20)
           foody = random.randint(20, dis_height - 20)

       pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
       pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
       pygame.display.update()

       clock.tick(snake_speed)

   pygame.quit()
   quit()

gameLoop()