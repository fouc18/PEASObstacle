
class Fourmi:
    def __init__(self, start):

        self.posX = start.row
        self.posY = start.col
        self.noeudVisite = []
        self.data = []
        self.deltaT = 1
        self.listePheromone = 0
        self.listeVoisins = []
    
    def getPosY(self):
        return self.posY

    def getPosX(self):
        return self.posX
 
    def move(self, noeud):

        self.posX = noeud.row
        self.posY = noeud.col

    def getListeVoisins(self):
        return self.listeVoisins
        

    def getRun(self):
        return self.noeudVisite

    #droite, gauche, en bas, en haut
    def getVoisins(self, gridWith, grid):

        
        #Voisin de droite
        if self.getPosX() + 1 > gridWith -1:
            self.listeVoisins.append(None) 
        elif grid[self.posX+1][self.posY].isBlack():
             self.listeVoisins.append(None)
        else:
            self.listeVoisins.append(grid[self.posX+1][self.posY])

        #Voisin de gauche
        if self.getPosX()-1 <  0:
            self.listeVoisins.append(None)
        elif grid[self.posX-1][self.posY].isBlack():
            self.listeVoisins.append(None)
        else:
            self.listeVoisins.append(grid[self.posX-1][self.posY])

        #Voisin d'en bas
        if self.getPosY()+1 > gridWith -1:
            self.listeVoisins.append(None)
        elif grid[self.posX][ self.posY+1].isBlack():
            self.listeVoisins.append(None)
        else:
            self.listeVoisins.append(grid[self.posX][ self.posY+1])

        #Voisin d'en haut
        if self.getPosY()-1 < 0:
            self.listeVoisins.append(None)
        elif grid[self.posX][self.posY-1].isBlack():
            self.listeVoisins.append(None)
        else:
            self.listeVoisins.append(grid[self.posX][self.posY-1])

    def printVoisin(self):
        for voisin in self.listeVoisins :
            print(voisin)

    def getListeNoeudVisite(self):

        return self.getListeNoeudVisite
            


            

            
                
        
