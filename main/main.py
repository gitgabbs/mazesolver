import pygame
from find_solution import FindSolution

# initialize pygame window
pygame.init()

solve = FindSolution()

margin = 20

if solve.width>solve.height:
    cell_size = (600-margin*2)//solve.width
else:
    cell_size = (600-margin*2)//solve.height

screen_width = cell_size*solve.width+margin*2
screen_height = cell_size*solve.height+margin*2

window = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
    
#for i in range(len(solve.marked)):
#            maze_row = ""
#            for j in range(len(solve.marked[i])):
#                maze_row = maze_row + str(solve.marked[i][j]) + " "
#            print(maze_row)

class Draw():
    def __init__(self):
        pass

    def empty_paths():
        indx_y = 0
        for i in solve.marked:
            indx_x = 0
            y = margin+indx_y*cell_size
            for j in i:
                x = margin+indx_x*cell_size
                coord = (x, y, cell_size, cell_size)
                indx_x += 1
                if j == "#":
                    #mark walls as white (correct path is black)
                    pygame.draw.rect(window, (255, 255, 255), coord)
            indx_y += 1

    def solution():
        indx_y = 0
        for i in solve.marked:
            indx_x = 0
            y = margin+indx_y*cell_size
            for j in i:
                x = margin+indx_x*cell_size
                coord = (x+1, y+1, cell_size-2, cell_size-2)
                indx_x += 1
                if j != "#" and j != "x" and j != 0:
                    pygame.draw.rect(window, (255, 0, 0), coord)
            indx_y += 1

while True:
    window.fill(pygame.Color(0,0,0))

    Draw.empty_paths()
    Draw.solution()

    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            exit()

    pygame.display.flip()