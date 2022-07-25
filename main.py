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

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Wave Function Collapse')

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

# Functions
def spawnImage(img, x, y):
    screen.blit(img, (x, y))

def elementExists(a_list, index):
    return index < len(a_list)

def spawnText(text, W, H, R=255, G=255, B=255):
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render(text, False, (R, G, B))
    screen.blit(text_surface, (W, H))


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


while True:
    # display_surface.blit(image, (0, 0))
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
        # spawnText(, 200, 200)

        w = width/DIM
        h = height/DIM
        # pygame.Rect(x, y, width, height)
        for i in range(DIM):
            for j in range(DIM):
                 pygame.draw.rect(screen, white, pygame.Rect(i*w, j*h, width/DIM, height/DIM), 2)

        spawnImage(tiles[seed['image']], seed['posX']* w, seed['posY']*h)
        grid[seed['posX']+seed['posY']*DIM]['Collapsed'] = True
        # grid[seed['posX']+seed['posY']*DIM]['Options'] = [BLANK, UP]

        gridCopy = sorted(grid, key=lambda x: x['Options'])
        length = len(gridCopy[0]['Options'])
        print(gridCopy)                   



        pygame.display.flip()
