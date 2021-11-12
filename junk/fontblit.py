#sasha motlagh
#10/25/21
#learning fonts and blit

import pygame as py, os, random, time
py.init()
black = (0, 0, 0)
white = (255, 255, 255)
width = 800
height = 800
window = py.display.set_mode((width, height))
py.display.set_caption("settings")
# title_font = py.font.SysFont(name, size, bold=False, italic=False)
title_font = py.font.SysFont("arial", 80)
subtitle_font = py.font.SysFont("arial", 50, italic = True)
def display_title(message):
    py.time.delay(100)
    text = title_font.render(message, 1, white)
    window.blit(text, (width/2 - text.get_width()/2, 70))
    py.display.flip()
    py.time.delay(100)
def display_subtitle(message, x, y):
    py.time.delay(100)
    text = subtitle_font.render(message, 1, white)
    window.blit(text, (x, y))
    py.display.flip()
    py.time.delay(100)
run = True
count = 0
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run = False
            py.quit()
    if count == 0:
        window.fill(black)
        display_title("settings")
        py.time.delay(300)
        
        display_subtitle("window size",80, 250)
    
        py.time.delay(300)
        display_subtitle("background color", 80, 350)
        
        py.time.delay(300)
        display_subtitle("object colors", 80, 450)
        
        py.time.delay(300)
        display_subtitle("sound (on/off)", 80, 550)
        
        py.time.delay(300)
        count += 1
#print the rest of the menu in the settings
    #window size
    #background color
    #object colors
    #sound (on/off)
    # display_title("oops...")
    # py.time.delay(300)
    # window.fill(black)
py.quit()