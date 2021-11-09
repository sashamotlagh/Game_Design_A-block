#Zain
#10/25

import pygame as py, os, random, time
py.init()
BLACK=(255,255,255)
WHITE=(0,0,0)
PURPLE=(150,0,150)
WIDTH = 800
HEIGHT = 800
bmessages=["Back"]
messages=['Instructions','Level 1','Level 2','Settings','Score Board', 'Exit']
messages2=['Screen size', 'Object Color', 'Sound on/off', ]
Ssmessages=['Larger', 'Smaller', ]
imessages=["do this to win"]
win=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Setting Window")
#TITLE_FONT= py.font.SysFont(name,size,bold=false, italic= false)
TITLE_FONT= py.font.SysFont('comicsans', 50, italic=True)
SUBTITLE_FONT= py.font.SysFont('comicsans', 30, italic=True)
xbox=25
wbox=25
square=py.Rect(10,10, wbox, xbox)

def display_message(message):
    py.time.delay(100)
    text=TITLE_FONT.render(message,30, BLACK )
    win.blit(text, (WIDTH/2-text.get_width()/2, 30) )
    py.display.update()
    py.time.delay(10)

def displaySub(subTitle,ysub):
    py.time.delay(100)
    text=SUBTITLE_FONT.render(subTitle,1, BLACK )
    win.blit(text, (10, ysub ))
    py.display.update()
    py.time.delay(10)

def display_back():
                x=660
                y=730
                square.x=x
                square.y=y
                for i in range(0,len(bmessages)):
                    word= bmessages[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    
                    
                    square.y=y

counter=1
def display_Menu():
    x=70
    y=190
    square.x=x
    square.y=y
    counter=1
    for i in range(0, len(messages)):
        word= messages[i]
        py.draw.rect(win, PURPLE, square)
        text=SUBTITLE_FONT.render(word,10, BLACK)
        win.blit(text, (x+wbox+10, y))
        py.display.flip()
        py.time.delay(100)
        y += 100
        square.y=y
        py.display.set_caption("Menu Window")

win.fill(WHITE)
display_message('Menu')
ysub=200
py.time.delay(200)
display_Menu()

run=True
counter=1
back=1
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
                win.fill(WHITE)
                display_message("Settings")
                py.display.set_caption("Setting Window")
                mouse_pos=py.mouse.get_pos()
                counter +=2
                
                x=70
                y=190
                square.x=x
                square.y=y
                for i in range(0, len(messages2)):
                    word= messages2[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
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
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    
                    
                    square.y=y            

            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>185 and mouse_pos[1]<=215 and counter==1:
                win.fill(WHITE)
                display_message('Instructions')
                py.display.set_caption("instructions window")
                x=70
                y=190
                square.x=x
                square.y=y
                
                for i in range(0, len(imessages)):
                    word= imessages[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
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
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    
                    
                    square.y=y

            
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>185 and mouse_pos[1]<=215 and counter==3:
                win.fill(WHITE)
                display_message('Screen Size')
                py.display.set_caption("Screen Size Window")
                x=70
                y=190
                square.x=x
                square.y=y
                for i in range(0, len(Ssmessages)):
                    word= Ssmessages[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    py.time.delay(100)
                    y += 100
                    square.y=y
                display_back()
                counter+=1
                back+=1


            if mouse_pos[0]>660 and mouse_pos[0]<=685 and mouse_pos[1]>730 and mouse_pos[1]<=755 and back==2:
                win.fill(WHITE)
                display_message('Menu')
                counter-=2
                back-=1
                display_Menu()




            if mouse_pos[0]>660 and mouse_pos[0]<=685 and mouse_pos[1]>730 and mouse_pos[1]<=755 and back==3:
                win.fill(WHITE)
                
                counter-=1
                back-=1
                win.fill(WHITE)
                display_message("Settings")
                py.display.set_caption("Setting Window")
                mouse_pos=py.mouse.get_pos()
                counter +=2
                back-=1
                x=70
                y=190
                square.x=x
                square.y=y
                for i in range(0, len(messages2)):
                    word= messages2[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
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
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    
                    
                    square.y=y    
                
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>190 and mouse_pos[1]<=215 and counter==4:
                WIDTH+=50
                HEIGHT+=50
                win=py.display.set_mode((WIDTH,HEIGHT))   
                display_back
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>290 and mouse_pos[1]<315 and counter==4:
                WIDTH-=50
                HEIGHT-=50
                win=py.display.set_mode((WIDTH,HEIGHT))   
                display_back
            
               
          
                    
                            
                                
            print(WIDTH)
            print(counter)
            print(back)

            
                
                
                
                
                
                
            # if py.Rect.collidepoint(square, mouse_pressed):
            #     win.fill
            # display_message("Start Game")
            # ysub=200
            # py.time.delay(300)
            # displaySub("Screen Size", ysub)
            # ysub+=125
            # displaySub("Background Colors", ysub)
            # py.time.delay(100)
            # ysub+=125
            # displaySub("Object color", ysub)
            # py.time.delay(100)
            # ysub+=125
            # displaySub("Sound On/Off", ysub)