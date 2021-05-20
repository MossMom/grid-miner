import pygame
import numpy as np

screenWidth = 1200
screenHeight = 800
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Grid Mining')
clock = pygame.time.Clock()

framesPic = pygame.image.load('pics/frames.png')
spriteSheet = pygame.image.load('pics/sprites.png')
spriteSheet2x = pygame.image.load('pics/sprites.png')
spriteSheet2x = pygame.transform.scale(spriteSheet2x, (540, 570))
spriteSheetScaled = pygame.image.load('pics/scaled sprites.png')
sidebarPic = pygame.image.load('pics/sidebar.png')
numbersPic = pygame.image.load('pics/numbers.png')
numbersPic = pygame.transform.scale(numbersPic, (200, 28))
fps = 60
tick = 0
count = 0
timer1 = 0
temp1 = 0

#lists
templist = list() #temp list
temparray = np.array([1, 2, 3, 4, 5, 6]) #temp array

#mine maps
MineMapBG = np.random.randint(5, size=(6, 6))
MineMap1 = np.random.randint(1, size=(6, 6))

#dice stuff
diceMax = 6 #max number possible to roll on dice, random.randint(1, diceMax)
dice1 = 1 #current dice1 value
dice2 = 1 #current dice2 value
spot1 = 0, 0
spot2 = 0, 0
rollDone = False

#player variables
health = 3
dicelvl = 0
picklvl = 0
coin = 2
mushrooms = 0
copper = 0
iron = 0
gold = 0
level = 1