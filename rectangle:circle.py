#Sasha motlagh
# rectangle and circle drawing

import random,os 
import pygame

pygame.init()
check=Trueheight=600
width=700
colors = {'black':(0,0,0),'red':(255,0,0),'green':(0,255,0)}
while check:
    try:
        height=int(height)
        width=int(width)
        check=False
    except:
        valueError= 