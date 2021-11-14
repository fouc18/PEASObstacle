import pygame
from graphique import Grid
import algo
from Fourmis import Fourmi

class Start:


   

    def getStart(self,start):
        
        fourmis = Fourmi(start.col, start.row)

        print(start.row)



    def start(self):
        ROWS = 50
        WIDTH = 800
        win = pygame.display.set_mode((WIDTH, WIDTH))
        grid_c = Grid()
        grid = grid_c.make_grid(ROWS, WIDTH)

        start = None
        end = None

        run = True
        while run:
            grid_c.draw(win, grid, ROWS, WIDTH)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if pygame.mouse.get_pressed()[0]:  # LEFT
                    pos = pygame.mouse.get_pos()
                    row, col = grid_c.get_clicked_pos(pos, ROWS, WIDTH)
                    spot = grid[row][col]
                    if not start and spot != end:
                        
                        start = spot
                        self.getStart(spot)
                        start.make_start()
                    
                        

                    elif not end and spot != start:
                        end = spot
                        end.make_end()

                    elif spot != end and spot != start:
                        spot.make_barrier()

                elif pygame.mouse.get_pressed()[2]:  # RIGHT
                    pos = pygame.mouse.get_pos()
                    row, col = grid_c.get_clicked_pos(pos, ROWS, WIDTH)
                    spot = grid[row][col]
                    spot.reset()
                    if spot == start:
                        start = None
                    elif spot == end:
                        end = None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and start and end:
                        for row in grid:
                            for spot in row:
                                spot.update_neighbors(grid)

                        algo.algorithm(lambda: grid_c.draw(win, grid, ROWS, WIDTH), grid, start, end)

                    if event.key == pygame.K_c:
                        start = None
                        end = None
                        grid = Grid.make_grid(ROWS, WIDTH)

        pygame.quit()
