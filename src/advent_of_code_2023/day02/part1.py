import re
from advent_of_code_2023.utils import read_input


def get_count(turn: str, colour: str) -> int:
    matches = re.findall(rf'(\d+)\s+{colour}', turn)
    if matches:
        return sum(int(match) for match in matches)
    else:
        return 0

def valid_game(line: str, max_r: int, max_g: int, max_b: int) -> bool:
    turns = line[line.index(':') + 1::]
    for turn in turns.split(';'):
        r, g, b = (get_count(turn, colour) for colour in ('red', 'green', 'blue'))
        print(turn, r, g, b)
        if r > max_r or g > max_g or b > max_b:
            return False
    return True

def sum_games(lines: list[str], max_r: int, max_g: int, max_b: int) -> int:
    return sum(idx + 1 for idx, line in enumerate(lines) if valid_game(line, max_r, max_g, max_b))

if __name__ == '__main__':
    print(sum_games(read_input(day=2), 12, 13, 14))