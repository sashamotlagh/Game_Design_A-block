import pygame
class button():
    def init(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    def isOver(self, position):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if position[0] > 70 and position[0] < self.x + self.width:
            if position[1] > self.y and position[1] < self.y + self.height:
                return True
            
        return False
def redrawwindow():
    window.fill((255,255,255))
    button.draw(window)
run=True
while run:
    redrawwindow()
    pygame.display.update()
    for i in pygame.event.get():
        position=pygame.mouse.get_pos()
        if i.type==pygame.quit():
            run=False
            pygame.quit()
            quit()
        if i.type==pygame.MOUSEBUTTONDOWN:
            if button.isOver(position):
                print("you clicked the button")
        if i.type==pygame.MOUSEMOTION:
            if button.isOver(position):
                button.color = (255,0,0)
            else:
                button.color(0,255,0)
