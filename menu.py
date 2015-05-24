__author__ = 'mohammed'
import pygame

import game
import button

pygame.init()
size = width, height = 888, 660 #screen size
screen = pygame.display.set_mode(size) #sets the screen size
menu = pygame.image.load("menuart.png").convert() #gets menu code and converts into optimised format
logo = pygame.image.load("logo.png").convert() #same for logo
logo.set_colorkey(button.BLACK)
while 1:
    mouse = pygame.mouse.get_pos() #gets mouse position for mouseover
    btn = button.Button("Testing sizes", 393.5, 450,100,50) #creates button with text
    for event in pygame.event.get(): #checks for special events such as quit and click
        if event.type == pygame.QUIT: pygame.quit() #if quit event, quit pygame
        elif event.type == pygame.MOUSEBUTTONDOWN: #checks if mouse is clicked
            if btn.rect.collidepoint(mouse): #checks if mouse is over the button
                print("button one clicked")
                game.game()
    screen.blit(menu, [0,0]) #draws menu on screen
    screen.blit(logo, [133.5,56.5]) #draws logo on screen
    btn.draw(mouse, screen) #draws button on screen
    pygame.display.flip() #updates screen