#ravi vasan

#10/25/21

#learning fonts and blit

import pygame as py, os, random, time

from pygame import display

os.system ('cls')

py.init()
colors = {'black':(0,0,0),
          'red':(255,0,0), 
          'green':(0,255,0), 
          'blue':(0,0,255), 
          'white':(255,255,255), 
          'purple':(150,0,150)}
keyList = list(colors.keys())
color = random.choice(keyList)

bmessages = ["back"]
settings_messages = ["screensize", "background color", "object colors", "sound (on/off)"]
menu_messages = ["instructions", "settings", "scoreboard", "level 1", "level 2", "exit"]
instructions_messages = ["make your circle touch the square", 
                        "chase the square", "do that 5 times", 
                        "use the up, down, and side buttons"] 
screensize_messages = ["bigger", "smaller"]
MainMenu = True
Settings = False
Instructions = False
Background_Color = False
Screensize = False
Object_Color = False
Level_1 = False
Level_2 = False
Scoreboard = False


width = 800
height = 800

window = py.display.set_mode((width, height))
color = colors.get(color)

# title_font = py.font.SysFont(name, size, bold=False, italic=False)
title_font = py.font.SysFont("arial", 80)
subtitle_font = py.font.SysFont("arial", 50, italic = True)
text = 0
def display_title(message):
    py.time.delay(100)
    text = title_font.render(message, 1, colors.get("black"))
    window.blit(text, (width/2 - text.get_width()/2, 70))
    py.display.flip()
    py.time.delay(100)
def display_subtitle(message, x, y):
    py.time.delay(100)
    text = subtitle_font.render(message, 1, colors.get("black"))
    window.blit(text, (x, y))
    py.display.flip()
    py.time.delay(100)


#these are the squares that will go next to the menu selections
wbox = 25
hbox= 25
square = py.Rect(10, 10, wbox, hbox)

def display_selection(messages):
    x = 70
    y = 240
    square.x = x
    square.y = y
    for i in range(0, len(messages)):
        word = messages[i]
        py.draw.rect(window, colors.get("black"), square)
        text = subtitle_font.render(word, 1, colors.get("black"))
        window.blit(text, (x + wbox + 20, y - 20))
        py.display.flip()
        py.time.delay(100)
        y += 100
        square.y = y

def display_back():
                x=660
                y=730
                square.x=x
                square.y=y
                for i in range(0,len(bmessages)):
                    word= bmessages[i]
                    py.draw.rect(win, colors.get("purple"), square)
                    text=subtitle_font.render(word, 10, colors.get("black"))
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    
                    square.y=y

counter=1


window.fill(colors.get("white"))
display_title("MENU")
py.time.delay(100)
display_selection(menu_messages)

ymin = 95
ymax = 265
run = True
count = 1
back = 1
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run=False
    if eve.type==py.MOUSEBUTTONDOWN:
        mouse_pressed=py.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos=py.mouse.get_pos()
            print(mouse_pos)
            if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>490 and mouse_pos[1]<515 and counter==1:
                win.fill(colors.get("white"))
                display_title("Settings")
                py.display.set_caption("Setting Window")
                mouse_pos=py.mouse.get_pos()
                counter +=2
                
                x=70
                y=190
                square.x=x
                square.y=y
                for i in range(0, len(instructions_messages)):
                    word= instructions_messages[i]
                    py.draw.rect(win, colors.get("purple"), square)
                    text=subtitle_font.render(word,10, colors.get("black"))
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    py.time.delay(100)
                    y += 100
                    square.y=y
                back+=1
                x=660
                y=730
                square.x=x
                square.y=y
                for i in range(0,len(bmessages)):
                    word= bmessages[i]
                    py.draw.rect(win, colors.get("purple"), square)
                    text=subtitle_font.render(word,10, colors.get("black"))
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    
                    
                    square.y=y            

            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>185 and mouse_pos[1]<=215 and counter==1:
                win.fill(colors.get("white"))
                display_title('Instructions')
                py.display.set_caption("instructions window")
                x=70
                y=190
                square.x=x
                square.y=y
                
                for i in range(0, len(instructions_messages)):
                    word= instructions_messages[i]
                    py.draw.rect(win, colors.get("purple"), square)
                    text=subtitle_font.render(word,10, colors.get("black"))
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    py.time.delay(100)
                    y += 100
                    square.y=y
                
                back+=1
                counter+=1
                x=660
                y=730
                square.x=x
                square.y=y
                for i in range(0,len(bmessages)):
                    word= bmessages[i]
                    py.draw.rect(win, colors.get("purple"), square)
                    text=subtitle_font.render(word,10, colors.get("black"))
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    
                    
                    square.y=y

            
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>185 and mouse_pos[1]<=215 and counter==3:
                win.fill(colors.get("white"))
                display_title('Screen Size')
                py.display.set_caption("Screen Size Window")
                x=70
                y=190
                square.x=x
                square.y=y
                for i in range(0, len(screensize_messages)):
                    word= screensize_messages[i]
                    py.draw.rect(win, colors.get("purple"), square)
                    text=subtitle_font.render(word,10, colors.get("black"))
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    py.time.delay(100)
                    y += 100
                    square.y=y
                display_back()
                counter+=1
                back+=1


            if mouse_pos[0]>660 and mouse_pos[0]<=685 and mouse_pos[1]>730 and mouse_pos[1]<=755 and back==2:
                win.fill(colors.get("white"))
                display_title('Menu')
                counter-=2
                back-=1
                display_title()




            if mouse_pos[0]>660 and mouse_pos[0]<=685 and mouse_pos[1]>730 and mouse_pos[1]<=755 and back==3:
                win.fill(colors.get("white"))
                
                counter-=1
                back-=1
                win.fill(colors.get("white"))
                display_title("Settings")
                py.display.set_caption("Setting Window")
                mouse_pos=py.mouse.get_pos()
                counter +=2
                back-=1
                x=70
                y=190
                square.x=x
                square.y=y
                for i in range(0, len(settings_messages)):
                    word= settings_messages[i]
                    py.draw.rect(win, colors.get("purple"), square)
                    text=subtitle_font.render(word,10, colors.get("black"))
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    py.time.delay(100)
                    y += 100
                    square.y=y
                back+=1
                x=660
                y=730
                square.x=x
                square.y=y
                for i in range(0,len(bmessages)):
                    word= bmessages[i]
                    py.draw.rect(win, colors.get("purple"), square)
                    text=subtitle_font.render(word,10, colors.get("black"))
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    
                    
                    square.y=y    
                
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>190 and mouse_pos[1]<=215 and counter==4:
                width+=50
                height+=50
                win=py.display.set_mode((width,height))   
                display_back
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>290 and mouse_pos[1]<315 and counter==4:
                width-=50
                height-=50
                win=py.display.set_mode((width,height))   
                display_back






