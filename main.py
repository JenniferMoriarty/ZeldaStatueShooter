import pygame
from pygame.math import Vector2

pygame.init()  
pygame.display.set_caption("statue shooter")  
screen = pygame.display.set_mode((800, 800))  
screen.fill((0,0,0))
clock = pygame.time.Clock() 
gameover = False 

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed

#timer for launching projectile:
timer = 0

#---------projectile class---------------------------------------------------------
class projectile():
    def __init__(self):
        
        self.pos = Vector2(200,500)
        self.isAlive = False
        self.speed = 10 
  
    def draw(self):
        pygame.draw.circle(screen, (200, 200, 0), (self.pos[0], self.pos[1]), 10)

    def move(self):
        self.isAlive = True

    def update(self, start, end):
        
        #bounds check: reset if you cross the edge of the game screen
        if self.pos[0] < 0 or self.pos[0] > 800 or self.pos[1] < 0 or self.pos[1] > 800:
            self.isAlive = False
            self.pos = (200, 500)
        
        self.direction = Vector2(end) - Vector2(start) #i want to write this out to show the math
        
        #to normalize a vector means to strip the magnitude and only look at the length
        if self.isAlive:
            self.pos += self.direction.normalize() * self.speed #This too- let's show the math
            
#---------end projectile class---------------------------------------------------------

p1 = projectile()


while not gameover:
    clock.tick(60) 
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True
            elif event.key == pygame.K_DOWN:
                keys[DOWN]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
            elif event.key == pygame.K_DOWN:
                keys[DOWN]=False
          

    if keys[LEFT]==True:
        vx=-5   
    elif keys[RIGHT] == True:
        vx = 5
    else:
        vx = 0
        
    if keys[UP]==True:
        vy=-5   
    elif keys[DOWN] == True:
        vy = 5
    else:
        vy = 0
  
    timer+=1
    if timer > 100:
        p1.move()
        timer = 0
        print("shoot")

        
    xpos+=vx 
    ypos+=vy
    p1.update((200, 500), (xpos, ypos))

    # RENDER--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) 

    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 30, 30)) #player
    
    pygame.draw.rect(screen, (100,100,100), (200, 500, 50,50)) #statue
    
    p1.draw()

    
    pygame.display.flip()
    
