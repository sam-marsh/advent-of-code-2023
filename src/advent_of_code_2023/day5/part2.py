from functools import lru_cache
import numpy as np
from advent_of_code_2023.utils import read_input

def intersection(start1, end1, start2, end2):
    lo = max(start1, start2)
    hi = min(end1, end2)
    return (lo, hi) if lo <= hi else None    

def exclude(start, end, exclude_start, exclude_end):
    to_remove = intersection(start, end, exclude_start, exclude_end)
    if not to_remove:
        return start, end
    first_interval = start, to_remove[0] - 1
    second_interval = to_remove[1] + 1, end
    intervals = []
    if first_interval[0] <= first_interval[1]:
        intervals.append(first_interval)
    if second_interval[0] <= second_interval[1]:
        intervals.append(second_interval)
    return intervals
    
def solve(lines: list[str]) -> int:
    lines = [line.strip() for line in lines]
    seeds = [int(x) for x in lines[0].split(' ')[1:]]

    seed_starts = seeds[::2]
    seed_lengths = seeds[1::2]

    intervals = [(start, start + length - 1) for start, length in zip(seed_starts, seed_lengths)]

    sections = []
    for line in lines[1:]:
        if not line: continue
        if 'map' in line:
            sections.append({})
            continue
        dest, source, length = (int(x) for x in line.split(' '))
        sections[-1][(source, source + length - 1)] = (dest, dest + length - 1)
        
    @lru_cache(maxsize=None)
    def lookup(section_index, interval):
        print(section_index, interval)
        if interval is None:
            return []
        any_intersection = False
        for source, dest in sections[section_index].items():
            overlap = intersection(*interval, *source)
            if not overlap:
                continue
            any_intersection = True
        if not any_intersection:
            return [interval]
        for source, dest in sections[section_index].items():
            overlap = intersection(*interval, *source)
            print(f"intersection of {interval} and {source} is {overlap}")
            if overlap is None:
                continue
            remaining = exclude(*interval, *overlap)
            print(f"remaining of {interval} and {source} is {remaining}")
            print(remaining)
            rest = [(overlap[0] - source[0] + dest[0], overlap[1] - source[0] + dest[0])]
            for sub in remaining:
                rest.extend(lookup(section_index, sub))
            return rest
        raise AssertionError()
    
    min_res = np.inf
    for start_interval in intervals:
        interval_list = [start_interval]
        for i in range(len(sections)):
            mapped = []
            for interval in interval_list:
                mapped.extend(lookup(i, interval))
            interval_list = mapped
            # should probably simplify/merge the intervals here but cba
        min_res = min(min_res, min(x[0] for x in interval_list))

    return min_res

if __name__ == "__main__":
    print(solve(read_input(day=5)))