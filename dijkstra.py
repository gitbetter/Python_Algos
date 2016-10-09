## Simple and quick implementation of Dijkstra's shortest path graph algorithm
## withouth using a heap

def shortest_paths(g):
    nodes = g.keys()
    seen = [nodes[0]] 
    sp_length = {nodes[0]: 0}

    for v in seen:
        for edge in g[v]:
            w, length = edge
            path_length = sp_length[v] + length
            if w not in seen or path_length < sp_length[w]:
                sp_length[w] = path_length 
                seen.append(w)

    return sp_length
            

if __name__ == "__main__":
    graph = {}
    with open("dijkstraData.txt") as f:
        lines = f.readlines()
        for line in lines:
            data = line.split()
            graph[int(data[0])] = []
            for i in range(1, len(data)):
                edge_data = [int(x) for x in data[i].split(",")]
                graph[int(data[0])].append((edge_data[0], edge_data[1]))

    print(shortest_paths(graph))
