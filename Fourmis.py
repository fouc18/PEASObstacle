class Fourmi:
    def __init__(self, posX, posY):

        self.posX = posX
        self.posY = posY
        self.noeudVisite = []
        self.data = []
        
        

    '''
    E/: Chemin de s a t
    V: Nombre de sommet du graphe  
    G: Graphe (V, E/) avec comme sommet initial s
    a: defini l'influence des pheromones sur le choix du prochain chemin
    s: point initial
    t: point final
    k: fourmis
    '''
    def Initialize(self,G, s):
    
        pass

    def SelectNextEdge(self, i, k):
        pass
    def ComputeCoefficient(self,i,j,k):
        pass
    def EvaporateOfShortestPath(self,i,j):
        pass

    def getPos(self):
        return [self.posX, self.posY] 

    def Reset(graphe, fourmis):
        pass

    def setRun(fourmi):
        pass

    def setNode(fourmi, s):
        pass
    def setVisited(fourmi, s):
        pass
    
    def add(list, time, fourmi):
        pass

    


    def move(self):
        pass
        
