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
class Button(object):
    def __init__(self, text):
        self.text = text
        self.font_colour = (BLACK)
        self.rect = pygame.Rect(393.5,450, 100,50)
        self.hover = False
        self.colour = (GREEN)
        self.hover_colour = (RED)
        self.obj = None
    def label(self):
      '''button label font'''
      font = pygame.font.Font(None, 20)
      return font.render(self.text, 1, self.font_colour)
    def colourchooser(self):
        if self.hover:
            return self.hover_colour
        else:
            return self.colour
    def draw(self, mouse, screen2, left, top, width, height):
        rectcoords = (left, top, width, height)
        self.check_hover(mouse)
        self.obj = pygame.draw.rect(screen2, self.colourchooser(), rectcoords)
        screen.blit(self.label(), (((self.rect.right - self.rect.left)/2 + self.rect.left) - ((self.label().get_rect().right - self.label().get_rect().left)/2), ((self.rect.bottom - self.rect.top)/2 + self.rect.top) - ((self.label().get_rect().bottom - self.label().get_rect().top)/2)))
    def check_hover(self, mouse):
        if self.rect.collidepoint(mouse):
           self.hover = True
        else:
           self.hover = False
while 1:
    mouse = pygame.mouse.get_pos()
    btn = Button("Button yolo")
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if btn.rect.collidepoint(mouse):
                print("button one clicked")
    screen.blit(menu, [0,0])
    screen.blit(logo, [133.5,56.5])
    btn.draw(mouse, screen, 393.5, 450,100,50)
    pygame.display.flip()