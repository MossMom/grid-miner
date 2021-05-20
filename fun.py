import pygame
import random

from var import *

def roll1(dice, maximum): #roll dice 1
    dice = random.randint(1, maximum)
    print("On a", maximum, "sided dice, you rolled a", dice)
    return dice

def roll2(dice, maximum): #roll dice 2
    dice = random.randint(1, maximum)
    print("On a", maximum, "sided dice, you rolled a", dice)
    return dice
    
def showRolls(a, b): #display dice values
    print("Your rolls are   ", a, ",", b, "   and   ", b, ",", a)

def callFunctions():
    drawMineBG() 
    drawMineSprites() 
    drawDiceIcons1() 
    drawInventory()
    drawNumbers()

def drawMineBG(): #draws the grid background
    pygame.draw.rect(screen, (61, 45, 31), (400, 0, 800, 800)) #area will hold dice icons
    pygame.draw.rect(screen, (62, 48, 34), (500, 100, 700, 700)) #area holds grid map
    for i in range(0,6,1): # Rows (height)
        for j in range (0,6,1): # Columns (width)
            if MineMapBG[i][j]==0: 
                pygame.draw.rect(screen, (50, 50, 50), (j*100+550, i*100+150, 100, 100))
                screen.blit(framesPic, (j*100+550, i*100+150), (0, 0, 100, 100))
            if MineMapBG[i][j]==1:
                pygame.draw.rect(screen, (80, 80, 80), (j*100+550, i*100+150, 100, 100))
                screen.blit(framesPic, (j*100+550, i*100+150), (100, 0, 100, 100))
            if MineMapBG[i][j]==2:
                pygame.draw.rect(screen, (110, 110, 110), (j*100+550, i*100+150, 100, 100))
                screen.blit(framesPic, (j*100+550, i*100+150), (200, 0, 100, 100))
            if MineMapBG[i][j]==3:
                pygame.draw.rect(screen, (140, 140, 140), (j*100+550, i*100+150, 100, 100))
                screen.blit(framesPic, (j*100+550, i*100+150), (300, 0, 100, 100))
            if MineMapBG[i][j]==4:
                pygame.draw.rect(screen, (170, 170, 170), (j*100+550, i*100+150, 100, 100))
                screen.blit(framesPic, (j*100+550, i*100+150), (400, 0, 100, 100))
    screen.blit(sidebarPic, (0, 0), (0, 0, 400, 800))
                
def spawnMineSprites(): #resets grid, then spawns new icons on the grid
    for i in range(0,6,1): # Rows (height)
        for j in range (0,6,1): # Columns (width)
            MineMap1[i][j] = 0
            
    for i in range(1, 6): #spawn 5 bats
        MineMap1[random.randint(0, 5)][random.randint(0, 5)] = 2
        
    for i in range(1, random.randint(8, 12)): #spawn 6-14 ore (can overwrite bats)
        MineMap1[random.randint(0, 5)][random.randint(0, 5)] = 1
    
    for i in range(1, random.randint(2, 3)): #spawn 1-2 mushrooms (can overwrite bats and ore)
        MineMap1[random.randint(0, 5)][random.randint(0, 5)] = 5
        
    for i in range(1, random.randint(1, 3)): #spawn 0-2 shops (can overwrite bats and ore and mushrooms)
        MineMap1[random.randint(0, 5)][random.randint(0, 5)] = 3
    
    for i in range(1, 3): #spawn 2 stairs (can overwrite anything)
        MineMap1[random.randint(0, 5)][random.randint(0, 5)] = 4
    
    MineMap1[0][0] = 0 # make sure [1, 1] is empty (can overwrite anything)
    
def drawMineSprites():
    for i in range(0,6,1): # Rows (height)
        for j in range (0,6,1): # Columns (width)
            if MineMap1[i][j]==0: #empty
                screen.blit(spriteSheet, (j*100+573, i*100+172), (54*4, 57*4, 54, 57))
            if MineMap1[i][j]==1: #ore
                if level <= 3:
                    screen.blit(spriteSheet, (j*100+573, i*100+172), (54*4, 57*0, 54, 57)) #copper
                elif level <= 6:
                    screen.blit(spriteSheet, (j*100+573, i*100+172), (54*0, 57*1, 54, 57)) #iron
                elif level <= 9:
                    screen.blit(spriteSheet, (j*100+573, i*100+172), (54*1, 57*1, 54, 57)) #gold
            if MineMap1[i][j]==2: #bat
                screen.blit(spriteSheet, (j*100+573, i*100+172), (54*3, 57*1, 54, 57))
            if MineMap1[i][j]==3: #shop
                screen.blit(spriteSheet, (j*100+573, i*100+172), (54*2, 57*2, 54, 57))
            if MineMap1[i][j]==4: #stairs
                screen.blit(spriteSheet, (j*100+573, i*100+172), (54*3, 57*2, 54, 57))
            if MineMap1[i][j]==5: #mushrooms
                screen.blit(spriteSheet, (j*100+573, i*100+172), (54*2, 57*1, 54, 57))

