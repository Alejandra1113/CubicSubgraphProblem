import random as rand
import numpy as np
import GeneticCubic as gc
import Generador
import os

def make_matrixs_Cubic():
    for i in range(0,42,2):
        for j in range(0,30,2):
            os.makedirs(f'matrix/{i+10}_Nodes/',exist_ok= True)
            np.save(f'matrix/{i+10}_Nodes/Cubic_{j}', gc.gen_random_graph(i+10))

def make_matrixs_NoCubic():
    for i in range(0,42,2):
        for j in range(0,30,2):
            os.makedirs(f'matrix/{i+10}_Nodes/',exist_ok= True)
            np.save(f'matrix/{i+10}_Nodes/NoCubic_{j}', Generador.ConnexGraphGenerator(i+10)[1])

make_matrixs_NoCubic()