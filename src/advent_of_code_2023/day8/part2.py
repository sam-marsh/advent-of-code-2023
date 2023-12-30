from math import lcm
from matplotlib import pyplot as plt
import numpy as np
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

    loop_start_index = []
    all_visited = []

    for node in graph.nodes():
        if node[-1] == 'A':
            index = 0
            visited = []
            current = node
            while True:
                if (current, index % len(directions)) in visited:
                    loop_start_index.append(visited.index((current, index % len(directions))))
                    break
                visited.append((current, index % len(directions)))
                current = next(v for (_, v, data) in graph.out_edges(current, data=True) if data['direction'] == directions[index % len(directions)])
                index += 1
            all_visited.append(visited)
    
    for visited, start in zip(all_visited, loop_start_index):
        print([idx for idx, x in enumerate(visited) if x[0][-1] == 'Z'])
        print(len(visited[start:]))
        # observed: the distance to the only Z in the loop exactly matches
        # the length of the loop for every start point
        # so we can use LCM to sync them up in this specific case
        
    return lcm(*(len(visited[start:]) for visited, start in zip(all_visited, loop_start_index)))

if __name__ == "__main__":
    print(solve(read_input(day=8)))