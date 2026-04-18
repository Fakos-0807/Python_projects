from __future__ import annotations
from typing import List
import pygame
from random import randint
pygame.init()
from pathlib import Path
import os


WINDOW_HEIGHT = 500
WINDOW_WIDTH = 800

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
FPS = 60

LIGHT_GREEN = (80,255,80)

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
        window.blit(self.image, (self.rect.x, self.rect.y))


class Hero(Picture):
    def __init__(self,x,y,width,height,file_name, speed):
        super().__init__(x,y,width,height,file_name)
        self.speed = speed

    def move(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
       

class Wall():
    def __init__(self,x,y,width,height,color):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color

    def show(self):
        pygame.draw.rect(window, self.color, self.rect)

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
        if side == "bottom":
            player.rect.y += player.speed
        
class Fakewall():
    def __init__(self,x,y,width,height,color):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color

    def show(self):
        pygame.draw.rect(window, self.color, self.rect)

class Enemy(Picture):
    def __init__(self, x,y,width,height,file_name, point1,distance,speed):
        super().__init__(x,y,width,height,file_name)
        self.point1 = point1
        self.end = point1 + distance
        self.end1 = point1 - distance
        self.distance = distance
        self.speed = speed
    def move(self):
        self.rect.y += self.speed
        if self.rect.y >= self.end or self.rect.y <= self.point1:
            self.speed *= -1
    def move1(self):
        self.rect.y -= self.speed
        if self.rect.y <= self.end1 or self.rect.y >= self.point1:
            self.speed *= -1
    def check_collisions1(self,player:Hero):
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
        if side == "bottom":
            player.rect.y += player.speed
                    
                    
        
            

Yellow = (255,255,0)
Red = (255,0,0)
Green = (80,255,80)
bg = Picture(0,0, WINDOW_WIDTH, WINDOW_HEIGHT,"fon.jpg")
hero = Hero(20,20,50,50,"ja.jpg", 4)
enemies = [Enemy(327,295,40,40,"wrag.jpg",295,145,3),
          Enemy(400,440,40,40,"wrag.jpg",440,145,2),
          Enemy(627,440,40,40,"wrag.jpg",440,145,1),
          Enemy(550,295,40,40,"wrag.jpg",295,145,2)
]



walls = [Wall(0,0,800,20,Green),
        Wall(0,0,20,500,Green),
        Wall(20,480,800,20, Green),
        Wall(780,0,20,500, Green),
        Wall(20,80,100,20, Red),
        Wall(175, 20,20,80,Red),
        Wall(75,155,345,20,Red),
        Wall(255,75,20,85, Red),
        Wall(75,175,20,100, Red),
        Wall(20,330,150,20, Red),
        Wall(150,235,20,115, Red),
        Wall(225,175,20,250, Red),
        Wall(75,405,150,20, Red),
        Wall(245,330,75,20, Red),
        Wall(300,405,20,75,   Red),
        Wall(375,350,20,130,Red),
        Wall(300,275,20,70,Red),
        Wall(330,20,20,80,Red),
        Wall(300,275,425,20,Red),
        Wall(450,405,20,75,Red),
        Wall(450,275,20,75,Red),
        Wall(400,75,20,145,Red),
        Wall(400,75,325,20,Red),
        Wall(525,275,20,150,Red),
        Wall(600,275,20,90,Red),
        Wall(600,425,20,55,Red),
        Wall(675,350,20,130,Red),
        Wall(300,230,20,100,Red),
        Wall(475,155,250,20,Red)]





fakewall = Fakewall(700,75,100,20,Red)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    bg.show()
    hero.show()
    hero.move(keys)
    fakewall.show()
    for i in range(len(walls)):
        walls[i].show()
    for wall in walls:
        if wall.rect.colliderect(hero.rect):
            wall.check_collisions(hero)
        wall.show()
    for enemy in enemies:
        if enemy.rect.colliderect(hero.rect):
            enemy.check_collisions1(hero)
        enemy.show()
        enemy.move()
    
#    enemy1.show()
#    enemy1.move()
#    enemy2.show()
#    enemy2.move1()
#    enemy3.show()
#    enemy3.move1()
#    enemy4.show()
#    enemy4.move()
    pygame.display.update()
    clock.tick(FPS)