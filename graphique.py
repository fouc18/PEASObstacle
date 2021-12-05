import pygame

#Liste des couleurs utilise par la partie graphique du logiciel.
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
    def __init__(self, row, col, width, total_rows):
        #Range d'un noeud
        self.row = row
        #Colone d'un noeud
        self.col = col
        #Position en x d'un noeud
        self.x = row * width
        #Position en y d'un noeud
        self.y = col * width
        #Couleur de depart d'un noeud
        self.color = WHITE
        #Voisins d'un noeud
        self.neighbors = []
        #Longueur d'un noeud
        self.width = width
        self.total_rows = total_rows
        #Pheromone de depart d'un noeud
        self.pheromone = 1
        self.visited = False
        #Ajouter le cout de tous les spots
        self.cost = 1
        

    def __str__(self): 
        return '%s, %a ' %(self.row, self.col)

    def get_pos(self):
        """
        Pour detenir la position d'un noeud

        Returns:
            self.row, self.col: Retourne la position relative d'un noeud
        """
        return self.row, self.col

    def isBlack(self):
        """
        Identifie si un noeud est un obstacle ou non

        Returns:
            Boolean: Si le noeud est noir (obstacle) return True aussi non
            Return false
        """
        if self.color == BLACK:
            return True
        return False

    def getXpos(self):
        """
        Identifie la position en x d'un noeud

        Returns:
            self.row:
        """
        return self.row
    
    def getYpos(self):
        """
        Identifie la position en y d'un noeud

        Returns:
            self.col: 
        """
        return self.col

    def make_fourmis(self):
        """
        Definie le noeud comme etant une fourmi
        """
        
        self.color = GREEN

    def is_barrier(self):
        """
        Identifie le noeud comme etant un obstacle

        Returns:
            self.color
        """
        return self.color == BLACK

    def is_start(self):
        """
        Identifie le noeud comme etant le point de depart

        Returns:
            self.color
        """
        return self.color == ORANGE

    def is_end(self):
        """
        Identifie le noeud comme etnat le point de fin

        Returns:
            self.color
        """
        return self.color == TURQUOISE

    def reset(self):
        """
        Defini un noeud vide 
        """
        self.color = WHITE

    def make_start(self):
        """
        Definie le noeud de depart
        """
        self.color = ORANGE

    def make_barrier(self):
        """
        Definie un obstacle
        """
        self.color = BLACK

    def make_end(self):
        """
        Defini le noeud de fin
        """
        self.color = TURQUOISE

    def draw(self, win):
        """Appel de la fonction qui dessine la grille a l'ecran

        Args:
            ecran, couleurs, position des noeud et grandeur de la fenetre
        """
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def __lt__(self, other):
        return False


class Grid:

    def __init__(self):
     
        self.grid = []

    def make_grid(self, rows, width):
        """Construit un tableau avec le nombre de range et grandeur souhaite

        Args:
            rows : Nombre de range souhaite
            width : Grandeur du tableau souhaite

        Returns:
            Grid: Un tableau construit
        """
        self.grid = []
        gap = width // rows
        #rows et col sont egaux, car le tableau est un carre
        for i in range(rows):
            self.grid.append([])
            for j in range(rows):
                spot = Spot(i, j, gap, rows)
                self.grid[i].append(spot)
               
        
        return self.grid

    def draw_grid(self, win, rows, width):
        """Dessine un tableau a l'ecran

        Args:
            win : Surface sur laquelle dessiner
            rows : Nombre de ranges souhaite
            width : Largeur souhaite
        """
        #Largeur des noeuds
        gap = width // rows
        for i in range(rows):
            pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

    def draw(self, win, grid, rows, width):
        """Dessine les elements a l'ecran

        Args:
            win : Surface sur laquelle dessiner
            grid : Tableau
            rows : Nombre de ranges souhaite
            width : Largeur souhaite
        """
        win.fill(WHITE)
        for row in grid:
            for spot in row:
                spot.draw(win)

        self.draw_grid(win, rows, width)
        pygame.display.update()

    def get_clicked_pos(self, pos, rows, width):
        """Nous permet de savoir ou l'utilisateu clique

        Args:
            pos : Position du curseur relative a la fenetre
            rows : Position du curseur relative au tableau
            width : Largeur de l'ecran

        Returns:
            position: Retourne la colone et la range ou l'utilisateur a clique
        """
        gap = width // rows
        y, x = pos
        row = y // gap
        col = x // gap

        return row, col

    def __str__(self): 
        return "Position d'un noeud a% " % (self.Spot.row)

    
