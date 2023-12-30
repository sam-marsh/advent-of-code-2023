import functools

from advent_of_code_2023.utils import read_input

def separate_chains(arrangement: str):
    c = []
    for part in arrangement.split('.'):
        if '#' in part:
            c.append(part)
    return c

def valid_check(arrangement: str, counts: tuple[int, ...]) -> bool:
    chains = separate_chains(arrangement)
    if len(chains) > len(counts):
        return False
    return True

def simplify(arrangement: str, counts): 
    # can delete dots either side without affecting result
    arrangement = arrangement.strip('.')

    if len(arrangement) == 0:
        if len(counts) > 0:
            # invalid if remaining hashes to be placed
            raise ValueError()
        return ('', tuple())

    if arrangement[0] == '?' and arrangement[-1] == '?':
        # cant simplify further
        return (arrangement, counts)

    if arrangement[0] == '#':
        if len(counts) == 0:
            # contradiction, hash where none available
            raise ValueError()
        # get substring corresponding to what must be a contiguous broken part chain
        sub = arrangement[:counts[0]]
        if len(sub) < counts[0]:
            # reached end of string, ran out of room
            raise ValueError()
        if '.' in sub:
            # only hashes and question marks allowed
            raise ValueError()
        # simplify by removing substring corresponding to broken parts
        arrangement = arrangement[counts[0]:]
        if len(arrangement) > 0 and arrangement[0] == '#':
            # if first char is a # then the chain was too long, invalid
            raise ValueError()
        # next char must be a dot, delete it 
        arrangement = arrangement[1:]
        counts = counts[1:]
    
    # hack to make things easier, now simplify in the other direction by reversing
    return simplify(arrangement[::-1], counts[::-1])

@functools.lru_cache(maxsize=None)
def num_arrangements(arrangement: str, counts: tuple[int, ...]):
    if '?' not in arrangement:
        a_counts = tuple(len(x) for x in arrangement.split(".") if x != '')
        return 1 if a_counts == counts else 0
    
    new_arrangement_working = arrangement.replace('?', '.', 1)
    new_arrangement_broken = arrangement.replace('?', '#', 1)

    t = 0
    try:
        simped = simplify(new_arrangement_working, counts)
        t += num_arrangements(*simped)
    except ValueError:
        pass
    try:
        simped = simplify(new_arrangement_broken, counts)
        t += num_arrangements(*simped)
    except ValueError:
        pass
    
    return t

def solve(lines: list[str]) -> int:
    s = 0
    for line in lines:
        split = line.strip().split(' ')
        arrangement = '?'.join([split[0]] * 5)
        counts = tuple(int(x) for x in split[1].split(",")) * 5
        s += num_arrangements(arrangement, counts)
    return s

if __name__ == "__main__":
    print(solve(read_input(day=12)))