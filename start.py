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
        self.compte = 0
        self.compte2 = 0
        self.moyenne = 0
        self.obstacle = []
        self.spotFourmis =  None
     
        
    def getStart(self,start):
        
        fourmis = Fourmi(start.col, start.row)

        

    

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
                        self.obstacle.append(spot)
                        for spots in range(len(self.obstacle)):
                            self.obstacle[spots].make_barrier()

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

                       
                        
                        
                        
                        #Creer une liste de fourmis
                        algo.Initialize(self.grid, self.start)
                        #print("fourmi run", algo.listeFourmis[0].noeudVisite)
                        #print(ant.posX)
                       # ant.getVoisins(self.WIDTH, self.grid)
                        for i in range(800):
                           
                           
                            for row in range(len(self.grid)):
                                
                                for col in range(len(self.grid)):
                                    if self.grid[row][col] != self.start or self.grid[row][col] != self.end:
                                        self.grid[row][col].reset()
                            #time.sleep(0.005)
                                
                            ant = Fourmi(self.start)
                            algo.listeFourmis.append(ant)

                            while ( ( algo.listeFourmis[i].getPosX() != self.end.getXpos() ) or ( algo.listeFourmis[i].getPosY() ) != ( self.end.getYpos() ) ) and self.compte < 800:
                                
                                
                                algo.listeFourmis[i].getVoisins(self.ROWS, self.grid)
                                #for fourmi in range(len(algo.listeFourmis)):
                                    
                                bestNode = algo.SelectNextEdge(algo.listeFourmis[i].getListeVoisins(), algo.listeFourmis[i])
                                
                                algo.listeFourmis[i].move(bestNode)

                                bestNode.pheromone = bestNode.pheromone + 1
                                
                                self.compte = self.compte + 1
                                algo.listeFourmis[i].listeVoisins.clear()
                            
                                algo.setVisited(algo.listeFourmis[i],bestNode)
                                self.spotFourmis = self.grid[algo.listeFourmis[i].posX][algo.listeFourmis[i].posY] 

                                for spots in range(len(self.obstacle)):
                                    self.obstacle[spots].make_barrier()
                                    
                                self.spotFourmis.make_fourmis()

                                self.start.make_start()
                                self.end.make_end()
                                
                                

                                
                                self.grid_c.draw(self.win, self.grid, self.ROWS, self.WIDTH)
                                #self.grid[bestNode.col][bestNode.row].make_fourmis()

                            

                            algo.listeFourmis[i].noeudVisite = list(dict.fromkeys(algo.listeFourmis[i].noeudVisite))

                          
                            if i > 1:
                                for noeudPheromone in range(len(algo.listeFourmis[i].noeudVisite)):
                                    if self.compte < self.compte2:
                                        algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone = algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone + 200
                            """if len(algo.listeFourmis[i].noeudVisite) < 200 and len(algo.listeFourmis[i].noeudVisite) > 100 :

                                for noeudPheromone in range(len(algo.listeFourmis[i].noeudVisite)):
                                    algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone = algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone + 2
                               """


                            """if len(algo.listeFourmis[i].noeudVisite) < 25 and len(algo.listeFourmis[i].noeudVisite) > 15 :
                                for noeudPheromone in range(len(algo.listeFourmis[i].noeudVisite)):
                                    algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone = algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone + 4

                            elif len(algo.listeFourmis[i].noeudVisite) < 15 and len(algo.listeFourmis[i].noeudVisite) > 10:
                                for noeudPheromone in range(len(algo.listeFourmis[i].noeudVisite)):
                        
                                    algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone = algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone + 10
                            
                            elif len(algo.listeFourmis[i].noeudVisite) < 10:
                                for noeudPheromone in range(len(algo.listeFourmis[i].noeudVisite)):
                                    algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone = algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone + 10000
                            else:
                                for noeudPheromone in range(len(algo.listeFourmis[i].noeudVisite)):
                                    algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone = algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone + 0.5
                            """
                            



                            

                                #time.sleep(0.05)
                                
                                #algo.algorithm(lambda: self.grid_c.draw(self.win, self.grid, self.ROWS, self.WIDTH), self.grid, self.start, self.end)
                            print("FINI !")
                            
                            
                            print("fourmi run", algo.listeFourmis[i].noeudVisite)
                            print("compte",self.compte)
                            print("noeud",len(algo.listeFourmis[i].noeudVisite))
                            
                            self.moyenne = self.compte + self.moyenne 
                            self.compte2 = self.compte
                            self.compte = 0
                            
                            """

                            for noeud in range(len(algo.listeFourmis[i].noeudVisite)):
                                #evaporation des pheromones
                                algo.listeFourmis[i].noeudVisite[noeud].pheromone = 1 - 0.5
                            """
                        print("moyenne",self.moyenne/200)  
                        

                    if event.key == pygame.K_c:
                        self.start = None
                        self.end = None
                        self.grid = Grid.make_grid(self.ROWS, self.WIDTH)

        pygame.quit()
