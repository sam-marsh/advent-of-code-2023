import functools

from advent_of_code_2023.utils import read_input


@functools.lru_cache(maxsize=None)
def num_arrangements(arrangement: str, counts: tuple[int, ...]):
    if '?' not in arrangement:
        a_counts = tuple(len(x) for x in arrangement.split(".") if x != '')
        return 1 if a_counts == counts else 0
    new_arrangement_working = arrangement.replace('?', '.', 1)
    new_arrangement_broken = arrangement.replace('?', '#', 1)
    return num_arrangements(new_arrangement_working, counts) + num_arrangements(new_arrangement_broken, counts)

def solve(lines: list[str]) -> int:
    s = 0
    for line in lines:
        split = line.strip().split(' ')
        arrangement = split[0]
        counts = tuple(int(x) for x in split[1].split(","))
        s += num_arrangements(arrangement, counts)
    return s

if __name__ == "__main__":
    print(solve(read_input(day=12)))