__author__ = 'mohammed'
import pygame
pygame.init()
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
size = width, height = 888, 660
screen = pygame.display.set_mode(size)
menu = pygame.image.load("menuart.png").convert()
logo = pygame.image.load("logo.png").convert()
class Button:
    def __init__(self):
        self.hover = False
        self.colour = (GREEN)
        self.hover_colour = (RED)
        self.obj = ""
    def colourchooser(self):
        if self.hover:
            return self.hover_colour
        else:
            return self.colour
    def draw(self, mouse, screen2, rectcoords):
        self.obj = pygame.draw.rect(screen2, self.colourchooser(), rectcoords)
        #   self.obj = pygame.Rect(hello)
        #self.check_hover(mouse)
    #def check_hover(self, mouse):
        #if self.obj.collidepoint(mouse):
         #   self.hover = True
        #else:
           # self.hover = False
while 1:
    mouse = pygame.mouse.get_pos()
    btn = Button()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if btn.obj.collidepoint(mouse):
                print("button one clicked")
    screen.blit(menu, [0,0])
    screen.blit(logo, [133.5,56.5])
    btn.draw(mouse, screen, (393.5,450,100,50))
    if btn.obj.collidepoint(mouse):
        btn.hover = True
    else:
        btn.hover= False
    pygame.display.flip()