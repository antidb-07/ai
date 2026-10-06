print("Dharmik Bosamia")
print("53013240021")
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('A', 2), ('C', 1), ('G', 9)],
    'C': [('B', 1)],
    'D': [('E', 6), ('G', 1)],
    'E': [('A', 3), ('D', 6), ('F', 5)],
    'F': [('E', 5), ('G', 2), ('H', 4)],
    'G': [('B', 9), ('D', 1), ('F', 2), ('I', 3)],
    'H': [('F', 4), ('I', 2), ('J', 5)],
    'I': [('G', 3), ('H', 2), ('J', 1)],
    'J': [('H', 5), ('I', 1)]
}


def aStarAlgo(start_node, stop_node):

    open_set = {start_node}
    closed_set = set()

    g = {}
    parents = {}

    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:

        n = min(
            open_set,
            key=lambda node: g[node] + heuristic(node)
        )

        print("Node for expansion --->", n)

        if n == stop_node:

            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)
            path.reverse()

            print("Path found:", path)

            return path
        
        if Graph_nodes.get(n) is None:
            print("Path does not exist!")
            return None

        for m, weight in get_neighbors(n):

            new_cost = g[n] + weight
            if m not in g or new_cost < g[m]:

                g[m] = new_cost
                parents[m] = n

                open_set.add(m)

                print(
                    "Child of", n,
                    "=>", m,
                    "Cost =", g[m],
                    "Heuristic =", heuristic(m),
                    "f(m) =", g[m] + heuristic(m)
                )

        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist!")
    return None



def get_neighbors(v):

    if v in Graph_nodes:
        return Graph_nodes[v]

    return None



def heuristic(n):

    H_dist = {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }

    return H_dist[n]


aStarAlgo('A', 'J')