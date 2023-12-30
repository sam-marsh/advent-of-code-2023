import re
from advent_of_code_2023.utils import read_input


def get_count(turn: str, colour: str) -> int:
    matches = re.findall(rf'(\d+)\s+{colour}', turn)
    if matches:
        return sum(int(match) for match in matches)
    else:
        return 0

def min_game_power(line: str, max_r: int, max_g: int, max_b: int) -> tuple[int, int, int]:
    turns = line[line.index(':') + 1::]
    min_r, min_g, min_b = 0, 0, 0
    for turn in turns.split(';'):
        r, g, b = (get_count(turn, colour) for colour in ('red', 'green', 'blue'))
        min_r = max(min_r, r)
        min_g = max(min_g, g)
        min_b = max(min_b, b)
    return min_r * min_g * min_b

def sum_games(lines: list[str], max_r: int, max_g: int, max_b: int) -> int:
    return sum(min_game_power(line, max_r, max_g, max_b) for line in lines)

if __name__ == '__main__':
    print(sum_games(read_input(day=2), 12, 13, 14))