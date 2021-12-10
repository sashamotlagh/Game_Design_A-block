#11/18/21
import pygame as py, os
py.init() #starting pygame working

menu_message=["Instructions","Scoreboard","Themes","Level 1","Level 2","Level 3","Exit"]
Themes=["Beach","Neon","Winter","Spring","Library","Fall","Apocolypse"]
back_message=("Back")
size_message=("300x500","600x1000","1200x1500")
win_message=["instructions to win"]
#listss that get chosen from during the menu pressing

colors = {'black':(0,0,0),'red':(255,0,0),'green':(0,255,0),'purple':(0,0,255)}
BLACK=colors.get('black')
WHITE=colors.get('white')
GREEN=colors.get('green')
PURPLE=colors.get('purple')
WIDTH = 800
HEIGHT = 1100
screen = py.display.set_mode((WIDTH,HEIGHT)) 
#size of the initial window

MAINMENU=True
SETTINGS=False
INSTRUCTIONS=False
BACKGROUND=False
SCREEN=False
LEVEL1=False
LEVEL2=False
SCOREBOARD=False
OBJECTCOLOR=False
#global variables

py.display.set_caption("Setting Window")
#the name of the caption of the window

bg = py.image.load('game images/final game images/scrabble-game-tiles-random.jpg')
#add 3 sizes for backgrounds because you need to have different screen sizes

beach=py.image.load('game images/final game images/beach.jpg')
neon=py.image.load('game images/final game images/neon.png')
apocolypse=py.image.load('game images/final game images/apocolypse.jpg')
winter=py.image.load('game images/final game images/winter.png')
#lists for the backgrounds

TITLE_FONT = py.font.SysFont("helvetica", 80, italic=False)
SUBTITLE_FONT = py.font.SysFont("helvetica", 50, italic = True)
text= TITLE_FONT.render(menu_message[0],1,colors.get("black"))
INSTRUCTIONS_FONT=py.font.SysFont('helvetica',70,italic=True)
#font decisions for different parts of the window
wbox=25
hbox=25
square=py.Rect(10,10,wbox,hbox)
#where the button press occurs

screen.blit(bg,(0,0))
py.display.set_caption('Wordscapes')
py.display.flip()
#
clock= py.time.Clock()
#start the clock make the game work on time delays
run=True
#begin the clock and the program's timing

def display_title(menu_message):
    py.time.delay(100)
    text=TITLE_FONT.render(menu_message,30, BLACK )
    screen.blit(text, (WIDTH/2-text.get_width()/2, 30) )
    py.display.update()
    py.time.delay(100)
#defining the display_title variabel to set up all the menus titles

def display_subtitle(message, y):
    py.time.delay(100)
    text = SUBTITLE_FONT.render(message, 1, BLACK)
    screen.blit(text, (10, y))
    py.display.update()
    py.time.delay(100)
#defining the display_subtitle variable

def display_Menu(menu_message):
    x=70
    y=190
    square.x=x
    square.y=y
    for i in range(0,len(menu_message)):
        word=menu_message[i]
        py.draw.rect(screen,BLACK,square)
        text=INSTRUCTIONS_FONT.render(word,1,BLACK)
        screen.blit(text,(x+wbox+10,y))
        py.display.flip()
        py.time.delay(100)
        y+=100
        square.y=y
#showing the list to display the messages in the menu_message list

