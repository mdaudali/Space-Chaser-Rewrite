__author__ = 'mohammed'
import pygame
pygame.init()
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0) #defining colours
RED      = ( 255,   0,   0)
size = width, height = 888, 660 #screen size
screen = pygame.display.set_mode(size) #sets the screen size
menu = pygame.image.load("menuart.png").convert() #gets menu code and converts into optimised format
logo = pygame.image.load("logo.png").convert() #same for logo
class Button(object): #button class
    def __init__(self, text):
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
    def draw(self, mouse, screen2, left, top, width, height): #draws the rectangle
        rectcoords = (left, top, width, height) #puts it into pygame appropriate
        self.rect = pygame.Rect(rectcoords) #creates a rect
        self.check_hover(mouse) #check if moused over
        pygame.draw.rect(screen2, self.colourchooser(), rectcoords) #draws the button
        text_x = ((self.rect.right - self.rect.left)/2 + self.rect.left) - ((self.label().get_rect().right - self.label().get_rect().left)/2) #half of the text is on the left side of the midpoint of the rect, and half on the right side
        text_y = ((self.rect.bottom - self.rect.top)/2 + self.rect.top) - ((self.label().get_rect().bottom - self.label().get_rect().top)/2) #half of the text is on the top side of the midpoint of the rect, and half on the bottom side
        screen.blit(self.label(), (text_x, text_y)) #midpoint of box - midpoint text
    def check_hover(self, mouse): #checks for mouseover
        if self.rect.collidepoint(mouse):
           self.hover = True
        else:
           self.hover = False
while 1:
    mouse = pygame.mouse.get_pos() #gets mouse position for mouseover
    btn = Button("Testing sizes") #creates button with text
    for event in pygame.event.get(): #checks for special events such as quit and click
        if event.type == pygame.QUIT: pygame.quit() #if quit event, quit pygame
        elif event.type == pygame.MOUSEBUTTONDOWN: #checks if mouse is clicked
            if btn.rect.collidepoint(mouse): #checks if mouse is over the button
                print("button one clicked")
    screen.blit(menu, [0,0]) #draws menu on screen
    screen.blit(logo, [133.5,56.5]) #draws logo on screen
    btn.draw(mouse, screen, 393.5, 450,100,50) #draws button on screen
    pygame.display.flip() #updates screen