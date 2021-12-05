#Classe decrivant les comportements d'une fourmi d'un algorithme ant 
#colony optimisation
class Fourmi:
   
    def __init__(self, start):
        #Position en X de la fourmi
        self.posX = start.row
        #Position en Y de la fourmi
        self.posY = start.col
        #Liste des noeuds visites de la fourmi
        self.noeudVisite = []
        #Liste des voisins de la fourmi
        self.listeVoisins = []
    
    def getPosY(self):
        return self.posY

    def getPosX(self):
        return self.posX

    #Deplace la fourmi vers un noeud
    def move(self, noeud):
        self.posX = noeud.row
        self.posY = noeud.col

    def getListeVoisins(self):
        """[Retourne la liste des voisins de gauche, droite, en haut
            et en bas d'une fourmi]
        """
        return self.listeVoisins
        
    def getRun(self):
        return self.noeudVisite

    #Delace la fourmi droite, gauche, en bas, en haut
    def getVoisins(self, gridWith, grid):
        """Verifi si les voisins de la fourmi sont des
           noeud valide au deplacement

        Args:
            gridWith : [Grosseur de la grille dans laquelle la fourmi se deplace]
            grid : [objet grid]
        """
        #Voisin de droite
        #Si le voisin n'est pas un noeud valide
        if self.getPosX() + 1 > gridWith -1:

            self.listeVoisins.append(None) 
        #Si le voisin est un obstacle
        elif grid[self.posX+1][self.posY].isBlack():
            
            self.listeVoisins.append(None)
        #Le voisin est valide
        else:
            self.listeVoisins.append(grid[self.posX+1][self.posY])
        
        #Voisin de gauche
        #Si le voisin n'est pas un noeud valide
        if self.getPosX()-1 <  0:

            self.listeVoisins.append(None)
        #Si le voisin est un obstacle
        elif grid[self.posX-1][self.posY].isBlack():

            self.listeVoisins.append(None)
        #Le voisin est valide
        else:
            self.listeVoisins.append(grid[self.posX-1][self.posY])

        #Voisin d'en bas
        #Si le voisin n'est pas un noeud valide
        if self.getPosY()+1 > gridWith -1:
            self.listeVoisins.append(None)
        #Si le voisin est un obstacle
        elif grid[self.posX][ self.posY+1].isBlack():
            self.listeVoisins.append(None)
        #Le voisin est valide
        else:
            self.listeVoisins.append(grid[self.posX][ self.posY+1])

        #Voisin d'en haut
        #Si le voisin n'est pas un noeud valide
        if self.getPosY()-1 < 0:
            self.listeVoisins.append(None)
        #Si le voisin est un obstacle
        elif grid[self.posX][self.posY-1].isBlack():
            self.listeVoisins.append(None)
        #Le voisin est valide
        else:
            self.listeVoisins.append(grid[self.posX][self.posY-1])

    def getListeNoeudVisite(self):
        """[Retourne la liste des noeuds visites d'une fourmi]

        """
        return self.noeudVisite
            


            

            
                
        
