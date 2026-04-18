from __future__ import annotations
from typing import List
import pygame
from random import randint
pygame.init()
from pathlib import Path
import os

Width_screen = 1500
Height_screen = 800
screen = pygame.display.set_mode((Width_screen, Height_screen))

FPS = 60
clock = pygame.time.Clock()


font_large = pygame.font.Font(None,48)
font_small = pygame.font.Font(None, 24)

White = (255,255,255)
Green = ()
Blue = ()
Red = ()

game_over = False
retry_text = font_small.render('PRESS ANY KEY', True, (White))
retry_rect = retry_text.get_rect()
retry_rect.midtop = (Width_screen //2, Height_screen //2)
in_air = False
coins = 0
much = 0



class Picture():
    def __init__(self,x,y,width,height,file_name):
        self.image = self.load_image(file_name, (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def load_image(self,file_name, size = None):
        path = os.path.join(Path(__file__).parent, file_name)
        image = pygame.image.load(path)
        if size:
            image = pygame.transform.scale(image,size)
        return image


    def show(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
class Wall(Picture):
    def __init__(self,x,y,width,height,file_name):
        super().__init__(x,y,width,height,file_name)
#    def show(self):
#        pygame.draw.rect(screen,self.rect)

    def check_collisions(self,player:Hero):
        distances = {
            "right":abs(self.rect.right - player.rect.left),
            "left":abs(self.rect.left - player.rect.right),
            "bottom":abs(self.rect.bottom - player.rect.top),
            "top":abs(self.rect.top - player.rect.bottom)
        }
        side = min(distances, key=distances.get)
        if side == "left":
            player.rect.x -= player.speed
        if side == "right":
            player.rect.x += player.speed
        if side == "top":
            player.rect.y -= player.speed
            in_air = False
        if side == "bottom":
            player.rect.y += player.speed



class Lucky_block(Wall):
    def __init__(self, x, y, width, height, file_name):
        super().__init__(x, y, width, height, file_name)               
        self.much = 0
    def check_collisions(self, player):
        return super().check_collisions(player)
    def check_lucky(self, player:Hero):
        distance = {"bottom":abs(self.rect.bottom - player.rect.top)}
        side = min(distance, key = distance.get)
        if side == "bottom":
            coins += 1
            much += 1
        #if much >= 3:
            
        

class Hero(Picture):
    def __init__(self,x,y,width,height,file_name, speed):
        super().__init__(x,y,width,height,file_name)
        self.velocity_y = 0  # Текущая вертикальная скорость
        self.gravity = 0.8   # Сила, тянущая вниз (настраивайте под себя)
        self.jump_power = -16 # Сила рывка вверх (отрицательная, так как Y растет вниз)
        self.speed = speed
        self.jump = 10
        self.in_air = False
    def move(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        
        #if keys[pygame.K_SPACE] and self.in_air == False:
        #    self.in_air = True
        #    for i in range(50):
        #        self.rect.y -= 1
        #while self.rect.y != 650:
        #    self.rect.y += 1
        #if not self.in_air:
        #    if keys[pygame.K_SPACE]:
        #        self.in_air = True
        #else:
        #    if self.jump >= -10:
        #        if self.jump > 0:
        #            self.rect.y -= self.jump**2
        #        else:
        #            self.rect.y += self.jump**2
        #        self.jump -= 1
        #    else:
        #        self.in_air = False
        #        self.jump = 10
        if not self.in_air:
            if keys[pygame.K_SPACE]:
                self.velocity_y = self.jump_power
                self.in_air = True
        else:
    # Применяем скорость к координате Y
            self.rect.y += self.velocity_y
    # Постепенно увеличиваем скорость (тянем вниз)
            self.velocity_y += self.gravity

    # Проверка приземления (замените на вашу проверку коллизии с полом)
            if self.rect.y >= 650: # Пример: 500 — уровень земли
                self.rect.y = 650
                self.in_air = False
                self.velocity_y = 0







    def camera(self, cam:Wall):
        if self.rect.x >= 850:
            cam.rect.x -= self.speed    
        if self.rect.x <= 650:
            cam.rect.x += self.speed    



bg = Picture(0,0,1900,Height_screen,'mario_bg.jpg')
pol = Wall(0,700,900,100,"wall_long.png")
pol1 = Wall(870,700,900,100,"wall_long.png")

wall1 = Wall(500, 500, 100,50,"wall_small.png")
wall2 = Wall(600, 500, 100,50,"wall_small.png")

hero = Hero(Width_screen//2,650,50,50,"pixel_man.png", 3)

running = True  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FPS)        
    bg.show()
    pol.show()
    pol1.show()
    wall1.show()
    wall2.show()
    keys = pygame.key.get_pressed()
    hero.show()
    hero.move(keys)
    hero.camera(wall1)
    hero.camera(wall2)
    pygame.display.update()

quit()