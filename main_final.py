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
# change font
font_ = pygame.font.Font("freesansbold.ttf", 32)
# background color
bg_color = (128, 128, 128)
# 4 lines that move across the screen to show motion
lines = [0, WIDTH/4, 2*WIDTH/4, 3*WIDTH/4]
# speed the screen moves at
game_speed = 2
# pause function
pause = False
# player axes (only moves up and down)
init_y = HEIGHT- 130
player_y = init_y

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
    play = pygame.rect.Rect(120, player_y + 10), (25, 60)
    # jetpack
    pygame.draw.rect(screen, 'white', [100, player_y + 20, 20, 30], 0, 5)
    # player main body
    pygame.draw.ellipse(screen, 'orange', [120, player_y + 20, 20, 50])
    return play





# main game loop (screen, player)
run = True
while run:
    timer.tick(fps)
    lines = draw_screen(lines)
    player = draw_player

    for event in pygame.event.get():
        # make able to quit the game
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()
