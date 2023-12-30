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
    try:
        grid[coord]
        return True
    except:
        return False

def parse_grid(lines: list[str]) -> int:
    grid = np.array([list(line.strip()) for line in lines], dtype=str)
    animal_coord = find_animal(grid)
    print(animal_coord, grid[*animal_coord])
    previous_coord = animal_coord
    for direction in (0, 1), (1, 0), (0, -1), (-1, 0):
        new_pos = tuple(previous_coord + np.array(direction))
        if in_grid(grid, new_pos) and grid[*new_pos] != '.':
            try:
                direction = next(d for d in direction_map[grid[*new_pos]] if tuple(new_pos + np.array(d)) == animal_coord)
                current_coord = new_pos
                print(f'Found {grid[*new_pos]} at {new_pos}!')
                break
            except:
                pass
    length = 1
    while not np.all(current_coord == animal_coord):
        direction = next(d for d in direction_map[grid[*current_coord]] if tuple(current_coord + np.array(d)) != previous_coord)
        new_pos = tuple(current_coord + np.array(direction))
        previous_coord = current_coord
        current_coord = new_pos
        print(f'Found {grid[*new_pos]} at {new_pos}')
        length += 1
    return length // 2



if __name__ == '__main__':
    print(parse_grid(read_input(day=10)))