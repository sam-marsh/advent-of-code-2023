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
    print(line)
    return sum(calculate_hash(x) for x in line.split(","))

print(calculate_hash("HASH"))
print(solve(read_input(day=15)))