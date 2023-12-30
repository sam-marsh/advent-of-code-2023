import numpy as np
from advent_of_code_2023.utils import read_input

def _check_horizontal_reflection(array, can_correct=False,):
    i = len(array) // 2 - 1
    if len(array) <= 1:
        return True
    if i + 1 >= len(array):
        return False
    if any(array[i] != array[i + 1]):
        if not can_correct or sum(array[i] != array[i + 1]) > 1:
            return False
        can_correct = False
    sub_array = np.concatenate([array[:i], array[i+2:]])
    return _check_horizontal_reflection(sub_array, can_correct)

def check_horizontal_reflection(array, i, can_correct):
    rows_before_line = i + 1
    rows_after_line = len(array) - i - 1
    balance = min(rows_before_line, rows_after_line)
    return _check_horizontal_reflection(array[i-balance+1:i+balance+1], can_correct)

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

            no_correction_result = None
            for i in range(n - 1):
                if check_horizontal_reflection(array, i, False):
                    print("H", i + 1)
                    no_correction_result = ("H", i)
                    found = True
                    break
            for j in range(m - 1):
                if check_horizontal_reflection(array.T, j, False):
                    print("V", j + 1)
                    no_correction_result = ("V", j)
                    found = True
                    break
            
            found = False
            for i in range(n - 1):
                if ("H", i) == no_correction_result: continue
                if check_horizontal_reflection(array, i, True):
                    print("H", i + 1, "corrected")
                    found = True
                    total += (i + 1) * 100
                    break
            if found:
                curr = []
                continue
            for j in range(m - 1):
                if ("V", j) == no_correction_result: continue
                if check_horizontal_reflection(array.T, j, True):
                    print("V", j + 1, "corrected")
                    found = True
                    total += (j + 1)
                    break

            assert found
            curr = []
    return total


if __name__ == "__main__":
    print(solve(read_input(day=13)))