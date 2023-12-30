import pprint
import sys
import numpy as np

from advent_of_code_2023.utils import read_input

direction_map = {
    '|': [(1, 0), (-1, 0)],
    '-': [(0, 1), (0, -1)],
    'L': [(-1, 0), (0, 1)],
    '7': [(0, -1), (1, 0)],
    'F': [(1, 0), (0, 1)],
    'J': [(0, -1), (-1, 0)]
}

def find_animal(grid: np.ndarray[str]) -> tuple[int, int]:
    return tuple(np.array(np.where(grid == 'S')).flatten())

def in_grid(grid: np.ndarray[str], coord: tuple[int, int]):
    return 0 <= coord[0] < grid.shape[0] and 0 <= coord[1] < grid.shape[1]

def parse_grid(lines: list[str]) -> int:
    grid = np.array([list(line.strip()) for line in lines], dtype=str)
    cleaned = np.full(shape=(len(grid), len(grid[0])), fill_value='.', dtype=str)
    upscaled = np.zeros(shape=(3*cleaned.shape[0], 3 * cleaned.shape[1]), dtype=bool)
    animal_coord = find_animal(grid)
    cleaned[*animal_coord] = 'S'
    previous_coord = animal_coord
    valid_directions = []
    for direction in (0, 1), (1, 0), (0, -1), (-1, 0):
        new_pos = tuple(previous_coord + np.array(direction))
        if in_grid(grid, new_pos) and grid[*new_pos] != '.':
            try:
                direction = next(d for d in direction_map[grid[*new_pos]] if tuple(new_pos + np.array(d)) == animal_coord)
                current_coord = new_pos
                valid_directions.append((-direction[0], -direction[1]))
            except:
                pass
    correct_shape = None
    for shape, direction in direction_map.items():
        if direction[0] in valid_directions and direction[1] in valid_directions:
            correct_shape = shape
            break
    cleaned[*animal_coord] = correct_shape
    while not np.all(current_coord == animal_coord):
        cleaned[*current_coord] = grid[*current_coord]
        direction = next(d for d in direction_map[grid[*current_coord]] if tuple(current_coord + np.array(d)) != previous_coord)
        new_pos = tuple(current_coord + np.array(direction))
        previous_coord = current_coord
        current_coord = new_pos
        
    for i in range(len(cleaned)):
        for j in range(len(cleaned[0])):
            if cleaned[i, j] == '|':
                upscaled[3 * i + 1, 3 * j + 1] = upscaled[3 * i, 3 * j + 1] = upscaled[3 * i + 2, 3 * j + 1] = True
            elif cleaned[i, j] == '-':
                upscaled[3 * i + 1, 3 * j + 1] = upscaled[3 * i + 1, 3 * j] = upscaled[3 * i + 1, 3 * j + 2] = True
            elif cleaned[i, j] == 'L':
                upscaled[3 * i + 1, 3 * j + 1] = upscaled[3 * i, 3 * j + 1] = upscaled[3 * i + 1, 3 * j + 2] = True
            elif cleaned[i, j] == '7':
                upscaled[3 * i + 1, 3 * j + 1] = upscaled[3 * i + 1, 3 * j] = upscaled[3 * i + 2, 3 * j + 1] = True
            elif cleaned[i, j] == 'F':
                upscaled[3 * i + 1, 3 * j + 1] = upscaled[3 * i + 2, 3 * j + 1] = upscaled[3 * i + 1, 3 * j + 2] = True
            elif cleaned[i, j] == 'J':
                upscaled[3 * i + 1, 3 * j + 1] = upscaled[3 * i, 3 * j + 1] = upscaled[3 * i + 1, 3 * j] = True

    np.set_printoptions(threshold=10000000, linewidth=1000000)
    print(cleaned)

    print(upscaled.astype(int))

    explore(upscaled, (0, 0))
    np.set_printoptions(threshold=10000000, linewidth=1000000)
    print(upscaled.astype(int))

    count_zero = 0
    for i in range(len(cleaned)):
        for j in range(len(cleaned[0])):
            if np.all(1 - upscaled[np.ix_(range(3 * i - 1, 3 * i + 2), range(3 * j - 1, 3 * j + 2))]):
                count_zero += 1

    return count_zero


def explore(occupied, coord):
    todo = [coord]
    while todo:
        curr = todo.pop()
        occupied[*curr] = True
        for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_pos = (curr[0] + direction[0], curr[1] + direction[1])
            if not in_grid(occupied, new_pos):
                continue
            if occupied[new_pos]:
                continue
            todo.append(new_pos)


if __name__ == '__main__':
    print(parse_grid(read_input(day=10)))