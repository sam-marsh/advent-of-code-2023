from matplotlib import pyplot as plt
from advent_of_code_2023.utils import read_input
import networkx as nx


def solve(lines: list[str]):
    nodes = set()
    edges = set()
    for line in lines:
        parts = line.strip().split(': ')
        source = parts[0]
        nodes.add(source)
        for x in parts[1].split(' '):
            nodes.add(x)
            edges.add((source, x))

    graph = nx.Graph()
    for n in nodes:
        graph.add_node(n)
    for e in edges:
        graph.add_edge(*e)
    
    # nx.draw(graph, with_labels=True)
    print(nx.minimum_edge_cut(graph))
    for e in nx.minimum_edge_cut(graph):
        graph.remove_edge(*e)
    res = list(nx.connected_components(graph))
    return len(res[0]) * len(res[1])
    # plt.show()


if __name__ == "__main__":
    print(solve(read_input(day=25)))