import pygame
import pygame as pygame
from pygame import mixer
import time
from pygame.locals import *
from pynput import *
import math


pygame.init()


#░█████╗░██╗░░░██╗██████╗░███████╗██╗░░░██╗░██████╗         ██╗░░░██╗░█████╗░██████╗░░██████╗
#██╔══██╗██║░░░██║██╔══██╗██╔════╝╚██╗░██╔╝██╔════╝         ██║░░░██║██╔══██╗██╔══██╗██╔════╝
#███████║██║░░░██║██║░░██║█████╗░░░╚████╔╝░╚█████╗░         ╚██╗░██╔╝███████║██████╔╝╚█████╗░
#██╔══██║██║░░░██║██║░░██║██╔══╝░░░░╚██╔╝░░░╚═══██╗         ░╚████╔╝░██╔══██║██╔══██╗░╚═══██╗
#██║░░██║╚██████╔╝██████╔╝███████╗░░░██║░░░██████╔╝         ░░╚██╔╝░░██║░░██║██║░░██║██████╔╝
#╚═╝░░╚═╝░╚═════╝░╚═════╝░╚══════╝░░░╚═╝░░░╚═════╝░         ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░

username = 0 # to print the username somewhere
skin = 0  # I will set these for you so you can read them to send on server
x = 0
y = 0
shooting = False








# Screen
screenx = 960
screeny = 540
screen = pygame.display.set_mode((screenx, screeny), RESIZABLE)
w, h = pygame.display.get_surface().get_size()

#vars
noloop = False
#Backround features
backround1 = pygame.image.load("costume1.svg")
# Images
font = pygame.font.Font("White On Black.ttf", 32)
Slide1 = font.render("A thecyberden Game", True, (255, 255, 255))
Slide2 = font.render("Made With Myexgiko", True, (255, 255, 255))
Login_button = font.render("Login", True, (255, 255, 255))
Loading = font.render("Loading", True, (255, 255, 255))
icon = pygame.image.load("Shadow shooters logo.svg")
pygame.display.set_icon(icon)
#upscale
backround1 = pygame.transform.scale(backround1, (w, h))

# window stuff
pygame.display.set_caption("Shadow Shooters")
# Music
mixer.init()
mixer.music.load("main_theme.wav")
mixer.music.play()

# Start
Start_Time = time.time()
# Stages of game
Area_Game = 1


# Main Loop
running = True
while running:
    screen.fill((0, 0, 0))
    seconds = (time.time() - Start_Time)
    print(seconds)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if int(seconds) > 2 and Area_Game == 1:
        Area_Game = 2
    if int(seconds) > 6 and Area_Game == 2:
        Area_Game = 3
    mouse_x, mouse_y = pygame.mouse.get_pos()
    w, h = pygame.display.get_surface().get_size()
    # upscale
    backround1 = pygame.transform.scale(backround1, (w + 100, w + 100))
    # game events

    #DEV STUFF REMOVE WHEN DONE
    #
    #
    #

    if Area_Game == 1:

        screen.blit(Slide1, ((w / 2) - 175, (h / 2) - 20))
    if Area_Game == 2:
        screen.blit(Slide2, ((w / 2) - 175, (h / 2) - 20))
    if Area_Game == 3:
        screen.blit(backround1, ((mouse_x * 0.05)-100, (mouse_y * 0.05)-175))
        rectx = (w/2)-60
        recty = (h/2)+90
        rectw = 120
        recth = 60
        if rectx < mouse_x and recty < mouse_y and (rectx + rectw) > mouse_x and (recty + recth) > mouse_y:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(rectx-5, recty-5, rectw+10, recth+10))
        else:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(rectx, recty, rectw, recth))
        if event.type == pygame.MOUSEBUTTONUP and rectx < mouse_x and recty < mouse_y and (rectx + rectw) > mouse_x and (recty + recth) > mouse_y:
            Area_Game = 4
            mixer.music.load("Clock Ticking2.wav")
            mixer.music.play()
        screen.blit(Login_button, ((w / 2) - 50, (h / 2) + 100))

    if Area_Game == 4:
        pygame.draw.circle(screen, (35, 35, 35), [w/2, (math.sin(seconds) * 100) + h/2], 20, 0)
        pygame.draw.circle(screen, (35, 35, 35), [(math.sin(seconds) * 100) + w/2, h/2], 20, 0)
        screen.blit(Loading, (20, h-60))
    if Area_Game == 5:
        print("indent error fix")
    pygame.display.update()
