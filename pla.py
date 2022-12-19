import pygame as py
import random

SCREEN_RECT = py.Rect(0,0,480,600)

FRAME_PER_SEC = 60

CEE = py.USEREVENT

HFE = py.USEREVENT + 1

EFF = py.USEREVENT +1

class Gamego(py.sprite.Sprite):
    def __init__(self,image_name,speed = 1):
        super().__init__()

        self.image = py.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        
        self.rect.y += self.speed

class Background(Gamego):

    def __init__(self,is_alt=False):
        super().__init__('.\\bga.png')

        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):

        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(Gamego):
    def __init__(self):
        super().__init__('cnima_enemy.png')
        self.speed = random.randint(2,4)

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

        self.ebullonts = py.sprite.Group()
    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
    
    def frie(self):
        for i in range(0,1,2):
            bu = ebullet()

            bu.rect.bottom = self.rect.y + i * 20
            bu.rect.centerx = self.rect.centerx

            self.ebullonts.add(bu)



class player(Gamego):

    def __init__(self):
        super().__init__('cnima.png',0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        self.bullonts = py.sprite.Group()
    def update(self):
        self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.x  = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def frie(self):
        for i in range(0,1,2):
            bu = bullet()

            bu.rect.bottom = self.rect.y - i * 20
            bu.rect.centerx = self.rect.centerx

            self.bullonts.add(bu)

class bullet(Gamego):
    def __init__(self):
        super().__init__('y.png',-2)
    
    def update(self):
        super().update()

        if self.rect.bottom < 0:
            self.kill()
class ebullet(Gamego):
    def __init__(self):
        super().__init__('y.png',2)
    
    def update(self):
        super().update()

        if self.rect.bottom < 0:
            self.kill()