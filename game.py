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
scaleArrow = [50,50]
arrow = []
posArrow = [[10,10],[60,10]]
speed = 20
AI = "off"
x = 0
y = 0
count = 0
stateMove = 'idle'
pygame.display.set_caption("Ha noi tower") # set caption
cursorHand = False
clock = pygame.time.Clock()
# value
running = True
white = (255,255,255)
#load images
floor = pygame.transform.scale(pygame.image.load("images/floor.png"),(scaleFloor[0],scaleFloor[1]))
pipe = pygame.transform.scale(pygame.image.load("images/pipe.png"),(scalePipe[0],scalePipe[1]))

arrow.append(pygame.transform.scale(pygame.image.load("images/arrow.png"),(scaleArrow[0],scaleArrow[1])))
arrow.append(pygame.transform.scale(pygame.image.load("images/arrowDown.png"),(scaleArrow[0],scaleArrow[1])))
# load font
font = pygame.font.SysFont('freesanbold.ttf', 50)
font1 = pygame.font.SysFont('freesanbold.ttf', 20)
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
    for i in range(2):
        screen.blit(arrow[i],(posArrow[i][0],posArrow[i][1]))
    screen.blit(font.render(str(number), True, (0, 255, 0)), (115,20))
    screen.blit(font1.render("Move min: "+str(pow(2,number) - 1), True, (255, 0, 0)), (150,30))
    screen.blit(font1.render("your move :"+str(count), True, (255, 0, 0)), (300,30))
# check click
def checkClick(pos):
    for i in range(3):
        if 300*i <= pos[0] < 300*(i+1) and pos[1] >= scaleScreen[1] - scaleFloor[1] - scalePipe[1]:
            return i
    return -1
# change cursor 
def changeCursor(pos):
    global cursorHand
    if pos[1] >= scaleScreen[1] - scaleFloor[1] - scalePipe[1]:
        cursorHand = True
    elif posArrow[0][0] <= pos[0] <= posArrow[0][0] + scaleArrow[0] and posArrow[0][1] <= pos[1] <= posArrow[0][1] + scaleArrow[1]:
        cursorHand = True
    elif posArrow[1][0] <= pos[0] <= posArrow[1][0] + scaleArrow[0] and posArrow[1][1] <= pos[1] <= posArrow[1][1] + scaleArrow[1]:
        cursorHand = True
    else:
        cursorHand = False
    if cursorHand:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
def checkTubeI(index):
    global boolPosTube,choiceIndex
    if A[index][number - 1] != -1:
        for i in A[index]:
            if i != -1:
                boolPosTube[number - 1 -i] = True
                choiceIndex = [index,number - 1 -i]
                break
def checkPut(index):
    if A[index][number - 1] == -1:
        return True
    else:
        for i in range(number):
            if A[index][i] != -1:
                if A[index][i] > number - 1 - choiceIndex[1]:
                    return True
                return False
def UpdateTube(pos):    
    global A
    for i in range(number - 1,-1,-1):
        if A[checkClick(pos)][i] == -1:
            posTube[choiceIndex[1]][0] = posPipe[checkClick(pos)][0] - ((scaletube[choiceIndex[1]][0] - scalePipe[0] )/2)
            posTube[choiceIndex[1]][1] = scaleScreen[1] - scaleFloor[1] - scaleTubeY*(number - i)
            for j in range(number):
                if A[choiceIndex[0]][j] != -1:
                    A[choiceIndex[0]][j] = -1
                    break
            A[checkClick(pos)][i] = number - 1 - choiceIndex[1]
            break
listMove = []
def HanoiTower(n,a,b,c):
    if n == 1:
        listMove.append([a,c])
    else:
        HanoiTower(n-1,a,c,b)
        listMove.append([a,c])
        HanoiTower(n-1, b, a, c)

# event
def event():
    global running, boolPosTube,A,number, AI
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            checkTubeI(checkClick(pygame.mouse.get_pos()))  
            if posArrow[0][0] <= pos[0] <= posArrow[0][0] + scaleArrow[0] and posArrow[0][1] <= pos[1] <= posArrow[0][1] + scaleArrow[1] and number != 7:
                number += 1
                loadAll()
            elif posArrow[1][0] <= pos[0] <= posArrow[1][0] + scaleArrow[0] and posArrow[1][1] <= pos[1] <= posArrow[1][1] + scaleArrow[1] and number != 3:
                number -= 1
                loadAll()
        elif event.type == pygame.MOUSEBUTTONUP:
            count = 0
            for i in boolPosTube:
                if i == True:
                    count = 1
            if count != 0:
                if (choiceIndex[0] == checkClick(pos) or checkClick(pos) == -1 ) or checkPut(checkClick(pos)) == False: 
                    pass
                else:
                    if AI == "off":
                        UpdateTube(pos)
                boolPosTube[choiceIndex[1]] = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                AI = "on"
            if event.key == pygame.K_b:
                print(boolPosTube)
