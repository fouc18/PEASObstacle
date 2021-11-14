class Fourmi:
    def __init__(self, posX, posY):

        self.posX = posX
        self.posY = posY
        self.noeudVisite = []
        self.data = []
        self.deltaT = 1
        self.listePheromone = 0
 
    def move(self, pos):
        self.posX = pos[0]
        self.posY = pos[1]

    def getRun(self):
        return self.noeudVisite
        
