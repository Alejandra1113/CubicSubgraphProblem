
def ThreeColorable(n, edges):
    adjacent_matrix = [[0] * n for _ in range(n)]

    for u,v in edges:
        adjacent_matrix[u][v] = 1
        adjacent_matrix[v][u] = 1
    
    set_A = [0]
    set_B = []
    set_C = []

    return ThreeColorableBacktrack(n,set_A,set_B,set_C, adjacent_matrix, 1)

def ThreeColorableBacktrack(n,set_A,set_B,set_C, adjacent_matrix, index):
    if index == n:
        return Void(set_A, adjacent_matrix) and Void(set_B, adjacent_matrix) and Void(set_C, adjacent_matrix)
    
    set_A.append(index)
    A = ThreeColorableBacktrack(n, set_A, set_B, set_C, adjacent_matrix, index+1)
    if A: return True
    set_A.pop()
    set_B.append(index)
    B = ThreeColorableBacktrack(n, set_A, set_B, set_C, adjacent_matrix, index+1)
    if B: return True
    set_B.pop()
    set_C.append(index)
    return ThreeColorableBacktrack(n, set_A, set_B, set_C, adjacent_matrix, index+1)

def Void(set_X, adjacent_matrix):
    for u in set_X:
        for v in set_X:
            if  adjacent_matrix[u][v]: return False

    return True


