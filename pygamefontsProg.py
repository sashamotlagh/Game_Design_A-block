#sasha motlagh
#create Window for settings in your game
import pygame, os,random,time
os.system('cls')
pygame.init()

## LISTS FOR MENU MESSAGES
menu_list=["instructions", "settings","level 1","level 2","scoreboard","exit"]
settingMessages=["Screen Size", "Background colors", "Object Colors","Sounds On/Off"]
instructionsMessages=["1. use the wasd keys to move player 1","\n2. use the arrow keys to move player 2","\n3. try to increase the size of the circle"]
Screensizeoptions=["small","medium","large"]
bgcolorchoices=["red","white","green","blue"]
colorchoices=["red","white","green","blue"]
sound=["on","off"]
#GLOBAL VARIABLES
colors = {'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,145), 'white':(255,255,255), 'purple':(150,0,150), 'orange':(255, 165, 0)}
WHITE=colors.get('white')
BLACK=colors.get('black')
ORANGE=colors.get('orange')
RED=colors.get('red')
BLUE=colors.get('blue')

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
TITLE_FONT=pygame.font.SysFont('arial', 80)
MENU_FONT=pygame.font.SysFont('arial', 40)
text= TITLE_FONT.render('message',1,RED)

def display_Title(message):
    win.fill(BLACK)
    pygame.time.delay(100)
    text= TITLE_FONT.render(message,1,RED)
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
        pygame.draw.rect(win, WHITE, square)
        text=MENU_FONT.render(word,1,RED)
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
    if display_Title==True:
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                run=False
                mouse_pressed=0
            if eve.type==pygame.MOUSEBUTTONDOWN:
                mouse_pressed=pygame.mouse.get_pressed()
            if mouse_pressed[0]:
                mouse_pos=pygame.mouse.get_pos()
                print(mouse_pos)
            #main menu back button
            if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>490 and mouse_pos[1]<215:
                win.fill(WHITE)
                settingMessages("Settings")
                pygame.display.set_caption("Settings")
                mouse_pos=pygame.mouse.get_pos()
            if mouse_pos==True:
                    x=70
                    y=190
                    square.x=x
                    square.y=y
            for i in range(0, len(settingMessages)):
                    word= settingMessages[i]
                    pygame.draw.rect(win, RED, square)
                    text=MENU_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    y += 100
                    square.y=y

pygame.quit()