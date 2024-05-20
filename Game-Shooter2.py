from pygame import *
from random import *
import pygame

win_width = 700
win_height = 500
window = pygame.display.set_mode((700,500))
display.set_caption('Космос')
background = transform.scale(image.load('ШАХМАТЫ.jpg'), (700, 500))
lost = 0
score = 0 
font.init()
font1 = font.Font(None,80)
font2 = font.Font(None, 80)
font3 = font.Font(None, 80)
win = font1.render('ПОБЕДА',1,(10,20,120))
lose = font2.render('ПОРАЖЕНИЕ',1,(10,20,120))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, width, height, player_x, player_y, player_speed,window):
        super().__init__()
        self.window = window
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        #if keys_pressed[K_UP] and self.rect.y > 5:
            #self.rect.y -= self.speed
        #if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            #self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('Bullet.jpeg', 10, 10, self.rect.centerx, self.rect.top, 5, window)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 565:
            self.rect.y = 0
            self.rect.x = randint(65, 635)
        self.rect.y += self.speed

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0 :
            self.kill()

        # self.rect.centerx 

game = True
finish = False
run = True
clock = time.Clock()
FPS = 60


player = Player('CosmoShip.png', 50, 70, 300, 400, 2,window)
monstres = sprite.Group()
bullets = sprite.Group()
for i in range(1,6):
    monster = Enemy('SuperEnemies.png', 30, 30, 200, 500, 1, window)
    monstres.add(monster)

for i in range(1):
     bullet = Bullet('Bullet.jpeg', 10, 10, 300, 400, 2, window)
     bullets.add(bullet)

mixer.init()
mixer.music.load('star-wars-imperial-march.mp3')
mixer.music.play()

YELLOW = (255,255,0)


while game:
    window.blit(background,(0,0))
    for e  in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                #fire.sound.play()
                player.fire()
    
    #if sprite.spritecollide(bullet, monstres,False):
        #score = score + 1

    if sprite.spritecollide(player, monstres, False) or lost >= 1:
        finish = True
        window.blit(lose, (0,0))
    if score == 10:
        window.blit(win,(0,0))
        finish = True
    #if score >= goal:
        #finish = True
        #window.blit(win, (0,0))

    if finish != True:
        score_font = pygame.font.SysFont("comicsansms", 35)
        def Your_score(score):
            value = font3.render("Ваш счёт: " + str(score), False, YELLOW)
            window.blit(value, (0, 0))
        window.blit(background,(0,0))
        Your_score(score)
        player.update()
        monstres.update()
        bullets.update()

        player.reset()
        bullets.draw(window)
        monstres.draw(window)

        collides = sprite.groupcollide(monstres,bullets,True,True)
        for c in collides:
            score = score + 1
            monster = Enemy('SuperEnemies.png', 30, 30, 200, 500, 2, window)
            monstres.add(monster)
        

    display.update()
    clock.tick(FPS)
