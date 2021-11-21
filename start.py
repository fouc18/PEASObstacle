import pygame
from graphique import Grid
from algo import Algo
from Fourmis import Fourmi
import time

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
                        #self.fourmis = spot #!
                        
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
                        #for row in self.grid:
                            #for spot in row:
                             #   spot.update_neighbors(self.grid)
                        
                       # spotFourmis.make_fourmis()

                        ant = Fourmi(self.start)
                        algo = Algo()
                        algo.listeFourmis.append(ant)

                        #Creer une liste de fourmis
                        algo.Initialize(self.grid, self.start)
                        print("fourmi run", algo.listeFourmis[0].noeudVisite)
                        #print(ant.posX)
                       # ant.getVoisins(self.WIDTH, self.grid)
                        

                        while algo.listeFourmis[0].getPosX() != self.end.getXpos() or algo.listeFourmis[0].getPosY() != self.end.getYpos():
                            
                            
                            algo.listeFourmis[0].getVoisins(self.ROWS, self.grid)
                            for fourmi in range(len(algo.listeFourmis)):
                                
                                bestNode = algo.SelectNextEdge(algo.listeFourmis[0].getListeVoisins(), algo.listeFourmis[fourmi])
                            print("position de la fourmis",algo.listeFourmis[0].posX, algo.listeFourmis[0].posY) 
                            print("position du meilleur noeud", bestNode.col, bestNode.row)
                            
                            algo.listeFourmis[0].move(bestNode)
                            algo.listeFourmis[0].listeVoisins.clear()
                            print("liste voisins",algo.listeFourmis[0].listeVoisins)

                            algo.setVisited(algo.listeFourmis[0],bestNode)
                            print("best node", bestNode)
                            print("nouvelle position de la fourmis", algo.listeFourmis[0].posX, algo.listeFourmis[0].posY)
                            spotFourmis = self.grid[algo.listeFourmis[0].posX][algo.listeFourmis[0].posY] 
                            spotFourmis.make_fourmis()
                            print(spotFourmis.color)
                            self.grid_c.draw(self.win, self.grid, self.ROWS, self.WIDTH)
                            #self.grid[bestNode.col][bestNode.row].make_fourmis()
                            print(self.ROWS)
                            #ime.sleep(2)
                            #algo.algorithm(lambda: self.grid_c.draw(self.win, self.grid, self.ROWS, self.WIDTH), self.grid, self.start, self.end)
                        print("FINI !")
                        
                        print("position de la fourmis",algo.listeFourmis[0].posX, algo.listeFourmis[0].posY) 
                        print(self.end.row, self.end.col)
                        

                    if event.key == pygame.K_c:
                        self.start = None
                        self.end = None
                        self.grid = Grid.make_grid(self.ROWS, self.WIDTH)

        pygame.quit()
