import pygame
import math
from queue import PriorityQueue
import random



class Algo:

    def __init__(self):

        self.listeFourmis = []



    '''
    E/: Chemin de s a t
    V: Nombre de sommet du graphe  
    G: Graphe (V, E/) avec comme sommet initial s
    a: defini l'influence des pheromones sur le choix du prochain chemin
    s: point initial
    t: point final
    k: fourmis
    
    La fonction initialise l'algorithme des colonies de fourmis
    '''
    def Initialize(self,grid, s):
        C = 0
        for node in grid.spot:

            grid.spot[node].pheromone = 0

            grid.spot[node].visited = False

            if grid.spot[node].cost > C:
                C = grid.spot[node].cost
        
        #??? lenght = C(V-1)
        time = 0
        for fourmis in self.listeFourmis:

            self.reset(grid, self.listeFourmis[fourmis])
            self.setRun(self.listeFourmis[fourmis])
            self.setNode(self.listeFourmis[fourmis], s)
            self.setVisited(self.listeFourmis[fourmis], s)
            self.add(time, self.listeFourmis[fourmis])

    """
    Noeud: noeud
    Fourmis: Foumis
    graoge

    return: Le prochain noeud choisi
    """
    def SelectNextEdge(self, noeud, fourmis, graphe):

        #if p.7 ??? return null else:
        best = -1
        result = NULL
        for noeud in graphe:
            #Si le noeud n'a pas encore ete visite
            if graphe.spot[noeud].visited == False:
                self.ComputeCoefficient(noeud, fourmis)

                #Si le noeud est la meilleure option
                if graphe.spot[noeud] > best:
                    best = graphe.spot[noeud]
                    result = graphe.spot[noeud].getPos()

                elif graphe.spot[noeud] == best and random.uniform(0,1) > 0.5:
                    result = graphe.spot[noeud].getPos()

        return result

     
    def ComputeCoefficient(self,i,j,k):
        pass
    def EvaporateOfShortestPath(self,i,j):
        pass

    #Initialise les donnees accumules par les fourmis a 0 
    def reset(self,graphe, fourmis):

        self.data =[]
        
    #initialise les noeuds visites par la fourmis en un tableau vide
    def setRun(self,fourmi):
        
        self.noeudVisite = []

    #Initialise le noeud de depart de la fourmi
    # s est un tableau [posX, posY]
    def setNode(self,fourmi, s):

        self.posX, self.posY = s
    
    #Insere le noeud de depart dans la liste des noeuds visites
    def setVisited(self,fourmis, s):

        fourmis.noeudVisite.append(s)
    
    #Ajoute la fourmis a la liste de toutes les fourmis
    def add(list, time, fourmi):
        pass