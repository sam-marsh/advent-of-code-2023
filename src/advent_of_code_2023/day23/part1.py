from matplotlib import pyplot as plt
import networkx as nx
import numpy as np

from advent_of_code_2023.utils import read_input

dir_map = {
    '.': [(0, 1), (1, 0), (0, -1), (-1, 0)],
    '>': [(0, 1)],
    'v': [(1, 0)],
    '<': [(0, -1)],
    '^': [(-1, 0)]
}

def valid_index(lines, i, j):
    return 0 <= i < len(lines) and 0 <= j < len(lines[0])

def solve(lines: list[str]):
    lines = [line.strip() for line in lines]

    graph = nx.DiGraph()
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
                    graph.add_edge((i, j), (i + di, j + dj))

    # pos = dict(zip(graph.nodes(), [(j, -i) for (i, j) in graph.nodes()]))
    # nx.draw(graph, pos, node_size=1)

    start_node = min(graph.nodes(), key=lambda n: n[0])
    end_node = max(graph.nodes(), key=lambda n: n[0])
    
    return max(len(x) - 1 for x in nx.all_simple_paths(graph, start_node, end_node))


if __name__ == "__main__":
    print(solve(read_input(day=23)))