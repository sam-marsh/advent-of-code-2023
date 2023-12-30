import numpy as np
from advent_of_code_2023.utils import read_input


def count_wins(time, record):
    # th * 0 + (t - th) * th - r = 0
    under = np.sqrt(-4 -4 * record + (time)**2)
    min_th = int(np.ceil((1/2) * (time - under)))
    max_th = int(np.floor((1/2) * (time + under)))
    print(time, record, min_th, max_th, max(0, max_th - min_th + 1))
    return max(0, max_th - min_th + 1)

def solve(lines: list[str]) -> int:
    times = [int(''.join(x for x in lines[0] if x.isdigit()))]
    records = [int(''.join(x for x in lines[1] if x.isdigit()))]
    prod = 1
    for time, record in zip(times, records):
        # print(time, record, count_wins(time, record))
        prod *= count_wins(time, record)
    return prod

if __name__ == "__main__":
    print(solve(read_input(day=6)))