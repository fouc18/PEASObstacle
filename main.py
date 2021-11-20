import pygame
from start import Start
from Fourmis import Fourmi
from algo import Algo

interface = Start(10,400)

interface.funcStart()

ant = Fourmi(interface.start)

ant = Fourmi(interface.start)
    
ant = Fourmi(interface.start)
algo = Algo()

algo.listeFourmis.append(ant)

#Creer une liste de fourmis
algo.Initialize(interface.grid, interface.start)

print(interface.start)

#print(ant.posX)
ant.getVoisins(interface.WIDTH, interface.grid)

print(ant.noeudVisite)

algo.SelectNextEdge()


















