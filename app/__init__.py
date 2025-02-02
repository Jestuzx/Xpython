from re import purge
import random
import pygame
from sys import exit
import time
from pygame import K_SPACE

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Xpytask1')
clock = pygame.time.Clock()
test_font = pygame.font.Font('../font/pixeltype.ttf', 50)

ground_surface = pygame.image.load('../img/ground.png')
sky_surface = pygame.image.load('../img/sky.png')
text_surface = test_font.render('XPython task',False, 'Black')
washing_machine = pygame.image.load('../img/first.png')
washing_machine_rect = washing_machine.get_rect(center=(400,220))
washing_machine_y_pos = 160

shaking = False

running = True
while running:
    # draw all elements

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shaking = True

            if shaking:
                for i in range(100):

                    offset_x = random.randint(-5, 5)
                    offset_y = random.randint(-5, 5)

                    screen.blit(washing_machine, (washing_machine_rect.x + offset_x, washing_machine_rect.y + offset_y))

                    pygame.display.flip()
                    pygame.time.delay(20)
    shaking = False


    screen.blit(ground_surface,(0,260))
    screen.blit(sky_surface,(0,-40))
    screen.blit(text_surface, (300,50))
    screen.blit(washing_machine,(350,160))

    pygame.display.update()
    clock.tick(60)

