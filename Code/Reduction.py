import numpy as np

def Reduction(n, edges):
    adjacent_matrix = [[0] * n for _ in range(n)]

    for u,v in edges:
        adjacent_matrix[u][v] = 1
        adjacent_matrix[v][u] = 1
    
    degree = np.sum(adjacent_matrix, axis= 0)
    adjacent_list = {}
    for i in range(n):
        adjacent_list = CreateCycle(degree[i], i, 1, adjacent_list)
        adjacent_list = CreateCycle(degree[i], i, 2, adjacent_list)
        adjacent_list = CreateCycle(degree[i], i, 3, adjacent_list)

    for j in range(len(edges)):
        adjacent_list = CreatePseudoK4D(j, 1, adjacent_list)
        adjacent_list = CreatePseudoK4D(j, 2, adjacent_list)
        adjacent_list = CreatePseudoK4D(j, 3, adjacent_list)

    for j,(u,v) in enumerate(edges):
        adjacent_list = ConnectCtoD(1, u, v, j, degree[u], degree[v], adjacent_list)
        adjacent_list = ConnectCtoD(2, u, v, j, degree[u], degree[v], adjacent_list)
        adjacent_list = ConnectCtoD(3, u, v, j, degree[u], degree[v], adjacent_list)        
    
    for i in range(n):
        adjacent_list = CreatePseudoK4U(i, adjacent_list)
        adjacent_list = CreatePseudoK4U(i, adjacent_list)
        adjacent_list = CreatePseudoK4U(i, adjacent_list)
        adjacent_list = ConnectUtoW(i, degree[i], adjacent_list)
    
    adjacent_list = CreateFinalCycle(n, adjacent_list)
    adjacent_list = ConnectFinalCycle(n, adjacent_list)

    n = len(adjacent_list)
    edges = []
    adjacent_matrix = [[0] * n for _ in range(n)]
    numbers = dict([(y,x) for (x,y) in enumerate(adjacent_list)])

    for u, y in adjacent_list.items():
        for v in y:
            vi = numbers[v]
            ui = numbers[u]
            if not adjacent_matrix[ui][vi]:
                edges.append((vi,ui))
                adjacent_matrix[ui][vi] = 1
                adjacent_matrix[vi][ui] = 1

    return n, edges



def CreateCycle(deg,i,h, adjacent_list):

    len_cycle = 2*deg +1 

    for j in range(1,len_cycle-1):
        p = j-1
        n = j+1
        adjacent_list[f'c_{i}{j}^{h}'] = [f'c_{i}{p}^{h}', f'c_{i}{n}^{h}']
    
    len_cycle -=1
    adjacent_list[f'c_{i}{0}^{h}'] = [f'c_{i}{len_cycle}^{h}', f'c_{i}{1}^{h}']
    p = len_cycle -1
    adjacent_list[f'c_{i}{len_cycle}^{h}'] = [f'c_{i}{p}^{h}', f'c_{i}{0}^{h}']
    
    return adjacent_list
        
def CreatePseudoK4D(j,h, adjacent_list):
    
    adjacent_list[f'd_{j}1^{h}'] = [f'd_{j}2^{h}',f'x_{j}^{h}', f'y_{j}^{h}']
    adjacent_list[f'd_{j}2^{h}'] = [f'd_{j}1^{h}',f'x_{j}^{h}', f'y_{j}^{h}']
    adjacent_list[f'x_{j}^{h}'] = [f'd_{j}2^{h}',f'd_{j}1^{h}']
    adjacent_list[f'y_{j}^{h}'] = [f'd_{j}2^{h}',f'd_{j}1^{h}']
    return adjacent_list

