import pygame, os,random,time

from pygame import color
os.system('cls')
pygame.init()

## LISTS FOR MENU MESSAGES

screenMessage=[ "1000x600", "1500x900", "2000x1200"]
settingMessages=["Screen Size", "Themes","Sounds On/Off"]
mainMenu=["Instructions", 'Settings', "Level 1", "Level 2", "Level 3", "ScoreBoard", "Exit"]
colors = {'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,145), 'white':(255,255,255), 'purple':(150,0,150), 'orange':(255, 165, 0)}
words_easy= "SQUISH"
words_medium="GUARD"
words_hard="BORDEAUX"
A=pygame.image.load('game images/letters/a.png')#65
B=pygame.image.load('game images/letters/b.png')#66
C=pygame.image.load('game images/letters/c.png')#67
D=pygame.image.load('game images/letters/d.png')#68
E=pygame.image.load('game images/letters/e.png')#69
F=pygame.image.load('game images/letters/f.png')#70
G=pygame.image.load('game images/letters/g.png')#71
H=pygame.image.load('game images/letters/h.png')#72
I=pygame.image.load('game images/letters/i.png')#73
J=pygame.image.load('game images/letters/j.png')#74
K=pygame.image.load('game images/letters/k.png')#75
L=pygame.image.load('game images/letters/l.png')#76
M=pygame.image.load('game images/letters/m.png')#77
N=pygame.image.load('game images/letters/n.png')#78
O=pygame.image.load('game images/letters/o.png')#79
P=pygame.image.load('game images/letters/p.png')#80
Q=pygame.image.load('game images/letters/q.png')#81
R=pygame.image.load('game images/letters/r.png')#82
S=pygame.image.load('game images/letters/s.png')#83
T=pygame.image.load('game images/letters/t.png')#84
U=pygame.image.load('game images/letters/u.png')#85
V=pygame.image.load('game images/letters/v.png')#86
W=pygame.image.load('game images/letters/w.png')#87
X=pygame.image.load('game images/letters/x.png')#88
Y=pygame.image.load('game images/letters/y.png')#89
Z=pygame.image.load('game images/letters/z.png')#90
letters=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
RIGHT=pygame.image.load('game images/final game images/right.png')
WRONG=pygame.image.load('game images/final game images/wrong.png')
    

#GLOBAL VARIABLES
WHITE=colors.get('white')
BLACK=colors.get('black')
ORANGE=colors.get('orange')
COLOR=WHITE
MAINMENU=True
SETTINGS=False
INSTRUCTIONS=False
BACKGROUND=False
SCREEN=False
LEVEL1=False
LEVEL2=False
LEVEL3=False
SCOREBOARD=False
EXIT=False
flag=False

# Screen and square definition
WIDTH=1500
HEIGHT=900
wbox=30
hbox=30
x=60
y=150
xs=30
ys=180
bg1 = pygame.image.load('game images/bg1medium.jpg')
bg2 = pygame.image.load('game images/bg1large.jpg')
bg05= pygame.image.load('game images/bg1small.jpg')
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Setting Window")
square=pygame.Rect(x,y, wbox,hbox)
screenSize=pygame.Rect(xs,ys,wbox*4, hbox*4)
win.blit(bg1,(0,0))
squaresSize=[pygame.Rect(xs,ys,wbox*4, hbox*4), pygame.Rect(xs,ys,wbox*4, hbox*3), pygame.Rect(xs,ys,wbox*3, hbox*3)]
#Declare FONTS
TITLE_FONT=pygame.font.SysFont('helvetica', 80)
MENU_FONT=pygame.font.SysFont('helvetica', 40)
INSTRUCTIONS_FONT=pygame.font.SysFont('helvetica', 30)
text= TITLE_FONT.render('message',1,ORANGE)
#New window title
#images
#Function to print Titles to all screens
def display_Title(message,ym):
    pygame.time.delay(100)
    text= TITLE_FONT.render(message,1,ORANGE)
    xm=WIDTH/2-text.get_width()/2
    win.blit(text, (xm,ym))
    pygame.display.update()
    pygame.time.delay(100)

def display_backgrounds(): #work on this to clarify the options!!!
    if xm>=70 and xm<=95 and ym>=150 and ym<=175:
        win.blit(bg1,(0,0))
        pygame.display.set_caption("Instructions")
        display_Title("Instructions", 70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        INSTRUCTIONS = True               
    if xm>=70 and xm<=95 and ym>=250 and ym<=275: #71, 193. 93,193. 93, 212. 71, 211
        win.blit(bg1,(0,0))
        pygame.display.set_caption("Settings")
        display_Title("SETTINGS",  70)
        Menu_function(settingMessages)
        display_Title("BACK", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        BACKGROUND = True 
    if xm>=70 and  xm<=95 and ym>=350 and ym<=375: #71, 193. 93,193. 93, 212. 71, 211
        win.blit(bg1,(0,0))
        pygame.display.set_caption("Level 1")
        display_Title("SQUISH",  70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        BACKGROUND= True
    if xm>=50 and xm<=150 and ym>=10 and ym<=40:
        print("x")
#Function to print all the menus 
def Menu_function(line):
    pygame.time.delay(100)
    ym=y
    square.y=y
    xm=x+wbox+10
    for i in range(0,len(line)):
        word=line[i]
        pygame.draw.rect(win, ORANGE, square)
        text=MENU_FONT.render(word,1,ORANGE)
        win.blit(text,(xm,ym))
        pygame.display.flip()
        pygame.time.delay(100)
        ym +=100
        square.y=ym

def scoreBoard(): #reading the scoreboard file to the player and updating it
    myFile=open('leaderboard.txt','w')
    myFile.close()
    myFile=open('leaderboard.txt','a')
    myFile.close()

def MainMenuWin(xm,ym):
    global MAINMENU
    global INSTRUCTIONS
    global SETTINGS
    global LEVEL1
    global LEVEL2
    global LEVEL3
    global SCOREBOARD
    if xm>=70 and xm<=95 and ym>=150 and ym<=175:
        win.blit(bg1,(0,0))
        pygame.display.set_caption("Instructions")
        display_Title("Instructions", 70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        INSTRUCTIONS = True               
    if xm>=70 and xm<=95 and ym>=250 and ym<=275: #71, 193. 93,193. 93, 212. 71, 211
        win.blit(bg1,(0,0))
        pygame.display.set_caption("Settings")
        display_Title("SETTINGS",  70)
        Menu_function(settingMessages)
        display_Title("BACK", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        SETTINGS = True 
    if xm>=70 and  xm<=95 and ym>=350 and ym<=375: #71, 193. 93,193. 93, 212. 71, 211
        win.blit(bg1,(0,0))
        pygame.display.set_caption("Level 1")
        display_Title("SQUISH",  70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        LEVEL1 = True
    if xm>=70 and  xm<=95 and ym>=450 and ym<=475: #71, 193. 93,193. 93, 212. 71, 211
        win.blit(bg1,(0,0))
        pygame.display.set_caption("Gay")
        display_Title("GUARD",  70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        LEVEL2 = True
    if xm>=70 and  xm<=95 and ym>=550 and ym<=575: #71, 193. 93,193. 93, 212. 71, 211
        win.blit(bg1,(0,0))
        pygame.display.set_caption("Level 3")
        display_Title("BORDEAUX",  70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        LEVEL2 = True
    if xm>=70 and  xm<=95 and ym>=650 and ym<=675: #71, 193. 93,193. 93, 212. 71, 211
        win.blit(bg1,(0,0))
        pygame.display.set_caption("ScoreBoard")
        display_Title("Scoreboard",  70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        LEVEL3 = True
    if xm>=70 and  xm<=95 and ym>=750 and ym<=775: #71, 193. 93,193. 93, 212. 71, 211
        win.blit(bg1,(0,0))
        display_Title("Exit",  70)
        display_Title("Back", HEIGHT-70)
        pygame.display.update()
        MAINMENU = False
        global run
        run=False
def SettingMenuWin(xm,ym):
    global SETTINGS
    global SCREEN
    global BACKGROUND
   
    if xm>=70 and xm<=95 and ym>=150 and ym<=175:
        win.blit(bg1,(0,0))
        display_Title("Screen Size", 70)
        display_Title("Back", 750)
        pygame.display.update()
        SETTINGS = False
        SCREEN = True  
                   
    if xm>=70 and xm<=95 and ym>=250 and ym<=275 and flag: #71, 193. 93,193. 93, 212. 71, 211
        win.blit(bg1,(0,0))
        display_Title("BACKGROUND COLORS",  70)
        display_Title("BACK", 750)
        pygame.display.update()
        BACKGROUND = True
        SETTINGS = False             

def Menu_Back():
    win.fill(COLOR)
    display_Title("MAIN", 50)
    Menu_function(mainMenu)
    pygame.display.update()
def Setting_Back():
    win.blit(bg1,(0,0))
    display_Title("SETTINGS", 70)
    Menu_function(settingMessages)
    display_Title("Back", HEIGHT-50)
    pygame.display.update()
def Screen_size():
    pygame.time.delay(100)
    ym=ys
    screenSize.x=xs
    xm=xs
    for i in range(0,len(squaresSize)):
        squary=squaresSize[i]
        squary.x=xm
        pygame.draw.rect(win, ORANGE, squary)
        word= screenMessage[i]
        text=MENU_FONT.render(word,1,ORANGE)
        win.blit(text,(xm-10,ym-40))
        pygame.display.flip()
        pygame.time.delay(100)
        xm +=200
    #if xm<HEIGHT-HEIGHT-4 and xm>HEIGHT-HEIGHT-30 and ym<WIDTH-WIDTH-30 and ym<WIDTH-WIDTH-80:
     #   win.blit(bg05,(0,0))

def game_Level1():
    win.blit(bg1, (0,0))
    pygame.display.set_caption("My game 1")
    pygame.display.flip()
    #add your game logic here
    words_easy="SQUISH"
    print(words_easy)
    words_easy=TITLE_FONT.render(words_easy, 1, ORANGE)
    win.blit(words_easy,(590,150))
    pygame.time.delay(50)
    win.blit(bg1, (0,0))
    display_Title("Level 1: guess the word", 70)

    win.blit(A,(30,300))
    win.blit(B,(190,300))
    win.blit(C,(350,300))
    win.blit(D,(510,300))
    win.blit(E,(670,300))
    win.blit(F,(830,300))
    win.blit(G,(990,300))
    win.blit(H,(1150,300))
    win.blit(I,(1310,300))

    win.blit(J,(30,500))
    win.blit(K,(190,500))
    win.blit(L,(350,500))
    win.blit(M,(510,500))
    win.blit(N,(670,500))
    win.blit(O,(830,500))
    win.blit(P,(990,500))
    win.blit(Q,(1150,500))
    win.blit(R,(1310,500))

    win.blit(S,(30,700))
    win.blit(T,(190,700))
    win.blit(U,(350,700))
    win.blit(V,(510,700))
    win.blit(W,(670,700))
    win.blit(X,(830,700))
    win.blit(Y,(990,700))
    win.blit(Z,(1150,700))
    

def game_Level2():
    words_medium="GUARD"
    win.blit(bg1, (0,0))
    pygame.display.set_caption("My game 1")
    pygame.display.flip()
    #add your game logic here
    print(words_medium)
    words_medium=TITLE_FONT.render(words_medium, 1, ORANGE)
    win.blit(words_medium,(590,150))
    pygame.time.delay(50)
    win.blit(bg1, (0,0))
    display_Title("Level 2: guess the word", 70)

    win.blit(A,(30,300))
    win.blit(B,(190,300))
    win.blit(C,(350,300))
    win.blit(D,(510,300))
    win.blit(E,(670,300))
    win.blit(F,(830,300))
    win.blit(G,(990,300))
    win.blit(H,(1150,300))
    win.blit(I,(1310,300))

    win.blit(J,(30,500))
    win.blit(K,(190,500))
    win.blit(L,(350,500))
    win.blit(M,(510,500))
    win.blit(N,(670,500))
    win.blit(O,(830,500))
    win.blit(P,(990,500))
    win.blit(Q,(1150,500))
    win.blit(R,(1310,500))

    win.blit(S,(30,700))
    win.blit(T,(190,700))
    win.blit(U,(350,700))
    win.blit(V,(510,700))
    win.blit(W,(670,700))
    win.blit(X,(860,700))
    win.blit(Y,(1020,700))
    win.blit(Z,(1180,700))

def game_Level3():
    win.blit(bg1, (0,0))
    words_hard="BORDEAUX"
    pygame.display.set_caption("My game 1")
    pygame.display.flip()
    #add your game logic here
    print(words_hard)
    words_hard=TITLE_FONT.render(words_hard, 1, ORANGE)
    win.blit(words_hard,(590,150))
    pygame.time.delay(50)
    win.blit(bg1, (0,0))
    display_Title("Level 3: guess the word", 70)

    win.blit(A,(30,300))
    win.blit(B,(190,300))
    win.blit(C,(350,300))
    win.blit(D,(510,300))
    win.blit(E,(670,300))
    win.blit(F,(830,300))
    win.blit(G,(990,300))
    win.blit(H,(1150,300))
    win.blit(I,(1310,300))

    win.blit(J,(30,500))
    win.blit(K,(190,500))
    win.blit(L,(350,500))
    win.blit(M,(510,500))
    win.blit(N,(670,500))
    win.blit(O,(830,500))
    win.blit(P,(990,500))
    win.blit(Q,(1150,500))
    win.blit(R,(1310,500))

    win.blit(S,(30,700))
    win.blit(T,(190,700))
    win.blit(U,(350,700))
    win.blit(V,(510,700))
    win.blit(W,(670,700))
    win.blit(X,(830,700))
    win.blit(Y,(990,700))
    win.blit(Z,(1150,700))

    pygame.display.update()
    display_Title("BACK", HEIGHT-70)
    if xm >335 and xm<460 and ym>745 and ym<795:
                    Menu_Back()
                    MAINMENU = True
                    LEVEL3 = False
    pygame.display.update()
#def display_word():
    # words_easy="SQUISH"
    # print(words_easy)
    # words_easy=TITLE_FONT.render(words_easy, 1, ORANGE)
    # win.blit(words_easy,(590,150))

    # win.blit(A,(30,300))
    # win.blit(B,(190,300))
    # win.blit(C,(350,300))
    # win.blit(D,(510,300))
    # win.blit(E,(670,300))
    # win.blit(F,(830,300))
    # win.blit(G,(990,300))
    # win.blit(H,(1150,300))
    # win.blit(I,(1310,300))

    # win.blit(J,(30,500))
    # win.blit(K,(190,500))
    # win.blit(L,(350,500))
    # win.blit(M,(510,500))
    # win.blit(N,(670,500))
    # win.blit(O,(830,500))
    # win.blit(P,(990,500))
    # win.blit(Q,(1150,500))
    # win.blit(R,(1310,500))

    # win.blit(S,(30,700))
    # win.blit(T,(190,700))
    # win.blit(U,(350,700))
    # win.blit(V,(510,700))
    # win.blit(W,(670,700))
    # win.blit(X,(830,700))
    # win.blit(Y,(990,700))
    # win.blit(Z,(1150,700))

    # pygame.display.update()
#def easy_letters():#letters:D,E,R,H,S,Q,U,I,D,C,A,K,G,A,N,R
a=ord('A')
c=ord('C')
d=ord('D')
e=ord('E')
g=ord('G')
h=ord('H')
i=ord('I')
k=ord('K')
q=ord('Q')
r=ord('R')
s=ord('S')
t=ord('T')
u=ord('U')



# def Color_screen():
#     for key in colors:
#Start Program
display_Title("MENU", 40)
Menu_function(mainMenu)
run=True 
# C:\Users\suarezm\OneDrive - Greenhill School\Game Design\GameDesign2021_Fall_Ablock\cade.py  
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
    mouse_pos=(0,0)
    if eve.type==pygame.MOUSEBUTTONDOWN:
        mouse_pressed=pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos=pygame.mouse.get_pos()
            print(pygame.mouse.get_pos())
            xm=mouse_pos[0]
            ym=mouse_pos[1]
            if MAINMENU:
                MainMenuWin(xm,ym)
            if INSTRUCTIONS:
                myFile=open('instructions.txt', 'r')
                yi=150
                for line in myFile.readlines():
                    text=INSTRUCTIONS_FONT.render(line, 1, ORANGE)
                    win.blit(text, (40,yi))
                    pygame.display.update()
                    pygame.time.delay(100)
                    yi+=50
                myFile.close()
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Menu_Back()
                    MAINMENU = True
                    INSTRUCTIONS = False
            if SETTINGS:
                SettingMenuWin(xm,ym)
                flag=True
                if xm >335 and xm<460 and ym>HEIGHT-70 and ym<HEIGHT:
                    Menu_Back()
                    MAINMENU = True
                    SETTINGS = False
                    flag=False
            if SCREEN:
                Screen_size()
                display_Title("Back", HEIGHT-70)
                pygame.display.update()
                if xm>65 and xm <160 and ym>170 and ym<300: 
                    WIDTH=1000
                    HEIGHT=600
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    win.blit(bg05,(0,0))
                    Screen_size()
                    display_Title("Back", HEIGHT-70)

                    pygame.display.update()
                if xm>230 and xm<=360 and ym>170 and ym<280: 
                    WIDTH=1500
                    HEIGHT=900
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    win.blit(bg1,(0,0))
                    Screen_size()
                    display_Title("Back", HEIGHT-70)

                    pygame.display.update()
                if xm>450 and xm <540 and ym>200 and ym<290: 
                    WIDTH=2000
                    HEIGHT=1200
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    win.blit(bg2,(0,0))
                    Screen_size()
                    display_Title("Back", HEIGHT-70)

                    pygame.display.update()
                
                if xm >415 and xm<600 and ym>530 and ym<600:
                    Setting_Back()
                    SETTINGS = True
                    SCREEN = False
            if BACKGROUND:
                display_backgrounds()

                if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                    Setting_Back()
                    SETTINGS = True
                    BACKGROUND = False
            if LEVEL1: #letters:D,E,R,H,S,Q,U,I,D,C,A,K,G,A,N,R
                game_Level1()
                chances=0
                squish=[S,Q,U,I,S,H]
                #if the press is correct
                #fix all of the buttons coordinates for thisa
                if xm>=300 and xm<=400 and ym>=450 and ym<=570:
                         win.blit(RIGHT, (300,450))
                if xm>=540 and xm<=680 and ym>=450 and ym<=590:
                         win.blit(RIGHT, (560,450))
                if xm>=790 and xm<=910 and ym>=450 and ym<=590:
                         win.blit(RIGHT, (790,450))
                if xm>=1040 and xm<=1140 and ym>=450 and ym<=570:
                         win.blit(RIGHT, (1040,450))
                if xm>=1280 and xm<=1380 and ym>=450 and ym<=570:
                         win.blit(RIGHT, (1280,450))
                if xm>=90 and xm<=190 and ym>=700 and ym<=920:
                        win.blit(RIGHT, (90,700))
                if xm>=300 and xm<=400 and ym>=700 and ym<=920:
                         win.blit(RIGHT, (300,700))
                if xm>=550 and xm<=650 and ym>=700 and ym<=920:
                       win.blit(RIGHT, (560,700))
                if xm>=790 and xm<=890 and ym>=700 and ym<=920:
                        win.blit(RIGHT, (790,700))
                if xm>=1040 and xm<=1140 and ym>=700 and ym<=920:
                         win.blit(RIGHT, (1040,700))
                if xm>=1280 and xm<=1380 and ym>=700 and ym<=920:
                         win.blit(RIGHT, (1280,700))
                #now for the wrong buttons
                if xm>=90 and xm<=190 and ym>=450 and ym<=570:
                         win.blit(WRONG, (90,450))
                if xm>=300 and xm<=400 and ym>=450 and ym<=570:
                         win.blit(WRONG, (300,450))
                if chances==3:
                    win.blit(WRONG,(WIDTH/2,HEIGHT/2))

                scoreBoard()

                #game_Level1()
                if xm >WIDTH-400 and xm<WIDTH-350 and ym>745 and ym<795:
                    win.blit("Back",(200,745))
                    Menu_Back()
                    MAINMENU = True
                    LEVEL1 = False
                pygame.display.flip()
                pygame.display.flip()
            if LEVEL2:
                #Play game
                game_Level2()

                if chances==3:
                    win.blit(WRONG,(WIDTH/2,HEIGHT/2))
                scoreBoard()
                display_Title("BACK", HEIGHT-70)
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Menu_Back()
                    MAINMENU = True
                    LEVEL2 = False
            if LEVEL3:
                #Play game
                game_Level3()

                if chances==3:
                    win.blit(WRONG,(WIDTH/2,HEIGHT/2))
                scoreBoard()
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Menu_Back()
                    MAINMENU = False
                    LEVEL3 = True
                pygame.display.flip()
            if EXIT:
                EXIT= True
                pygame.quit()

