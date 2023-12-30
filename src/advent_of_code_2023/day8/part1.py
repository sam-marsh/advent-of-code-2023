from matplotlib import pyplot as plt
from advent_of_code_2023.utils import read_input
import networkx as nx


def solve(lines: list[str]) -> int:
    directions = list(lines[0].strip())
    graph = nx.MultiDiGraph()
    
    for line in lines[2:]:
        split = line.strip().split(' = (')
        split2 = split[1].split(", ")
        graph.add_edge(split[0], split2[0], direction="L")
        graph.add_edge(split[0], split2[1][:-1], direction="R")
    
    nx.draw(graph, with_labels=True)
    plt.show()
    current_node = 'AAA'
    current_index = 0
    print(graph.out_edges('QCL', data=True))
    while current_node != 'ZZZ':
        print(current_node)
        current_direction = directions[current_index % len(directions)]
        found = False
        for u, v, data in graph.out_edges(current_node, data=True):
            if data["direction"] == current_direction:
                current_node = v
                current_index += 1
                found = True
                break
        if not found:
            raise AssertionError()


    return current_index

if __name__ == "__main__":
    print(solve(read_input(day=8)))