from imghdr import test_exr

import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Xpytask1')
clock = pygame.time.Clock()
test_font = pygame.font.Font('pixeltype.ttf', 50)

ground_surface = pygame.image.load('img/ground.png')
sky_surface = pygame.image.load('img/sky.png')
text_surface = test_font.render('XPython task',False, 'Black')
mainobject_surface = pygame.image.load('/img/mainobject.png')


while True:
    # draw all elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(ground_surface,(0,260))
    screen.blit(sky_surface,(0,-40))
    screen.blit(text_surface, (300,50))
    screen.blit(mainobject_surface,(0,0))

    pygame.display.update()
    clock.tick(60)