def display_back():
                x=500
                y=800
                square.x=x
                square.y=y
                for i in range(0,len(back_message)):
                    word= back_message[i]
                    py.draw.rect(screen, GREEN, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    screen.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    square.y=y
#defining the back button function to go from screens to the main menu

a=("A")
b=("B")
c=("C")
d=("D")
e=("E")
f=("F")
g=("G")
h=("H")

lp= 150
jp= 100

def level1_game():
    win.blit(bg, (0,0))
    py.display.set_caption("Wordscape Level 1")
    py.display.flip() 
    while lp>=150 and jp>=100:

    
#defining how the first level works

def display_Menu():
    x=60
    y=100
    square.x=x
    square.y=y
    for i in range(0, len(menu_message)):
        word= menu_message[i]
        py.draw.rect(screen, BLACK , square)
        text=SUBTITLE_FONT.render(word,10, BLACK)
        screen.blit(text, (x+wbox+10, y))
        py.display.flip()
        py.time.delay(100)
        y += 100
        square.y=y
        py.display.set_caption("Menu Window")

display_title(menu_message)
ysub=200
py.time.delay(200)
display_Menu()
#add scoreboard

run=True
counter=1
back=1
#starting the program with counter and back working

while run:
    clock.tick(18)
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run=False
#beginning the run for the actual game that allows the program to run while run=true
    if eve.type==py.MOUSEBUTTONDOWN:
        mouse_pressed=py.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos=py.mouse.get_pos()
            print(py.mouse.get_pos())
            if mouse_pos[0]>=60 and mouse_pos[0]<=85 and mouse_pos[1]>490 and mouse_pos[1]<515 and counter==1:
                screen.blit(bg)
                display_title("Settings")
                py.display.set_caption("Setting Window")
                mouse_pos=py.mouse.get_pos()
                counter +=1
                #

                x=70
                y=190
                square.x=x
                square.y=y
                for i in range(0, len(Themes)):
                    word= Themes[i]
                    py.draw.rect(screen, BLACK, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    screen.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    py.time.delay(100)
                    y += 100
                    square.y=y
                back+=1
                x=660
                y=730
                square.x=x
                square.y=y
                for i in range(0,len(back_message)):
                    word= back_message[i]
                    py.draw.rect(screen, BLACK, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    screen.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    square.y=y            


            if mouse_pos[0]>60 and mouse_pos[0]<=85 and mouse_pos[1]>285 and mouse_pos[1]<=315 and counter==1:
                screen.fill(bg)
                display_title('Instructions')
                py.display.set_caption("instructions window")
                x=60
                y=100
                square.x=x
                square.y=y
                #instructions window button
                for i in range(0,len(back_message)):
                    word= back_message[i]
                    py.draw.rect(screen, BLACK, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    screen.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    square.y=y
                back+=1
                counter+=1
                x=400
                y=800
                square.x=x
                square.y=y
            
            if mouse_pos[0]>60 and mouse_pos[0]<=85 and mouse_pos[1]>285 and mouse_pos[1]<=315 and counter==2:
                screen.fill(bg)
                display_title('Screen Size')
                py.display.set_caption("Screen Size Window")
                x=60
                y=100
                square.x=x
                square.y=y
                for i in range(0, len(size_message)):
                    word= size_message[i]
                    py.draw.rect(screen, BLACK, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    screen.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    py.time.delay(100)
                    y += 100
                    square.y=y
                display_back()
                counter+=1
                back+=1


            if mouse_pos[0]>660 and mouse_pos[0]<=685 and mouse_pos[1]>430 and mouse_pos[1]<=455 and back==2:
                screen.fill(bg)
                display_title('Menu')
                counter-=1
                back-=1
                display_Menu()
            if mouse_pos[0]>=60 and mouse_pos[0]<=85 and mouse_pos[1]>285 and mouse_pos[1]<315 and counter==1:
                level1_game()
                display_back()
                back+=1
                counter+=1

            if mouse_pos[0]>660 and mouse_pos[0]<=685 and mouse_pos[1]>430 and mouse_pos[1]<=455 and back==3:
                screen.fill(bg)
                
                counter-=1
                back-=1
                screen.fill(bg)
                display_title("Backgrounds")
                py.display.set_caption("Themes")
                mouse_pos=py.mouse.get_pos()
                counter +=1
                back-=1
                x=70
                y=190
                square.x=x
                square.y=y
                for i in range(0, len(Themes)):
                    word= Themes[i]
                    py.draw.rect(screen, BLACK, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    screen.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    square.y=y
                back+=1
                x=660
                y=730
                square.x=x
                square.y=y

                for i in range(0,len(back_message)):
                    word= back_message[i]
                    py.draw.rect(screen, BLACK, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    screen.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    square.y=y    
                
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>190 and mouse_pos[1]<=215 and counter==4:
                WIDTH+=50
                HEIGHT+=50
                screen=py.display.set_mode((WIDTH,HEIGHT))   
                display_back
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>290 and mouse_pos[1]<315 and counter==4:
                WIDTH-=50
                HEIGHT-=50
                screen=py.display.set_mode((WIDTH,HEIGHT))   
                display_back                     
            print(counter)
            print(back)

level1_game