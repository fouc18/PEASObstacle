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

    #Initialise les donnees accumules par les fourmis a 0 
    def Reset(self,graphe, fourmis):

        self.data =[]
        
    #initialise les noeuds visites par la fourmis en un tableau vide
    def setRun(self,fourmi):
        
        self.noeudVisite = []

    #Initialise le noeud de depart de la fourmi
    # s est un tableau [posX, posY]
    def setNode(self,fourmi, s):

        self.posX, self.posY = s
    
    #Insere le noeud de depart dans la liste des noeuds visites
    def setVisited(self,fourmi, s):
        self.noeudVisite.append(s)
    
    #Ajoute la fourmis a la liste de toutes les fourmis
    def add(list, time, fourmi):
        pass

    


    def move(self):
        pass
        
