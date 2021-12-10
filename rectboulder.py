#sasha motlagh
#11/9/21
#9 going right
#9 going left
#1 standing
import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
walkRight = [pygame.image.load('game images/Pygame-Tutorials-master/Game/R1.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/R2.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/R3.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/R4.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/R5.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/R6.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/R7.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/R8.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/R9.png')]
walkLeft = [pygame.image.load('game images/Pygame-Tutorials-master/Game/L1.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/L2.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/L3.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/L4.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/L5.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/L6.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/L7.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/L8.png'), pygame.image.load('game images/Pygame-Tutorials-master/Game/L9.png')]
bg = pygame.image.load('game images/bgSmaller.jpg')
char = pygame.image.load('game images/Pygame-Tutorials-master/Game/standing.png')
colors = {'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,145), 'white':(255,255,255), 'purple':(150,0,150), 'orange':(255, 165, 0)}
white= [255,255,255]
red= [255,0,0]
blue= [0,0,255]
spd=5
isJump = False
jumpCount = 5
left = False
right = False
walkCount = 0
clock= pygame.time.Clock()
x=50 #50
y=400 #400
vel = 5
width = 40
height = 60
OsX = [129,194,236,300,391]
BrX = 50
BrX2 = OsX[0]
PlY = 356-height
PlY2 = 254-height

def redrawGameWindow():
    global walkCount
    screen.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:  
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        screen.blit(char, (x, y))
        walkCount = 0
    pygame.display.update() 
pygame.display.set_caption('MY SHAPES')
screen.blit(bg, (0,0))
pygame.display.flip()
pygame.time.delay(1000)
print(pygame.mouse.get_pos)
count = 0
count1 = 1
count2 = 2
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
    else: 
        left = False
        right = False
        walkCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.25
            jumpCount -= 1
            if x>OsX[count] and y >= PlY:
                isJump = False
                jumpCount = 10
                BorX = OsX[count1]
                BorX2 = OsX[count2]
                count+=1
                count1+=1
                count2+=1
                PlY = PlY2
        else: 
            jumpCount = 10
            isJump = False
    redrawGameWindow() 
pygame.quit()