import pygame
from Start import Start
from Fourmis import Fourmi
from algo import Algo


interface = Start(20,800)

interface.funcStart()

ant = Fourmi(interface.start, interface.end)

algo = Algo()

#Creer une liste de fourmis
#

algo.Initialize(interface.grid, interface.start)





















