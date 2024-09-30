import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Xpytask1')
clock = pygame.time.Clock()


ground_surface = pygame.image.load('img/ground.png')
sky_surface = pygame.image.load('img/sky.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(ground_surface,(0,260))
    screen.blit(sky_surface,(0,-40))
    # draw all elements
    pygame.display.update()
    clock.tick(60)