from operator import truediv
from tabnanny import check
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
posTube = []
boolPosTube = []
choiceIndex = [-1,-1]
A = []  
posPipe = []
scaletube = []
pygame.display.set_caption("Ha noi tower") # set caption
# value
running = True
white = (255,255,255)
#load images
floor = pygame.transform.scale(pygame.image.load("images/floor.png"),(scaleFloor[0],scaleFloor[1]))
pipe = pygame.transform.scale(pygame.image.load("images/pipe.png"),(scalePipe[0],scalePipe[1]))
for i in range(7): 
    scaletube.append([scaleFloor[0] - distanceTube*i,scaleTubeY])
    tube.append(pygame.transform.scale(pygame.image.load(f"images/{i+1}.png"),(scaletube[i][0],scaletube[i][1])))
#FUNCTION
#draw graphics
def drawGraphics():
    screen.fill(white)
    for i in range(3):
        screen.blit(floor,(300*i,scaleScreen[1] - scaleFloor[1]))
        screen.blit(pipe,(posPipe[i][0],posPipe[i][1]))
# check click
def checkClick(pos):
    for i in range(3):
        if 300*i <= pos[0] < 300*(i+1) and pos[1] >= scaleScreen[1] - scaleFloor[1] - scalePipe[1]:
            return i
    return -1
# 
def checkTubeI(index):
    global boolPosTube,choiceIndex
    if A[index][number - 1] != -1:
        for i in A[index]:
            if i != -1:
                boolPosTube[number - 1 -i] = True
                choiceIndex = [index,number - 1 -i]
                break
# event
def event():
    global running, boolPosTube,A
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            checkTubeI(checkClick(pygame.mouse.get_pos()))  
        elif event.type == pygame.MOUSEBUTTONUP:
            count = 0
            for i in boolPosTube:
                if i == True:
                    count = 1
            if count != 0:
                if choiceIndex[0] == checkClick(pygame.mouse.get_pos()) or checkClick(pygame.mouse.get_pos()) == -1: 
                    pass
                else:
                    for i in range(number - 1,-1,-1):
                        if A[checkClick(pygame.mouse.get_pos())][i] == -1:
                            posTube[choiceIndex[1]][0] = posPipe[checkClick(pygame.mouse.get_pos())][0] - ((scaletube[choiceIndex[1]][0] - scalePipe[0] )/2)
                            posTube[choiceIndex[1]][1] = scaleScreen[1] - scaleFloor[1] - scaleTubeY*(number - i)
                            for j in range(number):
                                if A[choiceIndex[0]][j] != -1:
                                    A[choiceIndex[0]][j] = -1
                                    break
                            A[checkClick(pygame.mouse.get_pos())][i] = number - 1 - choiceIndex[1]
                            break
                boolPosTube[choiceIndex[1]] = False    
def setPosTube():
    global posTube
    for i in range(number):
        posTube.append([distanceTube* i/2,scaleScreen[1] - scaleFloor[1] - scaleTubeY*(i+1)])
        boolPosTube.append(False)
def drawTube():
    for i in range(number):
        if boolPosTube[i] == False:
            screen.blit(tube[i],(posTube[i][0],posTube[i][1]))
        else:
            screen.blit(tube[i],(pygame.mouse.get_pos()[0] - tube[i].get_width()/2,pygame.mouse.get_pos()[1] - tube[i].get_height()/2))
def loadA():
    global A
    for i in range(3):
        A.append([])
        for j in range(number):
            if (i == 0):
                A[i].append(j)
            else:
                A[i].append(-1)  
def loadPosPipe():
    global posPipe
    xx = scalePipe[0]
    yy = (scaleScreen[0] - 3*xx)/6
    for i in range(3):
        posPipe.append([yy + 2*i*yy + i*xx,scaleScreen[1] - scaleFloor[1] - scalePipe[1]])
# call function
loadA()
setPosTube()
loadPosPipe()
while running:
    drawGraphics()
    drawTube()
    event()
    pygame.display.flip()
pygame.quit()
 