def drawDiceIcons1():
    screen.blit(spriteSheet, (575, 25), (54*3, 57*3, 54, 57)) #1 top
    screen.blit(spriteSheet, (425, 175), (54*3, 57*3, 54, 57)) #1 side
    screen.blit(spriteSheet, (675, 25), (54*4, 57*3, 54, 57)) #2 top
    screen.blit(spriteSheet, (425, 275), (54*4, 57*3, 54, 57)) #2 side
    screen.blit(spriteSheet, (775, 25), (54*0, 57*4, 54, 57)) #3 top
    screen.blit(spriteSheet, (425, 375), (54*0, 57*4, 54, 57)) #3 side
    screen.blit(spriteSheet, (875, 25), (54*1, 57*4, 54, 57)) #4 top
    screen.blit(spriteSheet, (425, 475), (54*1, 57*4, 54, 57)) #4 side
    screen.blit(spriteSheet, (975, 25), (54*2, 57*4, 54, 57)) #5 top
    screen.blit(spriteSheet, (425, 575), (54*2, 57*4, 54, 57)) #5 side
    screen.blit(spriteSheet, (1075, 25), (54*3, 57*4, 54, 57)) #6 top
    screen.blit(spriteSheet, (425, 675), (54*3, 57*4, 54, 57)) #6 side

def drawInventory():
    for i in range(0,3,1):
        screen.blit(spriteSheetScaled, (65+(i*50*2), 50), (72*0, 76*2, 72, 76)) #empty health
    for i in range(0,health,1):
        screen.blit(spriteSheetScaled, (65+(i*50*2), 50), (72*4, 76*1, 72, 76)) #full health
    if picklvl == 0:
        screen.blit(spriteSheet2x, (70, 182), (54*0*2, 57*0*2, 54*2, 57*2)) #regular pick
    elif picklvl == 1:
        screen.blit(spriteSheet2x, (70, 182), (54*1*2, 57*0*2, 54*2, 57*2)) #copper pick
    elif picklvl == 2:
        screen.blit(spriteSheet2x, (70, 182), (54*2*2, 57*0*2, 54*2, 57*2)) #iron pick
    elif picklvl == 3:
        screen.blit(spriteSheet2x, (70, 182), (54*3*2, 57*3*2, 54*2, 57*2)) #gold pick
    if dicelvl == 0:
        screen.blit(spriteSheet2x, (220, 182), (54*4*2, 57*2*2, 54*2, 57*2)) #regular dice
    elif dicelvl == 1:
        screen.blit(spriteSheet2x, (220, 182), (54*0*2, 57*3*2, 54*2, 57*2)) #copper dice
    elif dicelvl == 2:
        screen.blit(spriteSheet2x, (220, 182), (54*1*2, 57*3*2, 54*2, 57*2)) #iron dice
    elif dicelvl == 3:
        screen.blit(spriteSheet2x, (220, 182), (54*2*2, 57*3*2, 54*2, 57*2)) #gold dice
    screen.blit(spriteSheetScaled, (50, 360), (72*1, 76*2, 72, 76)) #coin
    screen.blit(spriteSheetScaled, (160, 360), (72*2, 76*1, 72, 76)) #mushroom
    screen.blit(spriteSheetScaled, (270, 360), (72*4, 76*0, 72, 76)) #copper ore
    screen.blit(spriteSheetScaled, (50, 480), (72*0, 76*1, 72, 76)) #iron ore
    screen.blit(spriteSheetScaled, (160, 480), (72*1, 76*1, 72, 76)) #gold ore

def drawNumbers():
    screen.blit(numbersPic, (50+60, 360+60), (20*coin, 0, 20, 28)) #coin number
    screen.blit(numbersPic, (160+60, 360+60), (20*mushrooms, 0, 20, 28)) #mushroom number
    screen.blit(numbersPic, (270+60, 360+60), (20*copper, 0, 20, 28)) #copper number
    screen.blit(numbersPic, (50+60, 480+60), (20*iron, 0, 20, 28)) #iron number
    screen.blit(numbersPic, (160+60, 480+60), (20*gold, 0, 20, 28)) #gold number
    
def assignSpots(a, b):
    pygame.draw.rect(screen, ((0, 200, 0)), ((a-1)*100+551, (b-1)*100+151, 100, 100), 3)
    pygame.draw.rect(screen, ((0, 200, 0)), ((b-1)*100+551, (a-1)*100+151, 100, 100), 3)