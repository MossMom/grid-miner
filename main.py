import pygame
import random

from fun import *
from var import *

pygame.init()

while True: #GAME LOOP
#setup
    random.seed()
    clock.tick(fps)
    tick += 1
    if tick >= fps:
        tick = 0
        count += 1
    
#input/output section
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and timer1 == 0: #roll dice1 with A
        dice1 = roll1(dice1, diceMax)
        timer1 = fps//2
        
    if keys[pygame.K_s] and timer1 == 0: #roll dice2 with S
        dice2 = roll2(dice2, diceMax)
        timer1 = fps//2
    
    if keys[pygame.K_w] and timer1 == 0: #roll dice2 with S
        dice1 = roll1(dice1, diceMax)
        dice2 = roll2(dice2, diceMax)
        timer1 = fps//2
    
    if keys[pygame.K_d] and timer1 == 0: #show both dice values with D
        showRolls(dice1, dice2)
        if rollDone == True:
            rollDone = False
        else:
            rollDone = True
        timer1 = fps//2
    
    if keys[pygame.K_q] and timer1 == 0: #spawn new icons
        temp1 = 0
        timer1 = fps//2
        dice1 = 1
        dice2 = 1
        
    if keys[pygame.K_MINUS] and timer1 == 0: #increase player variables
        dicelvl += 1
        picklvl += 1
        coin += 1
        mushrooms += 1
        copper += 1
        iron += 1
        gold += 1
        timer1 = fps//2
    
    if keys[pygame.K_EQUALS] and timer1 == 0: #decrease player variables
        dicelvl -= 1
        picklvl -= 1
        coin -= 1
        mushrooms -= 1
        copper -= 1
        iron -= 1
        gold -= 1
        timer1 = fps//2
    
    
    if timer1 > 0:
        timer1 -= 1
    
#render section
    screen.fill((53, 38, 28))
    
    if temp1 == 0:
        spawnMineSprites()
        print("(re)spawned sprites")
        temp1 = 1
    
    callFunctions() #calls all "draw" functions
    drawNumbers()

    if rollDone == True:
        assignSpots(dice1, dice2)
                
    pygame.display.flip() 