import pygame as py
from pla import *

input()
class go(object):
    def __init__(self):
       self.sc = py.display.set_mode((SCREEN_RECT.size)) 
       self.clo = py.time.Clock()
       self.__create_sprites()
       py.time.set_timer(CEE,1000)
       py.time.set_timer(HFE,500)

    def __create_sprites(self):
        bg = Background()
        bg2 = Background(True)
        bg2.rect.y = -bg2.rect.height
        self.back_group = py.sprite.Group(bg,bg2)

        self.enemyg = py.sprite.Group()

        self.hero = player()
        self.ene = Enemy()
        self.hg = py.sprite.Group(self.hero)

    def start_game(self):
        while True:
            self.clo.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            py.display.update()

    def __event_handler(self):
        for e in py.event.get():

            if e.type == py.QUIT:

                go.__game_over()
            elif e.type == CEE:
                

                enemy = Enemy()

                self.enemyg.add(enemy)
            elif e.type == HFE:
                self.hero.frie()
            elif e.type == EFF:
                enemy.frie()


        
        kp = py.key.get_pressed()
        if kp[py.K_RIGHT]:
            self.hero.speed = 3
        elif kp[py.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0
    def __check_collide(self):
        py.sprite.groupcollide(self.hero.bullonts,self.enemyg,True,True)

        eneb = py.sprite.spritecollide(self.hero,self.enemyg,True)
        if len(eneb) > 0:
            self.hero.kill()

            go.__game_over()
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.sc)

        self.enemyg.update()
        self.enemyg.draw(self.sc)

        self.hg.update()
        self.hg.draw(self.sc)

        self.hero.bullonts.update()
        self.hero.bullonts.draw(self.sc)

        self.ene.ebullonts.update()
        self.ene.ebullonts.draw(self.sc)

    @staticmethod
    def __game_over():
        print('game over!')

        py.quit()
        exit()
if __name__ == '__main__':
    game = go()
    game.start_game()
    
