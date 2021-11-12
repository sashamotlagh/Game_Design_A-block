# Mouse position
# drawing rect
# moving object
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
import os
import pygame as py
 

#first thing
py.init()
WIDTH=800
HEIGHT=800
walkRight = [py.image.load('game images/Pygame-Tutorials-master/Game/R1.png'), py.image.load('game images/Pygame-Tutorials-master/Game/R2.png'), py.image.load('game images/Pygame-Tutorials-master/Game/R3.png'), py.image.load('game images/Pygame-Tutorials-master/Game/R4.png'), py.image.load('game images/Pygame-Tutorials-master/Game/R5.png'), py.image.load('game images/Pygame-Tutorials-master/Game/R6.png'), py.image.load('game images/Pygame-Tutorials-master/Game/R7.png'), py.image.load('game images/Pygame-Tutorials-master/Game/R8.png'), py.image.load('game images/Pygame-Tutorials-master/Game/R9.png')]
walkLeft = [py.image.load('game images/Pygame-Tutorials-master/Game/L1.png'), py.image.load('game images/Pygame-Tutorials-master/Game/L2.png'), py.image.load('game images/Pygame-Tutorials-master/Game/L3.png'), py.image.load('game images/Pygame-Tutorials-master/Game/L4.png'), py.image.load('game images/Pygame-Tutorials-master/Game/L5.png'), py.image.load('game images/Pygame-Tutorials-master/Game/L6.png'), py.image.load('game images/Pygame-Tutorials-master/Game/L7.png'), py.image.load('game images/Pygame-Tutorials-master/Game/L8.png'), py.image.load('game images/Pygame-Tutorials-master/Game/L9.png')]
bg = py.image.load('game images/bgSmaller.jpg')
char = py.image.load('game images/Pygame-Tutorials-master/Game/standing.png')
clock= py.time.Clock()
x=50
y=400
vel = 5
w = 40
h = 60
boulder=py.Rect(WIDTH-300,HEIGHT-200, 100,200)
#create window
height= 800
width = 800
colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150, 0, 150), 'white':(255,255,255), 'black':(0,0,0) }
screen=py.display.set_mode((800, 800))
myColor= colors.get('white')
screen.fill(myColor)
py.display.set_caption("Moving Man")
py.display.flip()
#parameters to define our square
x=width/2
y=height/2
wbox=50
hbox=50
#creating out object square
#draw object
objColor=colors.get('red')
boulderColor=colors.get('blue')
py.display.update()
#create speed to move the object on the screen,
speed = 10
run=True #Variable to control the main loop
#boolean to check for jump
Jumping=False
jumpCount=10
move=True
while run:
    py.time.delay(100) #milliseconds
    for anyThing in py.event.get():
        if anyThing.type == py.QUIT:
            run =False
    keyPressed= py.key.get_pressed()
   
    if keyPressed[py.K_RIGHT] and square.x <WIDTH-wbox-speed:
        if char.colliderect(boulder):
            char.x -= 10
        else:
            char.x += speed
    if keyPressed[py.K_LEFT] and char.x>speed-5:
        if char.colliderect(boulder):
            char.x=char.x+10
        else:
            char.x -= speed
    if not(Jumping):
        if keyPressed[py.K_DOWN] and char.y <HEIGHT-hbox-speed:
            if char.colliderect(boulder):
                char.y -=10
            else:
                char.y += speed
        if keyPressed[py.K_UP] and char.y>speed-5:
            char.y -= speed
        if keyPressed[py.K_SPACE]:
            Jumping=True
    else:
        if jumpCount >=-10:
            if not char.colliderect(boulder):
                char.y -= jumpCount* abs(jumpCount)*0.5
                jumpCount -=1
        else:
            jumpCount =10
            Jumping=False
 
    # if(py.Rect.collidepoint(boulder, (square.x+wbox/2,square.y))):    
    #     move=False
    #     square.x=square.x-wbox
    #     move=True
    # if  
    screen.fill(myColor)
    py.draw.rect(screen,boulderColor,boulder)
    py.display.flip()
py.quit()