from advent_of_code_2023.utils import read_input
from sympy import *
import numpy as np
from scipy.optimize import minimize


def read_data(lines: list[str]) -> list[tuple[int, int, int], tuple[int, int, int]]:
    data = []
    for line in lines:
        split = line.split('@')
        pos = tuple(int(x.strip()) for x in split[0].split(','))
        vel = tuple(int(x.strip()) for x in split[1].split(','))
        data.append((pos, vel))
    return data

def calculate(lines: list[str]) -> int:
    data = np.array(read_data(lines))
    indices = np.random.choice(range(len(data)), 3, replace=False)
    data = data[indices]

    xr, yr, zr, vxr, vyr, vzr = symbols("xr, yr, zr, vxr, vyr, vzr")

    ts = symarray('t', len(data))

    eqs = []
    for idx, ((x, y, z), (vx, vy, vz)) in enumerate(data):
        subeqs = [
            Eq(xr + vxr * ts[idx], x + vx * ts[idx]),
            Eq(yr + vyr * ts[idx], y + vy * ts[idx]),
            Eq(zr + vzr * ts[idx], z + vz * ts[idx])
        ]
        eqs.extend(subeqs)

    sol = solve(eqs)[0]
    return sol[xr] + sol[yr] + sol[zr]



if __name__ == "__main__":
    print(calculate(read_input(day=24)))