#sasha motlagh
#10/27/21
#more distinguished menu

import pygame
pygame.init()
colors = {'black':(0,0,0),'red':(255,0,0),'green':(0,255,0),'purple':(0,0,255)}
menu_message=["Instructions","Scoreboard","Settings","Level 1","Level 2","Exit"]
messages=["Screensize","Background Color","Object Color","Sounds On/Off"]
BLACK=colors.get('black')
WHITE=colors.get('white')
GREEN=colors.get('green')
PURPLE=colors.get('purple')
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")
# title_font = pygame.font.SysFont(name, size, bold=False, italic=False)
title_font = pygame.font.SysFont("arial", 80, italic=False)
subtitle_font = pygame.font.SysFont("arial", 50, italic = True)
text= title_font.render(menu_message,1,colors.get("black"))
WORDS_FONT=pygame.font.Sysfont('arial',70,italic=True)

wbox=25
hbox=25
square=pygame.Rect(10,10,wbox,hbox)

def display_title(menu_message):
    pygame.time.delay(100)
    text = title_font.render(menu_message, 1, BLACK)
    window.blit(text, (WIDTH/2 - text.get_width()/2, 70))
    pygame.display.flip()
    pygame.time.delay(100)
def display_subtitle(messages, x, y):
    pygame.time.delay(100)
    text = subtitle_font.render(messages, 1, BLACK)
    window.blit(text, (x, y))
    pygame.display.flip()
    pygame.time.delay(100)
def display_Menu(messages):
    x=70
    y=190
    square.x=x
    square.y=y
    for i in range(0,len(messages)):
        word=messages[i]
        pygame.draw.rect(window,GREEN,square)
        text=WORDS_FONT.render(word,1,BLACK)
        window.blit(text,(x+wbox+10,y))
        pygame.display.flip()
        pygame.time.delay(100)
        y+=100
        square.y=y

window.fill(WHITE)
display_title("Settings",WIDTH/2-text)
display_Menu(menu_message)
pygame.time.delay(200)

#fix this thing
run = True
count = 0
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False
            pygame.quit()
    if eve.type==pygame.MOUSEBUTTONDOWN:
        mouse_pressed=pygame.mouse.get_pressed
        if mouse_pressed[0]:
            mouse_position=pygame.mouse.get_pos()
            if mouse_position[0]>=70 and mouse_position[0]<=230 and mouse_position[1]>=190 and mouse_position[1]<=210:
                window.fill(WHITE)
                display_title("Screensize",WIDTH/2-text.get_width()/2,70)

    if count == 0:
        window.fill(BLACK)
        pygame.time.delay(300)
    display_Menu()
    print(pygame.mouse.get_pos())
    #little box size wbox=25 hbox=25 at x=70 y=190
    #space between boxes is y=290+n(100) where n is the number of the bullet in the list
    #x stays 70 for boxes
