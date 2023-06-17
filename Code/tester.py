import GeneticCubic as gc
import BacktrackCubicSubgraph as bt
import numpy as np
import os
import json

def test_genetic():
    with open('result_genetic_18.json', 'w') as fp:
        dict_results = {}    
        for s in os.listdir('matrix/18_Nodes/'):
            graph = np.load(f'matrix/18_Nodes/{s}')
            
            dict_results[s] = {}
            for i in range(3):
                best_fit, best_sol, line = gc.genetic_algo(graph, 3000)
                dict_results[s][i] = {
                    'best_fit': int(best_fit),
                    'line': [int(t) for t in line]
                }
        json.dump(dict_results, fp)

def test_back():
    with open('result_back_10.json', 'w') as fp:
        dict_results = {}    
        for s in os.listdir('matrix/10_Nodes/'):
            graph = np.load(f'matrix/10_Nodes/{s}')
  
            edges = []
            for u in range(graph.shape[0]):
                for v in range(u, graph.shape[0]):
                    if u == v:
                        continue
                    edges.append((u,v))
            is_cubic = bt.BacktrackCubicS(edges, [0] * graph.shape[0])
            if is_cubic:
                dict_results[s] = 1
            else:
                dict_results[s] = 0
        json.dump(dict_results, fp)

def test_back_14():
    with open('result_back_14.json', 'w') as fp:
        dict_results = {}    
        for s in ['NoCubic_24.npy', 'NoCubic_6.npy']:
            graph = np.load(f'matrix/10_Nodes/{s}')
  
            edges = []
            for u in range(graph.shape[0]):
                for v in range(u, graph.shape[0]):
                    if u == v:
                        continue
                    edges.append((u,v))
            is_cubic = bt.BacktrackCubicS(edges, [0] * graph.shape[0])
            if is_cubic:
                dict_results[s] = 1
            else:
                dict_results[s] = 0
        json.dump(dict_results, fp)

test_genetic()

