from itertools import combinations
from matplotlib import pyplot as plt
import numpy as np
from advent_of_code_2023.utils import read_input
import networkx as nx


def solve(lines: list[str]) -> int:
    lines = [line.strip() for line in lines]
    sep = lines.index('')
    workflow_lines = lines[:sep]
    part_lines = lines[sep+1:]
    parts = []
    workflows = {}
    for workflow_line in workflow_lines:
        workflow_line = workflow_line.split("{")
        name = workflow_line[0]
        rules = []
        for check in workflow_line[1][:-1].split(","):
            if ':' in check:
                condstr, section = check.split(':')
                if '>' in condstr:
                    var, val = condstr.split(">")
                    val = int(val)
                    condition = (var,">", val)
                else:
                    var, val = condstr.split("<")
                    val = int(val)
                    condition = (var,"<", val)
            else:
                condition = ('x',">",0)
                section = check
            rules.append((condition, section))
        workflows[name] = rules
    
    # x > 10
    # x < 11
    def negate(rule):
        return (rule[0], ">" if rule[1] == '<' else "<", rule[2] + 1 if rule[1] == ">" else rule[2] - 1)
    
    graph = nx.MultiDiGraph()
    for name in workflows:
        prev = []
        for rule in workflows[name]:
            graph.add_edge(name, rule[-1], cond=prev + [rule[0]])
            prev.append(negate(rule[0]))

    all_bounds = []

    def count_possibilities(b):
        for a in b.values():
            if a[1] < a[0]:
                return 0
        return np.prod([x[1] - x[0] + 1 for x in b.values()])

    total = 0
    for path in nx.all_simple_edge_paths(graph, "in", "A"):
        bounds = {v: [1, 4000] for v in ('x', 'm', 'a', 's')}
        
        for u, v, k in path:
            for rating, relation, value in graph[u][v][k]["cond"]:
                if relation == '>':
                    bounds[rating][0] = max(bounds[rating][0], value + 1)
                else:
                    bounds[rating][1] = min(bounds[rating][1], value - 1)

        total += count_possibilities(bounds)
        all_bounds.append(bounds)

    return total

print(solve(read_input(day=19)))