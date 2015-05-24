__author__ = 'mohammed'
import pygame
pygame.init()
size = width, height = 888, 660
screen = pygame.display.set_mode(size)
menu = pygame.image.load("menuart.png").convert()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
    screen.blit(menu, [0,0])
    pygame.display.flip()