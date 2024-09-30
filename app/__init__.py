from re import purge
import random
import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Xpytask1')
clock = pygame.time.Clock()
test_font = pygame.font.Font('../font/pixeltype.ttf', 50)

ground_surface = pygame.image.load('../img/ground.png')
sky_surface = pygame.image.load('../img/sky.png')
text_surface = test_font.render('XPython task',False, 'Black')


washing_machine = pygame.image.load('../img/pixil-frame-0.png')
washing_machine_rect = washing_machine.get_rect(center=(400,220))
washing_machine_y_pos = 160

while True:
    # draw all elements


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for _ in range(10):  # Кількість рухів для тряски
        # Випадкові зміщення
        offset_x = random.randint(-5, 5)  # Випадкове зміщення по X
        offset_y = random.randint(-5, 5)  # Випадкове зміщення по Y

        # Переміщення об'єкта
        screen.blit(washing_machine, (washing_machine_rect.x + offset_x, washing_machine_rect.y + offset_y))

        # Оновлення екрану
        pygame.display.flip()
        pygame.time.delay(20)

    screen.blit(ground_surface,(0,260))
    screen.blit(sky_surface,(0,-40))
    screen.blit(text_surface, (300,50))
    #screen.blit(washing_machine,(350,160))

    pygame.display.update()
    clock.tick(60)