def setPosTube():
    global posTube,boolPosTube
    boolPosTube.clear()
    posTube.clear()
    for i in range(number):
        posTube.append([distanceTube* i/2,scaleScreen[1] - scaleFloor[1] - scaleTubeY*(i+1)])
        boolPosTube.append(False)
def drawTube():
    for i in range(number):
        if boolPosTube[i] == False:
            screen.blit(tube[i],(posTube[i][0],posTube[i][1]))
        elif AI == "off":
            screen.blit(tube[i],(pygame.mouse.get_pos()[0] - tube[i].get_width()/2,pygame.mouse.get_pos()[1] - tube[i].get_height()/2))
        else:
            screen.blit(tube[i],(posTube[i][0],posTube[i][1]))
def loadA():
    global A
    A.clear()
    for i in range(3):
        A.append([])
        for j in range(number):
            if (i == 0):
                A[i].append(j)
            else:
                A[i].append(-1)  
def loadPosPipe():
    global posPipe
    posPipe.clear()
    xx = scalePipe[0]
    yy = (scaleScreen[0] - 3*xx)/6
    for i in range(3):
        posPipe.append([yy + 2*i*yy + i*xx,scaleScreen[1] - scaleFloor[1] - scalePipe[1]])
def loadAll():
    global scalePipe,pipe,listMove,x,y,stateMove,AI,boolPosTube,count
    loadA()
    setPosTube()
    scalePipe.clear()
    scalePipe = [20,(number+1) * scaleTubeY ]
    pipe = pygame.transform.scale(pygame.image.load("images/pipe.png"),(scalePipe[0],scalePipe[1]))
    loadPosPipe()
    listMove.clear()
    HanoiTower(number,0,1,2)
    x = listMove[0][0]
    y = listMove[0][1]
    stateMove = 'idle'
    AI = 'off'
    count = 0
loadAll()
def moveTube(start,end):
    global AI
    checkTubeI(start)
    AI = "moving"
def moveAI(start,end):
    global stateMove,AI,x,y,count
    if count < len(listMove):
        if stateMove == "idle":
            stateMove = 'move up'
        if stateMove == 'move up':
            if posTube[choiceIndex[1]][1] > scaleScreen[1] - scaleFloor[1] - scalePipe[1] - 100:
                posTube[choiceIndex[1]][1] -= speed
            else:
                posTube[choiceIndex[1]][1] = scaleScreen[1] - scaleFloor[1] - scalePipe[1] - 100
                stateMove = 'move x'
        elif stateMove == 'move x':
            if start > end:
                if posTube[choiceIndex[1]][0] > posPipe[end][0] - ((scaletube[choiceIndex[1]][0] - scalePipe[0] )/2):
                    posTube[choiceIndex[1]][0] -= speed
                else:
                    posTube[choiceIndex[1]][0] = posPipe[end][0] - ((scaletube[choiceIndex[1]][0] - scalePipe[0] )/2)
                    stateMove = 'move down'
            else:
                if posTube[choiceIndex[1]][0] < posPipe[end][0] - ((scaletube[choiceIndex[1]][0] - scalePipe[0] )/2):
                    posTube[choiceIndex[1]][0] += speed
                else:
                    posTube[choiceIndex[1]][0] = posPipe[end][0] - ((scaletube[choiceIndex[1]][0] - scalePipe[0] )/2)
                    stateMove = 'move down'
        elif stateMove == 'move down':
            for i in range(number - 1,-1,-1):
                if A[end][i] == -1:
                    if posTube[choiceIndex[1]][1] < scaleScreen[1] - scaleFloor[1] - scaleTubeY*(number - i):
                        posTube[choiceIndex[1]][1] += speed
                    else:
                        posTube[choiceIndex[1]][1] = scaleScreen[1] - scaleFloor[1] - scaleTubeY*(number - i)
                        stateMove = 'update A'
                    break
        else:
            for i in range(number - 1,-1,-1):
                if A[end][i] == -1:
                    for j in range(number):
                        if A[choiceIndex[0]][j] != -1:
                            A[choiceIndex[0]][j] = -1
                            break
                    A[end][i] = number - 1 - choiceIndex[1]
                    stateMove = 'idle'
                    AI = 'on'
                    if count < len(listMove) - 1:
                        count += 1
                        x = listMove[count][0]
                        y = listMove[count][1]
                    else:
                        AI = 'idle'
                    break
while running:
    drawGraphics()
    drawTube()
    event()
    if AI == 'on':
        moveTube(x,y)
    elif AI == 'moving':
        moveAI(x,y)
    changeCursor(pygame.mouse.get_pos())
    pygame.display.flip()
    clock.tick(100)
pygame.quit()
 