def ConnectCtoD(h,s,t,j,degs, degt,adjacent_list):
    len_cycles = 2*degs +1 
    
    len_cyclet = 2*degt +1 
    X = f'x_{j}^{h}'
    Y = f'y_{j}^{h}'
    for i in range(len_cycles):
        if len(adjacent_list[f'c_{s}{i}^{h}']) ==2:
            adjacent_list[f'c_{s}{i}^{h}'] += [X]
            adjacent_list[X] += [f'c_{s}{i}^{h}']
            break
    
    for i in range(len_cycles):
        if len(adjacent_list[f'c_{s}{i}^{h}']) ==2:
            adjacent_list[f'c_{s}{i}^{h}'] += [Y]
            adjacent_list[Y] += [f'c_{s}{i}^{h}']
            break
    
    for i in range(len_cyclet):
        if len(adjacent_list[f'c_{t}{i}^{h}']) ==2:
            adjacent_list[f'c_{t}{i}^{h}'] += [X]
            adjacent_list[X] += [f'c_{t}{i}^{h}']
            break
    
    for i in range(len_cyclet):
        if len(adjacent_list[f'c_{t}{i}^{h}']) ==2:
            adjacent_list[f'c_{t}{i}^{h}'] += [Y]
            adjacent_list[Y] += [f'c_{t}{i}^{h}']
            break
    return adjacent_list

def CreatePseudoK4U(i, adjacent_list): 
    
    adjacent_list[f'u_{i}1'] = [f'u_{i}2',f'x_{i}', f'y_{i}']
    adjacent_list[f'u_{i}2'] = [f'u_{i}1',f'x_{i}', f'y_{i}']
    adjacent_list[f'x_{i}'] = [f'u_{i}2',f'u_{i}1', f'u_{i}']
    adjacent_list[f'u_{i}'] = [f'x_{i}']
    adjacent_list[f'y_{i}'] = [f'u_{i}2',f'u_{i}1']
    return adjacent_list    

def ConnectUtoW(i,deg, adjacent_list):
    
    len_cycle = 2*deg +1 
    
    for j in range(len_cycle):
    
        if len(adjacent_list[f'c_{i}{j}^{1}']) ==2:
            adjacent_list[f'c_{i}{j}^{1}'] += [f'u_{i}']
            adjacent_list[f'u_{i}'] += [f'c_{i}{j}^{1}']
        
        if len(adjacent_list[f'c_{i}{j}^{2}']) ==2:
            adjacent_list[f'c_{i}{j}^{2}'] += [f'y_{i}']
            adjacent_list[f'y_{i}'] += [f'c_{i}{j}^{2}']
        
        if len(adjacent_list[f'c_{i}{j}^{3}']) ==2:
            adjacent_list[f'c_{i}{j}^{3}'] += [f'y_{i}']
            adjacent_list[f'y_{i}'] += [f'c_{i}{j}^{3}']
    
    return adjacent_list
            
def CreateFinalCycle(n, adjacent_list):
    
    for j in range(1,n-1):
        p = j-1
        x = j+1
        adjacent_list[f'a_{1}{j}'] = [f'a_{1}{p}', f'a_{1}{x}']
        adjacent_list[f'a_{2}{j}'] = [f'a_{2}{p}', f'a_{2}{x}']
    
    n-=1
    adjacent_list[f'a_{1}{0}'] = [f'a_{2}{n}', f'a_{1}{1}']
    adjacent_list[f'a_{2}{0}'] = [f'a_{1}{n}', f'a_{2}{1}']
    p = n -1
    adjacent_list[f'a_{2}{n}'] = [f'a_{2}{p}', f'a_{1}{0}']
    adjacent_list[f'a_{1}{n}'] = [f'a_{1}{p}', f'a_{2}{0}']
    
    return adjacent_list

def ConnectFinalCycle(n,adjacent_list):
    for j in range(n):
        adjacent_list[f'a_{1}{j}'] += [f'u_{j}'] 
        adjacent_list[f'a_{2}{j}'] += [f'u_{j}']
        adjacent_list[f'u_{j}'] += [f'a_{1}{j}', f'a_{2}{j}'] 
       
    return adjacent_list


Reduction(3, [(0,1),(1,2)])