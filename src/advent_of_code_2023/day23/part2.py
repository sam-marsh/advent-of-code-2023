from itertools import combinations
from matplotlib import pyplot as plt
import networkx as nx
import numpy as np

from advent_of_code_2023.utils import read_input

dir_map = {
    '.': [(0, 1), (1, 0), (0, -1), (-1, 0)],
    '>': [(0, 1), (1, 0), (0, -1), (-1, 0)],
    'v': [(0, 1), (1, 0), (0, -1), (-1, 0)],
    '<': [(0, 1), (1, 0), (0, -1), (-1, 0)],
    '^': [(0, 1), (1, 0), (0, -1), (-1, 0)]
}

def valid_index(lines, i, j):
    return 0 <= i < len(lines) and 0 <= j < len(lines[0])
    
def solve(lines: list[str]):
    lines = [line.strip() for line in lines]

    graph = nx.Graph()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] in dir_map:
                graph.add_node((i, j))
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] not in dir_map:
                continue
            for di, dj in dir_map[lines[i][j]]:
                if not valid_index(lines, i + di, j + dj):
                    continue
                if lines[i + di][j + dj] in dir_map:
                    graph.add_edge((i, j), (i + di, j + dj), weight=1)

    important_nodes = set(node for node in graph.nodes() if nx.degree(graph, node) != 2)

    while True:
        didsomething = False
        for node in graph.nodes():
            neighbours = list(nx.neighbors(graph, node))
            if len(neighbours) == 2:
                graph.add_edge(neighbours[0], neighbours[1], weight=graph[node][neighbours[0]]["weight"]+graph[node][neighbours[1]]["weight"])
                graph.remove_node(node)
                didsomething = True
                break
        if not didsomething:
            break
        
    pos = dict(zip(graph.nodes(), [(j, -i) for (i, j) in graph.nodes()]))
    nx.draw(graph, pos, node_size=1)
    nx.draw_networkx_edge_labels(graph, pos, nx.get_edge_attributes(graph, 'weight'))
    plt.show()

    terminal_nodes = [node for node in graph.nodes() if nx.degree(graph, node) == 1]
    print(terminal_nodes)

    return max(
        nx.path_weight(graph, x, "weight")
        for x in nx.all_simple_paths(graph, *terminal_nodes)
    )


if __name__ == "__main__":
    print(solve(read_input(day=23)))