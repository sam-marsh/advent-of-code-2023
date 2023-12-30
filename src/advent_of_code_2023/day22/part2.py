from itertools import combinations
from matplotlib import pyplot as plt
import numpy as np
from advent_of_code_2023.utils import read_input
from scipy.sparse import coo_array
import networkx as nx

def intersect_1d(s1, s2):
    return max(0, min(s1[1], s2[1]) - max(s1[0], s2[0]) + 1) != 0

def intersect_2d(s1, s2):
    (x1, y1), (x2, y2) = s1
    (x3, y3), (x4, y4) = s2
    return intersect_1d((x1, x2), (x3, x4)) and intersect_1d((y1, y2), (y3, y4))

def intersect_3d(s1, s2):
    (x1, y1, z1), (x2, y2, z2) = s1
    (x3, y3, z3), (x4, y4, z4) = s2
    return intersect_1d((x1, x2), (x3, x4)) and intersect_1d((y1, y2), (y3, y4)) and intersect_1d((z1, z2), (z3, z4))

def get_supports(bricks, relevant, i):
    if bricks[i][0][-1] == 1 or bricks[i][1][-1] == 1:
        return [-1]
    supports = []
    for j in relevant:
        if j != i:
            if intersect_3d(bricks[i] - np.array([(0, 0, 1), (0, 0, 1)]), bricks[j]):
                supports.append(j)
    return supports

def solve(lines: list[str]):
    bricks = []
    for line in lines:
        split = line.strip().split('~')
        start, end = (tuple(int(x) for x in split[i].split(',')) for i in (0, 1))
        bricks.append((start, end))
    # sort by height off the ground
    bricks = np.array(sorted(bricks, key=lambda brick: min(brick[0][-1], brick[1][-1])))

    # map of bricks intersecting in the XY plane
    relevant = {}
    for i in range(len(bricks)):
        sub_relevant = []
        for j in range(len(bricks)):
            if i != j:
                if intersect_2d(bricks[i, :, 0:2], bricks[j, :, 0:2]):
                    sub_relevant.append(j)
        relevant[i] = sub_relevant
    
    graph = nx.DiGraph()
    graph.add_node(-1)

    for i in range(len(bricks)):
        graph.add_node(i)

        supports = get_supports(bricks, relevant[i], i)
        if len(supports) == 0:
            current_z = min(bricks[i, :, -1])
            below = [x for x in relevant[i] if max(bricks[x, :, -1]) < current_z]
            if len(below) == 0:
                bricks[i, :, -1] -= current_z - 1
            else:
                highest_below = max(below, key=lambda x: max(bricks[x, :, -1]))
                below_z = max(bricks[highest_below, :, -1])
                bricks[i, :, -1] -= current_z - below_z - 1
        supports = get_supports(bricks, relevant[i], i)
        for support in supports:
            graph.add_edge(support, i)

    total = 0
    for i in range(len(bricks)):
        c = graph.copy()
        c.remove_node(i)
        paths = [x for x in nx.shortest_path_length(c, -1)]
        total += c.number_of_nodes() - len(paths)
    return total


if __name__ == "__main__":
    print(solve(read_input(day=22)))