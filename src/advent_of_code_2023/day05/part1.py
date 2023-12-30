import numpy as np
from advent_of_code_2023.utils import read_input


def lookup(section, item):
    for dest, source, length in section:
        if source <= item < source + length:
            return dest + (item - source)
    return item

def solve(lines: list[str]) -> int:
    lines = [line.strip() for line in lines]
    seeds = [int(x) for x in lines[0].split(' ')[1:]]
    sections = []
    for line in lines[1:]:
        if not line: continue
        if 'map' in line:
            sections.append([])
            continue
        sections[-1].append(tuple(int(x) for x in line.split(' ')))
    
    for i in range(len(sections)):
        sections[i] = sorted(sections[i], key=lambda x: x[1])
    
    lowest = np.inf
    for seed in seeds:
        curr = seed
        for section in sections:
            curr = lookup(section, curr)
        lowest = min(lowest, curr)

    return lowest

if __name__ == "__main__":
    print(solve(read_input(day=5)))