#MAria Suarez

#CReate Window for settings in your game

import pygame, os,random,time
os.system('cls')
pygame.init()

 

## LISTS FOR MENU MESSAGES
menu_list=["intro", "settins"]
settingMessages=["Screen Size", "Background colors", "Object Colors","Sounds On/Off"]

#GLOBAL VARIABLES

colors = {'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,145), 'white':(255,255,255), 'purple':(150,0,150), 'orange':(255, 165, 0)}

WHITE=colors.get('white')

BLACK=colors.get('black')

ORANGE=colors.get('orange')

 

WIDTH=800

HEIGHT=800

wbox=30

hbox=30

x=70

y=150

win=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Setting Window")

square=pygame.Rect(x,y, wbox,hbox)

#Declare FONTS

TITLE_FONT=pygame.font.SysFont('comicsans', 80)

MENU_FONT=pygame.font.SysFont('comicsans', 40)

text= TITLE_FONT.render('message',1,BLACK)

 

def display_Title(message):

    win.fill(WHITE)

    pygame.time.delay(100)

    text= TITLE_FONT.render(message,1,BLACK)

    xm=WIDTH/2-text.get_width()/2

    ym=40

    win.blit(text, (xm,ym))

    pygame.display.update()

    pygame.time.delay(100)

 

def Menu_function(messages):
    pygame.time.delay(100)
    ym=y
    xm=x+wbox+10
    for i in range(0,len(messages)):
        word=messages[i]
        pygame.draw.rect(win, ORANGE, square)
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm,ym))
        pygame.display.flip()
        pygame.time.delay(100)
        ym +=100
        square.y=ym

display_Title("MENU")
Menu_function(menu_list)
mouse_pressed=0
run=True

while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
        if eve.type==pygame.MOUSEBUTTONDOWN:

            mouse_pressed=pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos=pygame.mouse.get_pos()
            if mouse_pos[0]>=70 and mouse_pos[0]<=230 and mouse_pos[1] >=190 and mouse_pos[1]<210:
                win.fill(WHITE)
                display_Title("Screen Size",WIDTH/2-text.get_width()/2, 70 )

pygame.quit()