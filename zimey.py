import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Set up display
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')

# Set up clock for framerate control
clock = pygame.time.Clock()

# Define size of each block in the snake
snake_block = 10

# Define speed of the snake
snake_speed = 15

# Set up font style for text rendering
font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width/10, dis_height/3])


def game_Loop():
   is_game_over = False
   is_game_close = False
   x1 = dis_width // 2
   y1 = dis_height // 2
   x1_change = 0 # Переменная скорости
   y1_change = 0
   food_x = random.randint(20,dis_width-20) // 2 # Рандомизация положния яблока
   food_y = random.randint(20,dis_height-20) // 2
   game_over_message = 'Вы проиграли! Нажмите Q для выхода или C для повторной игры'

   while not is_game_over:
       while is_game_close:
           dis.fill(white)
           message(game_over_message, red)
           pygame.display.update()
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_q:
                       is_game_over = True
                       is_game_close = False
                   if event.key == pygame.K_c:
                       game_Loop()
               if event.type == pygame.QUIT:
                   is_game_over = True
                   is_game_close = False
       
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               is_game_over = True
           if event.type == pygame.KEYDOWN:
               direction = {
                   pygame.K_a: (-snake_block, 0),  # Move left
                   pygame.K_d: (snake_block, 0),  # Move right
                   pygame.K_w: (0, -snake_block),  # Move up
                   pygame.K_s: (0, snake_block)  # Move down
               }.get(event.key, (0, 0))
               x1_change, y1_change = direction
       
       if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
           is_game_close = True
       x1 += x1_change
       y1 += y1_change
       dis.fill(white)
       if food_x - 10 < x1 < food_x + 10 and food_y - 10 < y1 < food_y + 10: # Check for food consumption
           food_x = random.randint(20, dis_width - 20)
           food_y = random.randint(20, dis_height - 20)

       pygame.draw.rect(dis, blue, [food_x, food_y, snake_block, snake_block])
       pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
       pygame.display.update()

       clock.tick(snake_speed)

   pygame.quit()
   quit()

game_Loop()
