import GeneticColor
import GeneticCubic

def check(graph):
    is_colorable = GeneticColor.genetic_coloro(graph)

    edges = []
    for u in range(graph.shape[0]):
        for v in range(u, graph.shape[0]):
            if u == v:
                continue
            edges.append((u,v))

    best_fitness,_,_ = GeneticCubic.genetic_algo(graph)
    if int(best_fitness) == 0:
        is_cubic = True
    else:
        is_cubic = False

    return is_colorable == is_cubic