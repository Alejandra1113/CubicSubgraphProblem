import random as rand
import numpy as np
import networkx as nx


def gen_random_graph(n):
    G = nx.random_regular_graph(3, n)
    adj = nx.to_numpy_array(G).astype(np.int8)
    for _ in range(rand.randint(n//2,n*(n-1)//2)):
        i = rand.randint(0,n-1)
        j = rand.randint(0,n-1)
        while i==j:
            i = rand.randint(0,n-1)
            j = rand.randint(0,n-1)
        adj[i][j] = adj[j][i] = 1
    return adj

def make_create_individual(graph_base):
    n = graph_base.shape[0]+1
    def create_individual():
        individual = graph_base.copy()
        for i in range(1,n-2):
            for j in range(i,n-2):
                if graph_base[i][j] == 1:
                    individual[i][j] = individual[j][i] = rand.randint(0,1)
        return individual
    return create_individual

def penalty_1(x):
    if x == 0 or x == 3:
        return 0
    elif x == 1 or x == 2:
        return 3
    else:
        return x - 3

def make_fitness_1(graph_base):
    penalty = graph_base.sum()//2
    def fitness(graph):
        if graph.mean() > 4 and graph.max() <= 5:
            return 0
        fit = 0
        degres = graph.sum(axis=0)
        for d in degres:
            fit += penalty_1(d)
        if degres.sum() == 0:
            fit += penalty
        return fit
    return fitness

def penalty_2(x, p):
    if x == 0 or x == 3:
        return 0
    elif x < p :
        return (p-x)*3
    else:
        return (x + 3 - p)/ 3

def make_fitness_2(graph_base):
    penalty = graph_base.sum()//2
    p = max(5, int(graph_base.shape[0] * 0.25))
    print('El valor de P', p)
    def fitness(graph):
        sums = graph.sum(axis=0)
        c = 0
        for s in sums:
            if s > 0:
                c += 1
        if c > 0 and int(sums.sum())/c > 4 and int(sums.max()) <= 5:
            return 0
        if all([s==0 or s==4 for s in sums]) and int(sums.sum()) > 0:
            return 0
        fit = 0
        degres = graph.sum(axis=0)

        for d in degres:
            fit += penalty_2(d,p)
        if degres.sum() == 0:
            fit += penalty
        return fit
    return fitness

def make_crossover(graph_base):
    base_nodes = [i for i in range(graph_base.shape[0])]    
    def crosover(parent1, parent2):
        nodes = base_nodes.copy()
        rand.shuffle(nodes)
        child1 = parent1.copy()
        child2 = parent2.copy()

        point = rand.randint(2,len(base_nodes)-3)
        for i in nodes[:point]:
            for j in nodes[:point]:
                child2[i][j] = child2[j][i] = parent1[i][j]
        for i in nodes[point:]:
            for j in nodes[point:]:
                child1[i][j] = child1[j][i] = parent2[i][j]        
        for i in nodes[:point]:
            for j in nodes[point:]:
                #if parent1[i][j] != parent2[i][j]:
                child1[i][j] = child2[j][i] = 0
                child2[i][j] = child2[j][i] = 0
        for i in range(0,len(nodes)):
            for j in range(i, len(nodes)):
                child1[i][j] = child1[j][i]
                child2[i][j] = child2[j][i]
        return child1, child2
    return crosover

def remove_edge(graph):

    base_nodes = [i for i in range(graph.shape[0])]
    weights = []
    for i, s in enumerate(graph.sum(axis=0)):
        if s > 3:
            weights.append(int(s)-1)
        else:
            weights.append(1)

    node1 = rand.choices(base_nodes,weights, k =1)[0]
    node2 = rand.choices(base_nodes,weights, k =1)[0]
    count_no_mutate = 100
    while graph[node1][node2] == 0 and count_no_mutate > 0 and node1 == node2:
        node1 = rand.choices(base_nodes,weights, k =1)[0]
        node2 = rand.choices(base_nodes,weights, k =1)[0]
        count_no_mutate -= 1
    if count_no_mutate > 0:
        #print(node1, node2)
        graph[node1][node2] = 0
        graph[node2][node1] = 0
    return graph

def create_good_edge(graph_base):
    def create_edge(graph):   

        base_nodes = [i for i in range(graph.shape[0])]
        weights = []
        for i, s in enumerate(graph.sum(axis=0)):
            if s < 3:
                weights.append(3-int(s))
            else:
                weights.append(1)     

        node1 = rand.randint(1, graph.shape[0]-2)
        node2 = rand.randint(1, graph.shape[0]-2)
        count_no_mutate = 100
        while graph[node1][node2] == 1 and graph_base[node1][node2] == 0 and count_no_mutate > 0:
            node1 = rand.randint(1, graph.shape[0]-2)
            node2 = rand.randint(1, graph.shape[0]-2)
            count_no_mutate -= 1
        if count_no_mutate != 0:   
            #print(node1, node2)         
            graph[node1][node2] = 1
            graph[node2][node1] = 1            
        return graph
    return create_edge

def remove_vertex(graph):
    
    # Choose a random vertex to remove
    vertex = rand.randint(0, graph.shape[0]-1)
    # Remove the vertex from the adjacency matrix
    for i in range(0, graph.shape[0]):
        graph[i][vertex] = graph[vertex][i] = 0    
    return graph

def create_good_vertex(graph_base):
    def create_vertex(graph):
        
        # Choose a random vertex to remove
        vertex = rand.randint(0, graph.shape[0]-1)
        # Remove the vertex from the adjacency matrix
        #print(vertex)
        for i in range(0, graph.shape[0]):
            if graph_base[i][vertex] == 1:
                graph[i][vertex] = graph[vertex][i] = 1
        return graph
    return create_vertex

def selection_tournament(population, fitness, ratio):
    best_fit = 9999999999999
    best_sol = None
    selection = []
    for i in range(int(len(population)*ratio)):
        sample = rand.sample(population, 2)
        p1 = sample[0]
        p2 = sample[1]
        f1 = fitness(p1)
        f2 = fitness(p2)
        if f1 < f2:
            selection.append(p1)
            if f1 <= best_fit:
                best_fit = f1
                best_sol = p1
        else:
            selection.append(p2)      
            if f2 <= best_fit:
                best_fit = f2
                best_sol = p2
    return selection, best_fit, best_sol.copy()

def genetic_algo(graph, max_iteration=2000, verbose= False):

    fitness = make_fitness_2(graph)
    crossover = make_crossover(graph)
    create_individual = make_create_individual(graph)
    mutations = [create_good_edge(graph), remove_edge]
    
    population_size = 200
    population = []
    for i in range(population_size):
        individual = create_individual()
        population.append(individual)
    best_fitness = fitness(population[0])
    best_solution = population[0].copy()
    iteration = 0

    time_line = []

    while iteration < max_iteration and best_fitness != 0:
        if verbose and iteration % 100 == 0:
            print('Iteracion ', iteration, best_fitness, '\n', best_solution)
        selected_population, new_best_fitness, new_best_solution = selection_tournament(population, fitness, 0.75)
        if new_best_fitness <= best_fitness:
            best_solution = new_best_solution
            best_fitness = new_best_fitness
        new_population = []   
        
        for i in range(0, len(selected_population), 2):
            c1, c2 = crossover(selected_population[i], selected_population[i+1])
            new_population.append(c1)
            new_population.append(c2)
              

        for i in range(int(len(population)//2)):
            mutation = rand.choice(mutations)
            ind_random = rand.choice(new_population)
            mutation(ind_random)

        for i in range(population_size - len(new_population)):
            new_population.append(create_individual())
        
        population =  new_population
        iteration += 1
        time_line.append(best_fitness)
        
    return best_fitness, best_solution, time_line