# while run:
#     if MainMenu == True:
#         for eve in py.event.get():
#             if eve.type == py.QUIT:
#                 run = False
#                 py.quit()
#             if eve.type == py.MOUSEBUTTONDOWN:
#                 mouse_pressed = py.mouse.get_pressed()
#                 if mouse_pressed[0]:
#                     mouse_position = py.mouse.get_pos()
                    
#                     if mouse_position [0] >= 70 and mouse_position[0] <= 240 and mouse_position[1] >= ymin and mouse_position[1] <= ymax:
#                         if MainMenu == False and Instructions == True:
#                             window.fill(colors.get("white"))
#                             display_title("instructions")
#                             display_selection(instructions_messages)
                    
#                     elif mouse_position [0] >= 70 and mouse_position[0] <= 240 and mouse_position[1] >= ymin+100 and mouse_position[1] <= ymax+100:
#                         if MainMenu == False and Settings == True:
#                             window.fill(colors.get("white"))
#                             display_title("settings")
#                             display_selection(settings_messages)
#                         if mouse_position [0] >=70 and mouse_position[0] <= 240 and mouse_position[1] >= ymin+100 and mouse_position[1] <= ymax+100:
#                             if MainMenu == False and Screensize == True:
#                                 window.fill(colors.get("white"))
#                                 display_title("screensize")
                        
#                         if mouse_position [0] >=70 and mouse_position[0] <= 240 and mouse_position[1] >= ymin+200 and mouse_position[1] <= ymax+200:
#                             if MainMenu == False and Background_Color == True:
#                                 window.fill(colors.get("white"))
#                                 display_title("background color")
                        
#                         if mouse_position [0] >=70 and mouse_position[0] <= 240 and mouse_position[1] >= ymin+300 and mouse_position[1] <= ymax+300:
#                             if MainMenu == False and Object_Color == True:
#                                 window.fill(colors.get("white"))
#                                 display_title("object color")
                        
#                         if mouse_position [0] >=70 and mouse_position[0] <= 240 and mouse_position[1] >= ymin+400 and mouse_position[1] <= ymax+400:
#                             if MainMenu == False and Object_Color == True:
#                                 window.fill(colors.get("white"))
#                                 display_title("sound on/off")

#                     elif mouse_position [0] >= 70 and mouse_position[0] <= 240 and mouse_position[1] >= ymin+200 and mouse_position[1] <= ymax+200:
#                         if MainMenu == False and Scoreboard == True:
#                             window.fill(colors.get("white"))
#                             display_title("scoreboard")
                    
#                     elif mouse_position [0] >= 70 and mouse_position[0] <= 240 and mouse_position[1] >= ymin+300 and mouse_position[1] <= ymax+300:
#                         if MainMenu == False and Level_1 == True:
#                             window.fill(colors.get("white"))
#                             display_title("level 1")
                    
#                     elif mouse_position [0] >= 70 and mouse_position[0] <= 240 and mouse_position[1] >= ymin+400 and mouse_position[1] <= ymax+400:
#                         if MainMenu == False and Level_2 == True:
#                             window.fill(colors.get("white"))
#                             display_title("level 2")
                    
#                     elif mouse_position [0] >= 70 and mouse_position[0] <= 240 and mouse_position[1] >= ymin+500 and mouse_position[1] <= ymax+500:
#                         window.fill(colors.get("white"))
#                         py.quit()

    # print(py.mouse.get_pos())

py.quit()

#make a screen for each thing and also make a back button in the bottom right hand corner