import pygame
from graphique import Grid
import algo
from Fourmis import Fourmi

class Start:

    def __init__(self, ROWS, WIDTH):
        self.ROWS = ROWS
        self.WIDTH = WIDTH
        self.win = pygame.display.set_mode((WIDTH, WIDTH))
        self.grid_c = Grid()
        self.grid = self.grid_c.make_grid(ROWS, WIDTH)
        self.start = None
        self.end = None
     
        


    def getStart(self,start):
        
        fourmis = Fourmi(start.col, start.row)

        print(start.row)

    def x(self):
        print("test")



    def funcStart(self):

        run = True
        while run:
            self.grid_c.draw(self.win, self.grid, self.ROWS, self.WIDTH)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if pygame.mouse.get_pressed()[0]:  # LEFT
                    pos = pygame.mouse.get_pos()
                    row, col = self.grid_c.get_clicked_pos(pos, self.ROWS, self.WIDTH)
                    spot = self.grid[row][col]
                    if not self.start and spot != self.end:
                        
                        self.start = spot
                        self.fourmis = spot
                        
                        #self.getStart(spot)
                        self.start.make_start()
                        #self.fourmis.make_fourmis()
                    
                        

                    elif not self.end and spot != self.start:
                        self.end = spot
                        self.end.make_end()

                    elif spot != self.end and spot != self.start:
                        spot.make_barrier()

                elif pygame.mouse.get_pressed()[2]:  # RIGHT
                    pos = pygame.mouse.get_pos()
                    row, col = self.grid_c.get_clicked_pos(pos, self.ROWS, self.WIDTH)
                    spot = self.grid[row][col]
                    spot.reset()
                    if spot == self.start:
                        self.start = None
                    elif spot == self.end:
                        self.end = None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.start and self.end:
                        for row in self.grid:
                            for spot in row:
                                spot.update_neighbors(self.grid)

                        #algo.algorithm(lambda: self.grid_c.draw(self.win, self.grid, self.ROWS, self.WIDTH), self.grid, self.start, self.end)
                        

                    if event.key == pygame.K_c:
                        self.start = None
                        self.end = None
                        self.grid = Grid.make_grid(self.ROWS, self.WIDTH)

        pygame.quit()
