# This file was created by: Rohan Angelo

# Project title: Jetpack Joyride

# https://www.youtube.com/watch?v=427mSthTxQQ&ab_channel=LeMasterTech
# kidscancode
'''
Goals for final project:
create movable obstacles
character moves up and down with jetpack animation
create background
'''

# import libraries and modules
import random
import pygame

pygame.init()

# create screen
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

# put jetpack joyride name on the screen
pygame.display.set_caption("Jetpack Joyride")
# frames per second
fps = 60
# python timer
timer = pygame.time.Clock()
font_ = pygame.font.Font("freesansbold.ttf", 32)
bg_color = (128, 128, 128)
# draw screen
def draw_screen():
    screen.fill("black")
    pygame.draw.rect(surface, )

# display screen
run = True
while run:
    timer.tick(fps)
    draw_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()