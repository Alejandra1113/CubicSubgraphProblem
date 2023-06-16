import random

def ConnexGraphGenerator():
    n = random.randint(4, 100)
    adjacent_matrix = [[0]*n for _ in range(n)]
    m = random.randint(n-1, (n * (n-1))/2)
    edges = []

    for _ in range(m):
        while True:
            u = random.randint(0, n-1)
            v = random.randint(0, n-1)
            if u != v and not adjacent_matrix[u][v]:
                adjacent_matrix[u][v] = 1
                adjacent_matrix[v][u] = 1
                edges.append((u,v))
                break

    added_edges = BFS_CCheck(n, adjacent_matrix)
    return n, edges + added_edges


def BFS_CCheck(n,adjacent_matrix):

    queue = [0]
    visited = [0] * n
    visited[0] = 1
    edges_list = []
    
    while True:    
        while queue:
            v = queue.pop(0)
            for u in range(n):
                if not visited[u] and adjacent_matrix[u][v]:
                    visited[u] = 1
                    queue.append(u)

        try:
            u = visited.index(0)
            v = random.choice(list(filter(lambda x: visited[x] ==1, range(n) )))
            queue.append(u)
            visited[u] = 1
            edges_list.append((u,v))
            mp +=1
        except:
            break

    return edges_list

    

n, edges = ConnexGraphGenerator()
print(n)
