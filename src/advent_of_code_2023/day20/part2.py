from math import lcm
from matplotlib import pyplot as plt
from advent_of_code_2023.utils import read_input
import networkx as nx

def reset(graph: nx.DiGraph):
    for node, data in graph.nodes(data=True):
        if 'type' not in data:
            data['type'] = None
        if 'state' not in data:
            data['state'] = None
        if data['type'] == 'flip-flop':
            data['state'] = 0 # off
        if data['type'] == 'conjunction':
            data['state'] = {
                incoming: 0 for incoming, _ in graph.in_edges(node)
            }

def transmit_pulse(graph: nx.DiGraph, target, target_pulse) -> int:
    actions = [('button', 'broadcaster', 0)]
    counts = [0, 0]
    while actions:
        parent, node, pulse = actions.pop(0)
        if node == target and pulse == target_pulse:
            raise ValueError()
        counts[pulse] += 1
        data = graph.nodes[node]
        # print(parent, pulse, node)#, data['type'], data['state'])
        if data['type'] == 'broadcaster':
            for _, outgoing in graph.out_edges(node):
                actions.append((node, outgoing, pulse))
        if data['type'] == 'flip-flop':
            if pulse == 0:
                data['state'] = 1 - data['state']
                for _, outgoing in graph.out_edges(node):
                    actions.append((node, outgoing, data['state']))
        if data['type'] == 'conjunction':
            data['state'][parent] = pulse
            pulse_to_send = 0 if all(x == 1 for x in data['state'].values()) else 1
            for _, outgoing in graph.out_edges(node):
                actions.append((node, outgoing, pulse_to_send))
    return counts

def solve(lines: list[str]) -> int:
    graph = nx.DiGraph()
    for line in lines:
        name, connections = line.strip().split(" -> ")
        if name[0] == '%':
            type = 'flip-flop'
            name = name[1:]
        elif name[0] == '&':
            type = 'conjunction'
            name = name[1:]
        elif name == 'broadcaster':
            type = name
        connections = connections.split(', ')
        graph.add_node(name, type=type)
        for c in connections:
            graph.add_edge(name, c)
    
    nx.draw(graph, with_labels=True)
    plt.show()

    print(graph.nodes['kz'])
    counts = []
    for node, _ in graph.in_edges('kz'):
        reset(graph)
        count = 0
        while True:
            count += 1
            try:
                transmit_pulse(graph, node, 0)
            except ValueError:
                break
        
        counts.append(count)
        print(node, count)

    return lcm(*counts)



print(solve(read_input(day=20)))