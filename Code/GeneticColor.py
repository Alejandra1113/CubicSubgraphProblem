import random
import numpy as np
import matplotlib.pyplot as plt

def create_individual(n, number_of_colors):
    individual = []
    for i in range(n):
        individual.append(random.randint(1, number_of_colors))
    return individual

def fitness(graph, individual, n):
    fitness = 0
    for i in range(n):
        for j in range(i, n):
            if(individual[i] == individual[j] and graph[i][j] == 1):
                fitness += 1
    return fitness

def crossover(parent1, parent2, n):
    position = random.randint(2, n-2)
    child1 = []
    child2 = []
    for i in range(position+1):
        child1.append(parent1[i])
        child2.append(parent2[i])
    for i in range(position+1, n):
        child1.append(parent2[i])
        child2.append(parent1[i])
    return child1, child2

def mutation1(individual, n, number_of_colors):
    probability = 0.4
    check = random.uniform(0, 1)
    if(check <= probability):
        position = random.randint(0, n-1)
        individual[position] = random.randint(1, number_of_colors)
    return individual

def mutation2(individual, n, number_of_colors):
    probability = 0.2
    check = random.uniform(0, 1)
    if(check <= probability):
        position = random.randint(0, n-1)
        individual[position] = random.randint(1, number_of_colors)
    return individual

def tournament_selection(population, graph, population_size):
    new_population = []
    for j in range(2):
        random.shuffle(population)
        for i in range(0, population_size-1, 2):
            if fitness(graph, population[i], graph.shape[0]) < fitness(graph, population[i+1], graph.shape[0]):
                new_population.append(population[i])
            else:
                new_population.append(population[i+1])
    return new_population

def genetic_coloro(graph):
    Gen = np.array([])
    Fit = np.array([])

    n = graph.shape[0]
    number_of_colors = 3
    '''GA'''
    condition = True    
    while condition:
        '''Create Population'''
        population_size = 200
        generation = 0
        population = []
        for i in range(population_size):
            individual = create_individual(n, number_of_colors)
            population.append(individual)

        best_fitness = fitness(graph, population[0], n)
        fittest_individual = population[0]
        gen = 0
        while(best_fitness != 0 and gen != 3000):
            gen += 1
            population = tournament_selection(population, graph, population_size)
            new_population = []
            random.shuffle(population)
            for i in range(0, population_size-1, 2):
                child1, child2 = crossover(population[i], population[i+1], n)
                new_population.append(child1)
                new_population.append(child2)
            for individual in new_population:
                if(gen < 200):
                    individual = mutation1(individual, n, number_of_colors)
                else:
                    individual = mutation2(individual, n, number_of_colors)
            population = new_population
            best_fitness = fitness(graph, population[0], n)
            fittest_individual = population[0]
            for individual in population:
                if(fitness(graph, individual, n) < best_fitness):
                    best_fitness = fitness(graph, individual, n)
                    fittest_individual = individual
            if gen % 500 == 0:
                print("Generation: ", gen, "Best_Fitness: ",
                    best_fitness, "Individual: ", fittest_individual)
            Gen = np.append(Gen, gen)
            Fit = np.append(Fit, best_fitness)
            
        print("Using ", number_of_colors, " colors : ")
        print("Generation: ", gen, "Best_Fitness: ",
            best_fitness, "Individual: ", fittest_individual)
        print("\n\n")
        if(best_fitness != 0):
            return False
        else:
            return True
    return False

