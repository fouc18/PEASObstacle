import pygame
import math
from queue import PriorityQueue
import random



class Algo:

    def __init__(self):

        self.listeFourmis = []
        #Doit etre compris entre 0 et 1
        self.influenceDesPheromones = 0.2
        self.addData = 0.5
        self.pheromone = 2
        



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
    def Initialize(self, grid, s):
        C = 0
        for i in range (len(grid)):
            for j in range(len(grid)):
                grid[i][j].pheromone = 0
                
                grid[i][j].visited = False

                if grid[i][j].cost > C:
                    C = grid[i][j].cost
        
        #??? lenght = C(V-1)
        time = 0
        for fourmis in range(len(self.listeFourmis)):

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
    def SelectNextEdge(self, noeud, fourmis):
        #Verifi si le prochain noeud n'est pas en dehors du tableau
        if noeud == None:
             return None
        else:
            best = -1
            result = None
            
            for noeud in range(len(fourmis.listeVoisins)):
            #Si le noeud n'a pas encore ete visite

                if fourmis.listeVoisins[noeud] != None and fourmis.listeVoisins[noeud].visited == False:
                    current = self.ComputeCoefficient(fourmis.listeVoisins[noeud], fourmis)

                    #Si le noeud est la meilleure option
                    if current > best:
                        best = current
                        result = fourmis.listeVoisins[noeud]

                    elif current == best and random.uniform(0,1) > 0.9:
                        result = fourmis.listeVoisins[noeud]

        return result

    #Retourne le cout d'un certain chemin
    #! S'assurer que le cout des chemin > 1
    def computeLenght(self, fourmi):
        return sum(fourmi.noeudVisite.cost)

    def calculEdgeCoefficient_prime(self):
        return self.influenceDesPheromones

    #Verifie la quantite de pheromone sur un noeud en prennant en compte
    #L'infleunce des pheromones et les donnees additionnelle
    def calculEdgeCoefficient(self, noeud):
        if noeud.visited == False:
            return (self.pheromone * self.influenceDesPheromones)*(1+self.addData)
        else:
            return (self.pheromone * self.influenceDesPheromones)


    """
    Prends en entre un noeud et une fourmis et retourne le coefficient du chemin
    """
    def ComputeCoefficient(self,noeud,fourmis):
        #Si le noeud n'a pas de pheromones, en ajouter 
        if noeud.pheromone == 0:
            return self.calculEdgeCoefficient_prime()
        else:
            if len(fourmis.getRun) > 6:
                return 0
            else:
                return self.calculEdgeCoefficient(noeud)

    def EvaporateOfShortestPath(self,i,j):
        pass
        

    def edgeCoefficient(grid):
        pass
    #Initialise les donnees accumules par les fourmis a 0 
    def reset(self,graphe, fourmis):

        self.data =[]
        
    #initialise les noeuds visites par la fourmis en un tableau vide
    def setRun(self,fourmi):
        
        fourmi.noeudVisite = []

    #Initialise le noeud de depart de la fourmi
    # s est un tableau [posX, posY]
    def setNode(self,fourmi, s):

        self.posX, self.posY = s.row, s.col
    
    #Insere le noeud de depart dans la liste des noeuds visites
    def setVisited(self,fourmis, s):
        fourmis.noeudVisite.append(s)
    
    #Ajoute la fourmis a la liste de toutes les fourmis
    def add(list, time, fourmi):
        pass

    def __str__(self): 
        return "Position d'un noeud a% " % (self.Spot.row)