import time


from pygame import *
# -*- coding: utf-8 -*-
win_width = 600
win_height = 500
display.set_caption('1fps 100ping')
window = display.set_mode((win_width, win_height))
back =(180, 245, 255)
window.fill(back)

class GameSprite(sprite.Sprite):
    '''конструктор класса'''

    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        '''каждый спрайт хранит прямоугольник rect, в который вписан'''
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        '''метод, отрисовывающий героя на окне'''
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    '''класс главного игрока'''

    def update_right(self):
        '''движение'''
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y < 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y > win_width - 80:
            self.rect.x += self.speed
    def update_left(self):
        '''движение'''
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y < 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.y > win_width - 80:
            self.rect.x += self.speed

finish = False
run = True
clock= time.Clock()
FPS =60

raket1 = Player("racket.png", 30, 200, 4, 50, 150)
raket2 = Player("racket.png", 500, 200, 4, 50, 150)
ball = GameSprite( "tenis_ball.png", 200, 200, 4, 50 ,50)

font.init()
font = font.Font(None, 35)
lose1 = font.render("Player 2 wins", True,(180, 0, 0) )
lose2 = font.render("Player 1 wins", True,(180, 0, 0) )

speed_x = 3
speed_y = 3

run = True
clock= time.Clock()
finish = False
FPS =60

while run :
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        #window.fill(back)
        raket1.update_left()
        raket2.update_right()
        ball.rect.x += speed_x
        ball.rect.y -= speed_y

        if sprite.collide_rect(raket1, ball) or sprite.collide_rect(raket2, ball):
            speed_x *= -1
            speed_x *= -1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x > win_height:
            finish = True
            window.blit(lose2, (200, 200))
            #game_over = True
        if ball.rect.x < 0 :
            finish = True
            window.blit(lose1, (200, 200))
            #game_over = True
    raket1.reset()
    raket2.reset()
    ball.reset()
