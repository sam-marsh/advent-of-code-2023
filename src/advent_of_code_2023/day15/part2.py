from collections import defaultdict
from advent_of_code_2023.utils import read_input

def calculate_hash(line: str) -> int:
    value = 0
    for c in line:
        value += ord(c)
        value *= 17
        value %= 256
    return value

def solve(lines: list[str]) -> int:
    line = lines[0].strip()
    boxes = defaultdict(lambda: {})
    for s in line.split(","):
        if "-" in s:
            label = s[:-1]
            box = calculate_hash(label)
            if label in boxes[box]:
                del boxes[box][label]
        elif "=" in s:
            label, lens = s.split("=")
            lens = int(lens)
            box = calculate_hash(label)
            boxes[box][label] = lens
        else:
            raise AssertionError
    
    total = 0
    for box, contents in boxes.items():
        for idx, focal in enumerate(contents.values()):
            total += (box + 1) * (idx + 1) * focal
    
    return total

print(solve(read_input(day=15)))