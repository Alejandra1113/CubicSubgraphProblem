def CubicSubgraph(n, edges):
    degrees = [0] * n 
    for x,y in edges:
        degrees[x]+=1
        degrees[y]+=1

    return BacktrackCubicSubgraph(edges, degrees, 0)

    
def BacktrackCubicSubgraph(edges, degrees, index):
    if index == len(edges):
        return all([x == 0 or x == 3 for x in degrees]) and any([x>0 for x in degrees])

    if BacktrackCubicSubgraph(edges, degrees, index + 1): return True
    x,y = edges[index]
    
    degrees[x]-=1 
    degrees[y]-=1

    return BacktrackCubicSubgraph(edges, degrees, index +1)


print(CubicSubgraph(5, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]))