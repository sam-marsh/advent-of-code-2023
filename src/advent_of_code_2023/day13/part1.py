import numpy as np
from advent_of_code_2023.utils import read_input

def _check_horizontal_reflection(array):
    i = len(array) // 2 - 1
    if len(array) <= 1:
        return True
    if i + 1 >= len(array):
        return False
    if any(array[i] != array[i + 1]):
        return False
    sub_array = np.concatenate([array[:i], array[i+2:]])
    return _check_horizontal_reflection(sub_array)

def check_horizontal_reflection(array, i):
    rows_before_line = i + 1
    rows_after_line = len(array) - i - 1
    balance = min(rows_before_line, rows_after_line)
    return _check_horizontal_reflection(array[i-balance+1:i+balance+1])

def solve(lines: list[str]):
    lines.append('')
    curr = []

    total = 0
    for line in lines:
        if line.strip() != '':
            curr.append(list(line.strip()))
        else:
            array = np.array(curr)
            print(array)
            n, m = array.shape
            found = False
            for i in range(n - 1):
                if check_horizontal_reflection(array, i):
                    print("H", i + 1)
                    total += (i + 1) * 100
                    found = True
                    break
            if found:
                curr = []
                continue
            for j in range(m - 1):
                if check_horizontal_reflection(array.T, j):
                    print("V", j + 1)
                    total += (j + 1)
                    found = True
                    break
            assert found
            curr = []
    return total


if __name__ == "__main__":
    print(solve(read_input(day=13)))