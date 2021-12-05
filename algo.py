import random

class Algo:

    def __init__(self):
        self.listeFourmis = []
        self.influenceDesPheromones = 50
        self.addData = 0

    def SelectNextEdge(self, listeVoisins, fourmis, noeud):
        """Cet algorithme permet a la fourmi de choisir le noeud optimal
            parmi ses voisins

        Args:
            liste : Liste des voisins de la fourmi
            fourmis : Fourmi specifique
            noeud ([type]): Noeud a evaluer par l'algorithme 

        Returns:
            Le noeud optimal choisi par l'algorithme
        """
        #Si la fourmi detient des voisins
        if listeVoisins is not None:
                best = -1
                result = None  
        #Pour les noeuds voisins de la fourmi  
        for nodes in range(len(listeVoisins)):
            #Si le prochain noeud n'est pas en dehors du tableau
            if listeVoisins[nodes] is not None :
                #Calcul du coefficient du noeud
                current = self.ComputeCoefficient(listeVoisins[nodes], fourmis)
                #Si le noeud est la meilleure option
                if current > best:
                    best = current
                    result = listeVoisins[nodes]
                #Ajout d'un element random pour eviter que la fourmi ne fasse
                    #du sur place
                elif current is best and random.uniform(0,1) > 0.80:
                    result = listeVoisins[nodes]

        return result

    def calculEdgeCoefficient_prime(self, noeud):
        """
           Cet algorithme permet de definir le noeud le plus optmial
           dans le cas ou le noeud selectionne ne detient pas de pheromones

        Args:
            noeud : Noeud presentement en evaluation

        Returns:
            Le score du noeud. 
            Plus le score est haut, meilleur est le noeud
        """
        return noeud.pheromone**(self.influenceDesPheromones) 

    def calculEdgeCoefficient(self, noeud):
        """
           Cet algorithme permet de definir le noeud le plus optmial
           dans le cas ou le noeud selectionne detient des pheromones

        Args:
            noeud : Noeud presentement en evaluation

        Returns:
            Le score du noeud. 
            Plus le score est haut, meilleur est le noeud
        """
        if noeud.visited == False:
            return (noeud.pheromone * self.influenceDesPheromones)
        
    def ComputeCoefficient(self,noeud,fourmis):
        """Prend un noeud et une fourmi en entre et calcul le score
           d'un noeud en fonction de l'etat des pheronomes du noeud
           et de la quantite de noeud visite par la fourmi
           
        Args:
            noeud : Noeud en evaluation
            fourmis : Fourmi en evaluation

        Returns:
            Le noeud le plus optimal.
        """
        #Si le noeud n'a pas de pheromone
        if noeud.pheromone == 1:
            return self.calculEdgeCoefficient_prime(noeud)
        #Si la course de la fourmi est inferieur a un nombre de noeud x
        #le prochain noeud choisi sera random
        else:
            if len(fourmis.getRun())  < 10 : 
                return 0
            else:
                return self.calculEdgeCoefficient(noeud)

    
    def setVisited(self,fourmis, s):
        """Ajoute un noeud a la liste des noeud visite

        Args:
            fourmis : Fourmi 
            s : Noeud visite
        """
        fourmis.noeudVisite.append(s)
    
    def __str__(self): 
        return "Position d'un noeud a% " % (self.Spot.row)