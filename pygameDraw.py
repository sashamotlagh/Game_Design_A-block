#sasha motlagh 10/21/21
#learning display, opening windows, changing size window, basic game loop
import pygame as py, os
from pygame.draw import circle 
import pygame, random
os.system('clear')
#first thing to do is initialize pygame
pygame.init()
check=True
height=800
width=800
colors = {'black':(0,0,0),'red':(255,0,0), 'blue':(0,0,255), 'white':(255,255,255), 'green':(0,255,0), 'purple':(150,0,150), 'yellow':(0,150,150)}
colorNames=['black', 'red', 'blue', 'white', 'green', 'purple', 'yellow']
randColor = random.choice(colorNames)
while check:
    height= input("height of your window: (100-1000) ")
    width= input("width of your window: (10-1000) ")
    colorNames=['black', 'red', 'blue', 'white', 'green', 'purple', 'yellow', 'somecolor']
    randColor = random.choice(colorNames)

    try:
        height = int(height)
        width= int(width)
        check = False
    except ValueError:
        print('Try again')
        check = True

color = colors.get(str(randColor))
window=pygame.display.set_mode((height,width))
window.fill(color)
pygame.display.flip()

pygame.display.set_caption("Game Window")
pygame.display.flip()
x=width/2
y=height/2
hbox=50
wbox=50
speed= 10
xc= 15
yc= 20
radius=hbox/2
rect=pygame.Rect(width/2, height/2, wbox, hbox)
pygame.draw.rect(window, colors.get('purple'), rect)
pygame.draw.circle(window, colors.get('white'), (xc,yc), radius)
pygame.display.flip()
run=True

#main loop
while run:
    pygame.time.delay(10)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run= False
    #x,y=pygame.mouse.get_pos()
    #print("(" + str(x)+ " , "+ str(y)+ ")")
    keyPressed= pygame.key.get_pressed()
    if keyPressed[pygame.K_UP]:
        if rect.y < 0:
            rect.y=height
        else:
            rect.y -= speed
    if keyPressed[pygame.K_DOWN]:
        if rect.y == 0:
            rect.y=height
        else:
            rect.y +=speed
    if keyPressed[pygame.K_LEFT]:
        if rect.x < 0:
            rect.x=width
        else:
            rect.x -= speed
    if keyPressed[pygame.K_RIGHT]:
        if rect.x == 0:
            rect.x= width
        else:
            rect.x += speed
    if keyPressed[pygame.K_w]:
        yc-= speed
    if keyPressed[pygame.K_s]:
        yc +=speed
    if keyPressed[pygame.K_a]:
        xc -= speed
    if keyPressed[pygame.K_d]:
        xc += speed
    window.fill(color)
    pygame.display.flip()
    pygame.draw.rect(window, colors.get('purple'), rect)
    pygame.draw.circle(window, colors.get('white'), (xc,yc), radius)
    pygame.display.flip()

    point =(xc, yc)   
    collide=rect.collidepoint(point)

    if collide:
        rcircle=rcircle+(hbox/6)
        x=random.randrange(0,width)
        y=random.randrange(0,height)
        rect=pygame.Rect(x,y,wbox,hbox)
    pygame.draw.rect(window, colors.get('purple'), rect)
    pygame.draw.circle(window, colors.get('blue'), (xc,yc), circle)
    pygame.display.flip()
pygame.quit()