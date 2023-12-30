from functools import lru_cache
from matplotlib import pyplot as plt
import numpy as np
from advent_of_code_2023.utils import read_input

def valid(data, i, j):
    return data[i % len(data), j % len(data[0])] != '#'

def solve(lines: list[str]) -> int:
    data = np.array([list(x.strip()) for x in lines])
    first = tuple(np.array(np.where(data == 'S')).flatten())

    def step_set(s):
        n1 = set((i, j + 1) for (i, j) in s if valid(data, i, j + 1))
        n2 = set((i, j - 1) for (i, j) in s if valid(data, i, j - 1))
        n3 = set((i + 1, j) for (i, j) in s if valid(data, i + 1, j))
        n4 = set((i - 1, j) for (i, j) in s if valid(data, i - 1, j))
        return n1.union(n2, n3, n4)
    
    curr = set([first])
    lengths = [1]
    for _ in range(400):
        curr = step_set(curr)
        lengths.append(len(curr))

    xs = np.array(list(range(len(lengths))))
    np.savetxt('data.txt', np.stack((xs, lengths)))

    # Unsatisfying approach...
    # Two observations from plotting data:
    # - The pattern is periodic in the size of the square grid
    # - The scaling is quadratic
    # No idea how to solve this more generally.
    s = 26501365 % len(data)
    print(s)
    print(xs[s::len(data)])
    fit, *extra = np.polyfit(xs[s::len(data)], lengths[s::len(data)], 2, full=True)
    p = np.poly1d(fit)
    
    # freqs = {}
    # for s in curr:
    #     canonical = (s[0] % len(data), s[1] % len(data[0]))
    #     if canonical in freqs:
    #         freqs[canonical] += 1
    #     else:
    #         freqs[canonical] = 1
    
    # formatted = np.zeros_like(data, dtype=int)

    # for i in range(len(data)):
    #     for j in range(len(data)):
    #         if data[i, j] == '#':
    #             formatted[i, j] = 0
    #         else:
    #             formatted[i, j] = freqs.get((i, j), 0)

    # print('\n'.join(' '.join(f'{y:04}' for y in x) for x in formatted))

    print(extra)
    # plt.plot(xs, lengths)
    # plt.plot(xs, p(xs))
    # plt.show()

    return p(26501365)

print(solve(read_input(day=21)))