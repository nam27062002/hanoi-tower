from operator import truediv
from turtle import distance
import pygame
pygame.init()
number = 3
scaleScreen = [900,500] # scale screen
scaleFloor = [scaleScreen[0]/3,100] # scale floor
scaleTubeY = 30
distanceTube = 35
scalePipe = [20,(number+1) * scaleTubeY ]
screen = pygame.display.set_mode((scaleScreen[0],scaleScreen[1])) # create screen
tube = [] # list tube
pygame.display.set_caption("Ha noi tower") # set caption
# value
running = True
white = (255,255,255)
#load images
floor = pygame.transform.scale(pygame.image.load("images/floor.png"),(scaleFloor[0],scaleFloor[1]))
pipe = pygame.transform.scale(pygame.image.load("images/pipe.png"),(scalePipe[0],scalePipe[1]))
for i in range(7): 
    tube.append(pygame.transform.scale(pygame.image.load(f"images/{i+1}.png"),(scaleFloor[0] - distanceTube*i,scaleTubeY)))
#FUNCTION
#draw graphics
def drawGraphics():
    screen.fill(white)
    xx = scalePipe[0]
    yy = (scaleScreen[0] - 3*xx)/6
    for i in range(3):
        screen.blit(floor,(300*i,scaleScreen[1] - scaleFloor[1]))
        screen.blit(pipe,(yy + 2*i*yy + i*xx,scaleScreen[1] - scaleFloor[1] - scalePipe[1]))
# check click
def checkClick(pos):
    for i in range(number):
        pass
# event
def event():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print()
def drawTube():
    for i in range(number):
        screen.blit(tube[i],(distanceTube* i/2,scaleScreen[1] - scaleFloor[1] - scaleTubeY*(i+1)))
while running:
    drawGraphics()
    drawTube()
    event()
    pygame.display.flip()
pygame.quit()
