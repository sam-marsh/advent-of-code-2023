import functools
from advent_of_code_2023.utils import read_input

def process_game(line: str):
    winningstr, havestr = line.split(':')[1].strip().split('|')
    print(winningstr, havestr)
    winning_numbers = set(int(x) for x in winningstr.strip().split(' ') if x is not '')
    have_numbers = [int(x) for x in havestr.strip().split(' ') if x is not '']
    card_value = 0
    for n in have_numbers:
        if n in winning_numbers:
            card_value += 1
    return card_value

def count_value(lines: list[str]):
    wins = {}
    for i in range(len(lines)):
        if i + 1 in wins:
            continue
        v = process_game(lines[i])
        wins[i + 1] = list(range(i + 2, i + 2 + v))
    
    print(wins)
    @functools.lru_cache(maxsize=None)
    def count_wins(idx):
        if len(wins[idx]) == 0:
            return 1
        return 1 + sum(count_wins(x) for x in wins[idx])
        

    return sum(count_wins(x) for x in range(1, len(lines) + 1))

if __name__ == "__main__":
    print(count_value(read_input(day=4)))