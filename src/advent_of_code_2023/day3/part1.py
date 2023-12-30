import numpy as np
from advent_of_code_2023.utils import read_input

def in_grid(grid, coord):
    return 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0])

def num_digits(n):
    if n == 0:
        return 0
    return 1 + num_digits(n // 10)

def adjacent_to_symbol(symbols, coord):
    for symbol_coord in symbols:
        if max(abs(symbol_coord[0] - coord[0]), abs(symbol_coord[1] - coord[1])) <= 1:
            return True
    return False

def sum_schematic(lines: list[str]):
    grid = np.array([list(line.strip()) for line in lines], dtype=str)
    symbols = set()
    numbers = {}
    current_number = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i, j].isdigit():
                current_number = 10 * current_number + int(grid[i, j])
            else:
                if current_number != 0:
                    numbers[(i, j - num_digits(current_number))] = current_number
                    current_number = 0
                if not grid[i, j].isdigit() and grid[i, j] != '.':
                    symbols.add((i, j))
        if current_number != 0:
            numbers[(i, j - num_digits(current_number) + 1)] = current_number
            current_number = 0

    s = 0
    for number_coord, number in numbers.items():
        for j_coord in range(number_coord[1], number_coord[1] + num_digits(number)):
            if adjacent_to_symbol(symbols, (number_coord[0], j_coord)):
                s += number
                break
    
    return s

if __name__ == "__main__":
    print(sum_schematic(read_input(day=3)))