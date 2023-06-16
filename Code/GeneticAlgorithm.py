import random
import matplotlib.pyplot as plt
import numpy as np

'''Create Graph'''
def gen_random_graph(n):
    graph = []
    for i in range(n):
        vertex = []
        for j in range(n):
            vertex.append(random.randint(0, 1))
        graph.append(vertex)
    for i in range(n):
        for j in range(0, i):
            graph[i][j] = graph[j][i]
    for i in range(n):
        graph[i][i] = 0
    return np.array(graph)

def make_create_individual(graph_base):
    n = graph_base.shape[0]
    def create_individual():
        individual = graph_base.copy()
        for i in range(1,n-1):
            for j in range(i,n-1):
                if graph_base[i][j] == 1:
                    individual[i][j] = random.randint(0,1)
        return individual
    return create_individual

def penalty_1(x):
    if x == 0 or x == 3:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return x - 3
    
def make_fitness_1(graph_base):
    penalty = graph_base.sum()//2
    def fitness(graph):
        fit = 0
        degres = graph.sum(axis=0)
        for d in degres:
            fit += penalty_1(d)
        if degres.sum() == 0:
            fit += penalty
        return fit
    return fitness


class GeneticAlgorithm:
    
    def __init__(self, create_individual, fitness, crossover, mutations) -> None:
        self.create_individual = create_individual
        self.fitness = fitness
        self.crossover = crossover
        self.mutations = mutations

    def fit(self):
        
        population_size = 200
        generation = 0
        population = []
        for i in range(population_size):
            individual = self.create_individual()
            population.append(individual)
            
        best_fitness = self.fitness()


        for i, ind in enumerate(population):
            self.fitness(ind)
            