
class Fourmi:
    def __init__(self, start):

        self.posX = start.row
        self.posY = start.col
        self.noeudVisite = []
        self.data = []
        self.deltaT = 1
        self.listePheromone = 0
        self.listeVoisin = []
 
    def move(self, pos):
        self.posX = pos[0]
        self.posY = pos[1]

    def getRun(self):
        return self.noeudVisite

    #droite, gauche, en bas, en haut
    def getVoisins(self, gridWith, grid):
        
        #Voisin de droite
        if self.posX + 1 >= gridWith:
            self.listeVoisin.append(None)
        else:
            self.listeVoisin.append(grid[self.posX+1][self.posY])

        #Voisin de gauche
        if self.posX-1 <  0:
            self.listeVoisin.append(None)
        else:
            self.listeVoisin.append(grid[self.posX-1][self.posY])

        #Voisin d'en bas
        if self.posY-1 < 0:
            self.listeVoisin.append(None)
        else:
            self.listeVoisin.append(grid[self.posX][ self.posY-1])

        #Voisin d'en haut
        if self.posY+1 >= gridWith:
            self.listeVoisin.append(None)
        else:
            self.listeVoisin.append(grid[self.posX][self.posY+1])

    def printVoisin(self):
        for voisin in self.listeVoisin :
            print(voisin)
            


            

            
                
        
