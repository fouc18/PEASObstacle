import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.pheromone = 0
        self.visited = False
        #Ajouter le cout de tous les spots
        self.cost = 1

    def __str__(self): 
        return '%s, %a ' %(self.row, self.col)

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def make_fourmis(self):
        self.width = self.width // 2
        return self.col == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
    
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    
    def __lt__(self, other):
        return False


class Grid:

    def __init__(self):
     
        self.grid = []
    
    

    def make_grid(self, rows, width):
        self.grid = []
        gap = width // rows
        for i in range(rows):
            self.grid.append([])
            for j in range(rows):
                spot = Spot(i, j, gap, rows)
                self.grid[i].append(spot)
               
        
        return self.grid

    def draw_grid(self, win, rows, width):
        gap = width // rows
        for i in range(rows):
            pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

    def draw(self, win, grid, rows, width):
        win.fill(WHITE)

        for row in grid:
            for spot in row:
                spot.draw(win)

        self.draw_grid(win, rows, width)
        pygame.display.update()

    def get_clicked_pos(self, pos, rows, width):
        gap = width // rows
        y, x = pos

        row = y // gap
        col = x // gap

        return row, col

    def __str__(self): 
        return "Position d'un noeud a% " % (self.Spot.row)

    
