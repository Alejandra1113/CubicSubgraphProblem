import random as rand
import numpy as np
import GeneticCubic as gc
import os

def make_matrixs_Cubic():
    for i in range(0,42,2):
        for j in range(0,30,2):
            os.makedirs(f'matrix/{i+10}_Nodes/',exist_ok= True)
            np.save(f'matrix/{i+10}_Nodes/Cubic_{j}', gc.gen_random_graph(i+10))



#np.load('tomate.npy')