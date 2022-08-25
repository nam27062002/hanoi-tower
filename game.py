from operator import truediv
import pygame
pygame.init()
number = 3
scaleScreen = [900,500] # scale screen
scaleFloor = [scaleScreen[0]/3,100] # scale floor
scaleTubeY = 30
scalePipe = [20,number * scaleTubeY]
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
    tube.append(pygame.transform.scale(pygame.image.load(f"images/{i+1}.png"),(300,scaleTubeY)))
#FUNCTION
#draw graphics
def drawGraphics():
    screen.fill(white)
    xx = scalePipe[0]
    yy = (scaleScreen[0] - 3*xx)/6
    for i in range(3):
        screen.blit(floor,(300*i,scaleScreen[1] - scaleFloor[1]))
        screen.blit(pipe,(yy + 2*i*yy + i*xx,scaleScreen[1] - scaleFloor[1] - scalePipe[1]))
# event
def event():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
def drawTube():
    screen.blit(tube[0],(0,0))
while running:
    drawGraphics()
    drawTube()
    event()
    pygame.display.flip()
pygame.quit()
