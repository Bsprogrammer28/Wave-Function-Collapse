from numpy import tile
from pandas import options
import pygame
from random import randint, choice
pygame.init()

DIM = 2
height = DIM*2*100
width = DIM*2*100
white = (255, 255, 255)
black = (0, 0, 0)
tiles = []
grid = []

BLANK = 0
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

rules = [
    [
        [BLANK, UP],
        [BLANK, RIGHT],
        [BLANK, DOWN],
        [BLANK, LEFT],
    ],
    [
        [RIGHT, LEFT, DOWN],
        [LEFT, UP, DOWN],
        [BLANK, DOWN],
        [RIGHT, DOWN, UP],
    ],
    [
        [RIGHT, LEFT, DOWN],
        [LEFT, DOWN, UP],
        [UP, RIGHT, LEFT],
        [BLANK, LEFT],
    ],
    [
        [BLANK, UP],
        [LEFT, UP, DOWN],
        [RIGHT, LEFT, UP],
        [RIGHT, UP, DOWN],
    ],
    [
        [RIGHT, LEFT, DOWN],
        [BLANK, RIGHT],
        [RIGHT, LEFT, UP],
        [RIGHT, UP, DOWN],
    ],
]

for i in range(DIM*DIM):
    grid.append({
        "Collapsed": False,
        "Options": [BLANK, UP, RIGHT, DOWN, LEFT]
    })

def spawnImage(img, x, y):
    screen.blit(img, (x, y))


path = "E:/Work/Programming/Learning New Things/Wave Function Collapse/inPython/"

tiles.append(pygame.image.load(f'{path}blank.png'))
tiles.append(pygame.image.load(f'{path}up.png'))
tiles.append(pygame.image.load(f'{path}right.png'))
tiles.append(pygame.image.load(f'{path}down.png'))
tiles.append(pygame.image.load(f'{path}left.png'))

seed = {
    "image": randint(0, len(tiles)-1),
    "posX": randint(0, DIM-1),
    "posY": randint(0, DIM-1)
}


for i in range(len(tiles)):
    tiles[i] = pygame.transform.scale(tiles[i], (width/DIM, height/DIM))

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Wave Function Collapse')

while True:
    # display_surface.blit(image, (0, 0))
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        w = width/DIM
        h = height/DIM
        # pygame.Rect(x, y, width, height)
        for i in range(DIM):
            for j in range(DIM):
                break

        spawnImage(tiles[seed['image']], seed['posX']* w, seed['posY']*h)
        grid[seed['posX']+seed['posY']*DIM]['Collapsed'] = True
        grid[seed['posX']+seed['posY']*DIM]['Options'] = [BLANK]

        gridCopy = sorted(grid, key=lambda x: x['Options'])
        length = len(gridCopy[0]['Options'])

        for i in range(len(gridCopy)):
            if len(gridCopy[i]['Options']) > len:
                gridCopy.sli

        for i in range(DIM):
            for j in range(DIM):
                cell = grid[i+j*DIM]
                if(cell['Collapsed']):
                    index = cell['Options'][0]
                    spawnImage(tiles[0], i*w, j*h)
                else:
                    pygame.draw.rect(screen, white, pygame.Rect(i*w, j*h, width/DIM, height/DIM), 2)
                
        

        pygame.display.update()
