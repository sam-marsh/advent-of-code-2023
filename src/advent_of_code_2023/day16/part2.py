import numpy as np
from advent_of_code_2023.utils import read_input

RIGHT = np.array([0, 1])
UP = np.array([-1, 0])
LEFT = np.array([0, -1])
DOWN = np.array([1, 0])

def solve(lines: list[str]) -> int:
    data = np.array([list(x.strip()) for x in lines])

    starting_locations = []
    for i in range(len(data)):
        starting_locations.append((np.array([i, 0]), RIGHT))
        starting_locations.append((np.array([i, len(data[0])-1]), LEFT))
    for j in range(len(data[0])):
        starting_locations.append((np.array([0, j]), DOWN))
        starting_locations.append((np.array([len(data)-1, j]), LEFT))

    best = 0
    counter = 0
    for start in starting_locations:
        counter += 1
        print(counter,"of",len(starting_locations))
        visited = set()
        
        todo = [start]

        while todo:
            position, direction = todo.pop()
            if position[0] < 0 or position[0] >= len(data) or position[1] < 0 or position[1] >= len(data[0]):
                continue
            if (tuple(position), tuple(direction)) in visited:
                continue
            visited.add((tuple(position), tuple(direction)))
            tile = data[*position]
            if tile == '.':
                todo.append((position + direction, direction))
            elif tile == '/':
                if np.all(direction == RIGHT):
                    todo.append((position + UP, UP))
                elif np.all(direction == UP):
                    todo.append((position + RIGHT, RIGHT))
                elif np.all(direction == LEFT):
                    todo.append((position + DOWN, DOWN))
                elif np.all(direction == DOWN):
                    todo.append((position + LEFT, LEFT))
                else:
                    raise AssertionError()
            elif tile == '\\':
                if np.all(direction == RIGHT):
                    todo.append((position + DOWN, DOWN))
                elif np.all(direction == UP):
                    todo.append((position + LEFT, LEFT))
                elif np.all(direction == LEFT):
                    todo.append((position + UP, UP))
                elif np.all(direction == DOWN):
                    todo.append((position + RIGHT, RIGHT))
                else:
                    raise AssertionError()
            elif tile == '|':
                if np.all(direction == RIGHT) or np.all(direction == LEFT):
                    todo.append((position + UP, UP))
                    todo.append((position + DOWN, DOWN))
                else:
                    todo.append((position + direction, direction))
            elif tile == '-':
                if np.all(direction == UP) or np.all(direction == DOWN):
                    todo.append((position + LEFT, LEFT))
                    todo.append((position + RIGHT, RIGHT))
                else:
                    todo.append((position + direction, direction))
            else:
                raise AssertionError()
        
        best = max(best, len(set(x[0] for x in visited)))
    return best

print(solve(read_input(day=16)))