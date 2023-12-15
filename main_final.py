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
from settings import *
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
# change font
font_ = pygame.font.Font("freesansbold.ttf", 32)
# background color
bg_color = (128, 128, 128)
# 4 lines that move across the screen to show motion
lines = [0, WIDTH/4, 2*WIDTH/4, 3*WIDTH/4]
# speed the screen moves at
game_speed = 4
# pause function
pause = False
# player axes (only moves up and down)
init_y = HEIGHT- 130
player_y = init_y
# jetpack booster that draws flames under the jetpack 
booster = False
# y velocity and gravity
y_velocity = 0
gravity = 0.5
# top platform and bottom platform





# draw background screen so it moves from right to left
def draw_screen(line_list):
    screen.fill("black")
    # alpha argument that lets me modify the transparency of points in a plot
    pygame.draw.rect(surface, (bg_color[0], bg_color[1], bg_color[2], 50), [0, 0, WIDTH, HEIGHT])
    screen.blit(surface, (0, 0))
    # rectangles at the top and bottom of the screen
    top = pygame.draw.rect(screen, "gray", [0, 0, WIDTH, 50])
    bot = pygame.draw.rect(screen, "gray", [0, HEIGHT-50, WIDTH, 50])
    # create lines that slide from the right to the left
    for i in range(len(line_list)):
        pygame.draw.line(screen, "black", (line_list[i], 0), (line_list[i], 50), 3)
        pygame.draw.line(screen, "black", (line_list[i], HEIGHT-50), (line_list[i], HEIGHT), 3)
        # makes the screen "move"
        if not pause:
            line_list[i] -= game_speed
        if line_list[i] < 0:
            line_list[i] = WIDTH
    return line_list


# draw player that moves
def draw_player():
    play = pygame.rect.Rect((120, player_y + 10), (25, 60))
    # hitbox
    # pygame.draw.rect(screen, "green", play, 5)
    # jetpack booster with flames
    if player_y < init_y or pause:
        if booster:
            pygame.draw.ellipse(screen, "red", [100, player_y + 50, 20, 30])
            pygame.draw.ellipse(screen, "orange", [100, player_y + 50, 10, 30])
            pygame.draw.ellipse(screen, "yellow", [100, player_y + 50, 5, 30])
        # legs
        pygame.draw.rect(screen, "yellow", [128, player_y + 60, 10, 20], 0, 3)
        pygame.draw.rect(screen, "orange", [130, player_y + 60, 10, 20], 0, 3)
    # jetpack
    pygame.draw.rect(screen, "white", [100, player_y + 20, 20, 30], 0, 5)
    # player main body, face, eyes, head
    pygame.draw.ellipse(screen, "orange", [120, player_y + 20, 30, 50])
    pygame.draw.circle(screen, "orange", (135, player_y + 15), 10)
    pygame.draw.circle(screen, "orange", (138, player_y + 12), 3)
    return play

# collision
def check_colliding():
    # see that player collides with top and bottom
    coll = [False, False]
    if player.colliderect(bot_plat):
        coll[0] = True
    elif player.colliderect(top_plat):
        coll[1] = True
    return coll




# main game loop (screen, player)
run = True
while run:
    timer.tick(fps)
    lines = draw_screen(lines)
    bot_plat = draw_screen(lines)
    top_plat = draw_screen(lines)
    player = draw_player()                       
    colliding = check_colliding()

    for event in pygame.event.get():
        # make able to quit the game
        if event.type == pygame.QUIT:
            run = False
        # movement up and down on the y axis using space bar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not pause:
                booster = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE: 
                booster = False
    # gravity that brings player down when not flying
    if not pause:
        if booster:
            y_velocity -= gravity
        else:
            y_velocity += gravity
        # stops when colliding with bottom and top platform
        if (colliding[0] and y_velocity > 0) or (colliding[1] and y_velocity < 0):
            y_velocity = 0


        player_y += y_velocity
    
    pygame.display.flip()
    
pygame.quit()
