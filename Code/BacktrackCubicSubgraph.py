def CubicSubgraph(n, edges):
    degrees = [0] * n 
    for x,y in edges:
        degrees[x]+=1
        degrees[y]+=1

    return BacktrackCubicSubgraph(edges, degrees, 0)

#Backtack puro y duro que genera todos los casos
def BacktrackCubicSubgraph(edges, degrees, index):
    if index == len(edges):
        return all([x == 0 or x == 3 for x in degrees]) and any([x>0 for x in degrees])

    if BacktrackCubicSubgraph(edges, degrees, index + 1): return True
    x,y = edges[index]
    
    degrees[x]-=1 
    degrees[y]-=1

    return BacktrackCubicSubgraph(edges, degrees, index +1)

#Backtrack que poda en cuanto las aristas se pasan del degree
def BacktrackCubicS(edges, degrees, index):
    if index == len(edges):
        return all([x == 0 or x == 3 for x in degrees]) and any([x>0 for x in degrees])

    x,y = edges[index]
    if degrees[x] < 3 and degrees[y]< 3:
        degrees[x] += 1 
        degrees[y] += 1

        if BacktrackCubicS(edges, degrees, index + 1): return True
        
        degrees[x] -= 1 
        degrees[y] -= 1
        return BacktrackCubicS(edges, degrees, index +1)
    
    return False


#K5
print(BacktrackCubicS([(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)], [0]*5, 0))

#Petersen
print(BacktrackCubicS([(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,1),(1,0),(0,4),(0,7),(3,6),(5,9),(2,8)], [0]*10, 0))