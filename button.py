__author__ = 'mohammed'
import pygame
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0) #defining colours
RED      = ( 255,   0,   0)
class Button(object): #button class
    def __init__(self, text, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.left,self.top,self.width,self.height)
        self.text = text #text for label
        self.font_colour = (BLACK) #font colour
        self.hover = False #testing for mouseover
        self.colour = (GREEN) #base colour
        self.hover_colour = (RED) #mouse over colour
    def label(self):
      '''button label font'''
      font = pygame.font.Font(None, 20)
      return font.render(self.text, 1, self.font_colour)
    def colourchooser(self): #checks mouseover state and returns appropriate colour
        if self.hover:
            return self.hover_colour
        else:
            return self.colour
    def draw(self, mouse, screen2): #draws the rectangle
        rectcoords = (self.left, self.top, self.width, self.height) #puts it into pygame appropriate
        self.check_hover(mouse) #check if moused over
        pygame.draw.rect(screen2, self.colourchooser(), rectcoords) #draws the button
        text_x = ((self.rect.right - self.rect.left)/2 + self.rect.left) - ((self.label().get_rect().right - self.label().get_rect().left)/2) #half of the text is on the left side of the midpoint of the rect, and half on the right side
        text_y = ((self.rect.bottom - self.rect.top)/2 + self.rect.top) - ((self.label().get_rect().bottom - self.label().get_rect().top)/2) #half of the text is on the top side of the midpoint of the rect, and half on the bottom side
        screen2.blit(self.label(), (text_x, text_y)) #midpoint of box - midpoint text
    def check_hover(self, mouse): #checks for mouseover
        if self.rect.collidepoint(mouse):
           self.hover = True
        else:
           self.hover = False