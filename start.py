

import pygame
from graphique import Grid
from algo import Algo
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
        self.compte = 0
        self.obstacle = []
        self.spotFourmis =  None
        
    def funcStart(self):
        """
        Cette fonction est la principale fonction du logiciel.
        Elle relit toutes les autres classes et fonction du logiciel.
        """

        run = True
        #Demarage de la partie visuelle de l'application
        while run:
            self.grid_c.draw(self.win, self.grid, self.ROWS, self.WIDTH)
            #Verifi les evenements declanche par l'utilisateur
            for event in pygame.event.get():
                #Si l'utilisateur clique sur la croix rouge le logiciel s'arrete
                if event.type == pygame.QUIT:
                    run = False
                #Si l'utilisateur clique sur son bouton gauche de sa souris
                if pygame.mouse.get_pressed()[0]:  # LEFT
                    #Verifie la position du curseur de l'utilisateur
                    pos = pygame.mouse.get_pos()
                    row, col = self.grid_c.get_clicked_pos(pos, self.ROWS, self.WIDTH)
                    #Definit un cube avec la position du curseur de l'utilisateur
                    spot = self.grid[row][col]
                    #Si ce n'est pas un cube de depart ou de fin
                    if not self.start and spot != self.end:
                        #Definir le cube en tant que cube de depart
                        self.start = spot
                        #Colorer le cube avec la couleur d'un cube de depart
                        self.start.make_start()
                        
                    #Si le cube n;est pas un cube de depart ou de fin pour le 2e clic
                    elif not self.end and spot != self.start:
                        #Definir le cube en tant que cube de fin
                        self.end = spot
                        #Colorer le cube avec la couleur d'un cube de fin
                        self.end.make_end()
                    #Si le cube n'est pas un cube de fin et un cube de depart
                    elif spot != self.end and spot != self.start:
                        #definir le cube en tant que cube obstacle
                        self.obstacle.append(spot)
                        for spots in range(len(self.obstacle)):
                            self.obstacle[spots].make_barrier()

                #Si l'utilisateur fait un clic droit avec sa souris
                elif pygame.mouse.get_pressed()[2]:  # RIGHT
                    #Entreposer la position du clic dans la variable pos
                    pos = pygame.mouse.get_pos()
                    #Specifier la position de la souris relativement aux variables row et col du tableau
                    row, col = self.grid_c.get_clicked_pos(pos, self.ROWS, self.WIDTH)
                    spot = self.grid[row][col]
                    #Definit le cube comme etant un cube de base
                    spot.reset()
                    if spot == self.start:
                        self.start = None
                    elif spot == self.end:
                        self.end = None
                
                #Si l'utilisateur clique sur la barre d'espace
                #et que le point de depart et de fin sont defini
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.start and self.end:
                             
                        #Depart de l'algorithme
                        algo = Algo()

                        #Creer une liste de fourmis
                        for i in range(200):                       
                            for row in range(len(self.grid)):                
                                for col in range(len(self.grid)):
                                    if self.grid[row][col] != self.start or self.grid[row][col] != self.end:
                                        self.grid[row][col].reset()
                            #Definit le point de depart des fourmis
                            ant = Fourmi(self.start)
                            #Ajoute la fourmi a la liste des fourmis
                            algo.listeFourmis.append(ant)

                            #On continu l'exploration si la fourmi n'a pas atteint le point d'arrive
                            #Ou si elle n'a pas parcouru plus de 400 noeud dans son parcours
                            while ( ( algo.listeFourmis[i].getPosX() != self.end.getXpos() ) or ( algo.listeFourmis[i].getPosY() ) != ( self.end.getYpos() ) ) and self.compte < 400:
                                
                                #On defini les obstacles
                                for spots in range(len(self.obstacle)):
                                    
                                    self.obstacle[spots].make_barrier() 

                                algo.listeFourmis[i].getVoisins(self.ROWS, self.grid)
                                #On selectionne le meilleur noeud dans la liste des noeuds voisins de la fourmi      
                                bestNode = algo.SelectNextEdge(algo.listeFourmis[i].getListeVoisins(), algo.listeFourmis[i], i)
                                #La fourmi bouge au prochain noeud
                                algo.listeFourmis[i].move(bestNode)
                                #On ajoute un compte (pas de la fourmi)
                                self.compte = self.compte + 1
                                #On enleve les voisins de la liste des voisins de la fourmi
                                algo.listeFourmis[i].listeVoisins.clear()
                                #On defini le noeud actuel comme etant visite             
                                algo.setVisited(algo.listeFourmis[i],bestNode)
                                #On colore le noeud de la couleur des fourmis
                                self.spotFourmis = self.grid[algo.listeFourmis[i].posX][algo.listeFourmis[i].posY] 

                                self.spotFourmis.make_fourmis()
                                #On colore le point de depart
                                self.start.make_start()
                                #On colore le point de fin
                                self.end.make_end()
                                
                                self.end.pheromone = 1000000       
                                #Actualisation des graphiques
                                self.grid_c.draw(self.win, self.grid, self.ROWS, self.WIDTH)
                                
                            
                            #On supprime les doublons des noeud visites de la fourmi
                            algo.listeFourmis[i].noeudVisite = list(dict.fromkeys(algo.listeFourmis[i].noeudVisite))

                        #En fonction du compte (des pas de la fourmi) on ajoute des pheromones 
                            if self.compte < 30 and self.compte > 20 :
                                for noeudPheromone in range(len(algo.listeFourmis[i].noeudVisite)):
                                   
                                    algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone = algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone + 1
                               
                            if self.compte < 20 and self.compte > 15 :
                              
                                for noeudPheromone in range(len(algo.listeFourmis[i].noeudVisite)):
                                    algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone = algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone + 100
                           
                            elif self.compte > 50:
                                for noeudPheromone in range(len(algo.listeFourmis[i].noeudVisite)):
                                    algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone = algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone + 0.2
                            
                            elif self.compte < 15 and self.compte > 10:
                              
                                for noeudPheromone in range(len(algo.listeFourmis[i].noeudVisite)):
                        
                                    algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone = algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone + 500 
                            elif self.compte < 7:
                               
                                for noeudPheromone in range(len(algo.listeFourmis[i].noeudVisite)):
                                    algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone = algo.listeFourmis[i].noeudVisite[noeudPheromone].pheromone + 10000
                                                   
                            self.compte = 0
                            
                    if event.key == pygame.K_c:
                        self.start = None
                        self.end = None
                        self.grid = Grid.make_grid(self.ROWS, self.WIDTH)

        pygame.quit()
