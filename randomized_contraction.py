import random, copy

def karger_min_cut(g):
    while len(g) > 2:
        v, w = chooseRandomEdge(g)
        contract(g, v, w)
    
    return len(g[list(g.keys())[0]])

def chooseRandomEdge(g):
    v = random.choice(list(g.keys()))
    w = random.choice(g[v])
    return v, w

def contract(g, v, w):
    # Fuse the two vertices into one
    g[v].extend(g[w])

    # replace references to w with v
    for n in g[w]:
        g[n].remove(w)
        g[n].append(v)

    # remove self loops for vertex v
    while v in g[v]:
        g[v].remove(v)

    del g[w]

if __name__ == '__main__':
    graph = {}
    for line in open("kargerMinCut.txt"):
        node = int(line.split()[0])
        graph[node] = [int(x) for x in line.split()[1:]]

    trials = 100
    cuts = []
    for i in range(trials):
        random.seed()
        copiedGraph = copy.deepcopy(graph)
        mincut = karger_min_cut(copiedGraph)
        cuts.append(mincut)
    
    print(cuts)
    print("Min. cut: " + str(min(cuts)))
