import numpy as np
from advent_of_code_2023.utils import read_input

def decompose(input: np.ndarray) -> int:
    if np.all(input == 0):
        return 0
    return input[-1] + decompose(input[1:] - input[:-1])

def solve(lines: list[str]) -> int:
    return sum(decompose(np.array([int(x) for x in line.strip().split(" ")])) for line in lines)


if __name__ == "__main__":
    print(solve(read_input(day=9)))