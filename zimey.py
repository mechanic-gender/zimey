import pygame
import time
import random

pygame.init()#инициализация всего
white = (255, 255, 255)#цвета в ргб
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
dis_width = 800#ширина
dis_height = 600#высота
dis = pygame.display.set_mode((dis_width, dis_height))#создоём поле
pygame.display.set_caption('Змейка')# название
clock = pygame.time.Clock()
snake_block = 10#размер змеи
snake_speed = 15#сокрость
font_style = pygame.font.SysFont(None, 30)#шрифт 1


def message(msg, color,x=400,y=300):# функция для вывода сообшений
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x, y])



import time
import random
#цветовая палитра
pygame.init()
white = (255, 255, 255)
black = (2, 0, 0)
red = (255, 200, 0)
blue = (0, 0, 255)
#размер окон
dis_width = 600
dis_height = 550
#настрйки змейки
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont(None, 30)
score_font=pygame.font.SysFont("comicsansms",35)
def score(score,x=10,y=10):
    v=score_font.render("ваш шёт: "+str (score),True,(255,0,0))
    dis.blit(v,(x,y))
def score1(score,x=20,y=10):
    v=score_font.render("ваш шёт: "+str (score),True,(255,0,0))
    dis.blit(v,(x,y))

#настройки сообшений
# def message(msg, color):
#    mesg = font_style.render(msg, True, color)
#    dis.blit(mesg, [dis_width/10, dis_height/3])
#    mesg1 = font_style.render(msg, True, color)
#    dis.blit(mesg, [dis_width/10, dis_height/3])
def snake (snakeblock,snakelist):#рщст змея
    for x in snakelist:
        pygame.draw.rect(dis,black,[x[0],x[1],snakeblock,snakeblock])

def snake2 (snakeblock,snakelist):#рщст змея2
    for x in snakelist:
        pygame.draw.rect(dis,black,[x[0],x[6],snakeblock,snakeblock])

def gameLoop():# основная логики змей
   game_over = False
   game_close = False
   x1 = dis_width / 2
   y1 = dis_height / 2
   x1_change = 0 #шаг по гор
   y1_change = 0
   snakelist=[]
   len_of_snake=1
   len_of_snake1=5
   x2=300
   y2=300
   x2_change=0
   y2_change=0

   foodx = random.randint(20,dis_width-20) # Рандомизация положния яблока
   foody = random.randint(20,dis_height-20)

   while not game_over:
       while game_close == True:
           dis.fill(white)#оно белое
           message("Вы проиграли!", red,100,100)#чо пишем
           message("Нажмите Esc для выхода или ", red,50,150)
           message("space для повторной игры", red, 100, 200)
           score((len_of_snake - 1))
           pygame.display.update()
           for event in pygame.event.get():#кнопки
               if event.type == pygame.KEYDOWN:#проверка на кнопку
                   if event.key == pygame.K_ESCAPE:
                       game_over = True
                       game_close = False
                   if event.key == pygame.K_q:
                       game_over = True
                       game_close = False
                   if event.key == pygame.K_SPACE:
                       gameLoop()
                   if event.key == pygame.K_e:
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
               elif event.key == pygame.K_s:
                   x1_change = 0
                   y1_change = snake_block
               elif event.key == pygame.K_w:
                   y1_change = -snake_block
                   x1_change = 0
               # elif event.key == pygame.K_NumLk_8:
               #     y1_change = -snake_block
               #     x1_change = 0
               elif event.key == pygame.K_UP:
                   y2_change = -snake_block
                   x2_change = 0
               elif event.key == pygame.K_DOWN:
                   y2_change = snake_block
                   x2_change = 0
               elif event.key == pygame.K_LEFT:
                   x2_change = -snake_block
                   y2_change = 0
               if event.key == pygame.K_RIGHT:
                   x2_change = snake_block
                   y2_change = 0
       if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
           game_close = True
       if x2 >= dis_width or x2 < 0 or y2 >= dis_height or y2 < 0:
           game_close = True

       x1 += x1_change
       y1 += y1_change
       dis.fill(white)
       if foodx-10<x1<foodx+10 and foody-10<y1<foody+10:
           foodx = random.randint(50, dis_width - 20)
           foody = random.randint(20, dis_height - 90)
           len_of_snake+=1
       score((len_of_snake-1))
       #score1((len_of_snake-1))
       if foodx-10-len_of_snake1<x2<foodx+10+len_of_snake1 and foody-10-len_of_snake1<y2<foody+10+len_of_snake1:
           foodx = random.randint(50, dis_width - 20)
           foody = random.randint(20, dis_height - 90)
           len_of_snake1+=1
       score((len_of_snake1-5),300,10)
       #score1((len_of_snake1 - 5), 300, 10)
       pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
       snakehead=[]
       snakehead.append(x1)
       snakehead.append(y1)
       snakelist.append(snakehead)
       if len(snakelist)>len_of_snake:
        del snakelist[0]
       snake(snake_block,snakelist)
       x2+=x2_change
       y2+=y2_change
       pygame.draw.circle(dis,(255,0,0),(x2,y2),len_of_snake1)
       pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
       pygame.display.update()

       clock.tick(snake_speed)

   pygame.quit()
   quit()

gameLoop()