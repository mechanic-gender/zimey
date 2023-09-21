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

def game_loop():
    is_game_over = False
    is_game_close = False
    x = dis_width // 2
    y = dis_height // 2
    x_change = 0
    y_change = 0
    snake_block = 10
    food_size = 10
    food_x = random.randint(0, (dis_width - food_size) // snake_block) * snake_block
    food_y = random.randint(0, (dis_height - food_size) // snake_block) * snake_block
    game_over_message = 'You lost! Press Q to quit or C to play again'

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
                        game_loop()
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
                x_change, y_change = direction

        x += x_change
        y += y_change
        if x >= dis_width or x < 0 or y >= dis_height or y < 0:
            is_game_close = True
        dis.fill(white)
        if x == food_x and y == food_y:
            food_x = random.randint(0, (dis_width - food_size) // snake_block) * snake_block
            food_y = random.randint(0, (dis_height - food_size) // snake_block) * snake_block

        pygame.draw.rect(dis, blue, [food_x, food_y, food_size, food_size])
        pygame.draw.rect(dis, black, [x, y, snake_block, snake_block])
        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
