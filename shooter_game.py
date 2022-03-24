#Создай собственный Шутер!

from pygame import *
from random import randint


class GameSprite(sprite.Sprite):

    def __init__(self, my_image, p_x ,p_y , p_w, p_h, N_speed):
        sprite.Sprite().__init__()
        self.image = transform.scale(image.load(my_image),(p_w, p_h))
        self.speed = N_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y

    def move(self):
        self.rect.y -= 10

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# class Bullet(GameSprite):

#     def fire2():
#         self.rect.y -= self.speed

#         if self.rect.y <= 0:
#             self.kill()

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] or keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys [K_d] or keys[K_RIGHT]:
            self.rect.x += self.speed

                         

class Enemy(GameSprite):

    def fall(self):

        if self.rect.y > win_height - 50:
            self.rect.y -= self.speed
        else:                
            self.rect.y = -50
            self.rect.x = randint(0,win_height)


        


                
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

#fire_sound = mixer.sound('fire.mp3')

img_back = 'galaxy.jpg'
img_hero = 'rocket.png'
img_enemy = 'ufo.png'

win_windth = 700
win_height = 500

window = display.set_mode((win_windth,win_height))

display.set_caption('Страшилка')

backgroud = transform.scale(image.load(img_back),(win_windth,win_height))


run = True

hero = Player(img_hero, 200, 430, 50,50, 10)
monster = Enemy(img_enemy, 200, 200, 50, 50, 1)
bullet = Player('bullet.png',hero.rect.x + 25, hero.rect.y, 10, 15, 10)

bullet_array = []

while run:

    for e in event.get(): 
        if e.type == QUIT:
            run = False

    keys = key.get_pressed()
    if keys[K_SPACE]:
        bullet_array.append(GameSprite('bullet.png',hero.rect.x + 25, hero.rect.y, 10, 15, 10))

    

    for i in range(len(bullet_array) - 1):
        if bullet_array[i].rect.y < 0:
            bullet_array.remove(bullet_array[i])
        
    
    window.blit(backgroud, (0,0))
    
    for elem in bullet_array:
        elem.move()
        elem.reset()

    monster.reset()
    monster.fall()

    hero.reset()
    hero.update()

    bullet.reset()
    bullet.update()

    
    display.update()
    time.delay(30)
 






































































































































