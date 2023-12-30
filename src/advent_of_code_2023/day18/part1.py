from advent_of_code_2023.utils import read_input

dir_map = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1)
}

def bounds(polygon):
    min_i, max_i = min(x[0] for x in polygon), max(x[0] for x in polygon)
    min_j, max_j = min(x[1] for x in polygon), max(x[1] for x in polygon)
    return (min_i, min_j), (max_i, max_j)

def on_perimeter(polygon, i, j):
    for pt1, pt2 in zip(polygon, polygon[1:]):
        if min(pt1[0], pt2[0]) <= i <= max(pt1[0], pt2[0]) and min(pt1[1], pt2[1]) <= j <= max(pt1[1], pt2[1]):
            return True
    return False

def inside(polygon, bds, i, j):
    intersections = 0
    for ri in range(bds[0][0], bds[1][0]):
        if on_perimeter(polygon, ri, j):
            if ri == i:
                return False
            intersections += 1
        if ri == i:
            return intersections % 2 == 1
    raise AssertionError()

def solve(lines: list[str]) -> int:
    data = []
    for line in lines:
        split = line.strip().split(' ')
        data.append((
            split[0], int(split[1]), split[2][1:-1]
        ))
    polygon = [(0, 0)]
    perimeter = 0
    for dir, num, _ in data:
        dir = dir_map[dir]
        polygon.append((polygon[-1][0] + num * dir[0], polygon[-1][1] + num * dir[1]))
        perimeter += abs(polygon[-1][0] - polygon[-2][0]) + abs(polygon[-1][1] - polygon[-2][1])
    bds = bounds(polygon)

    first = next((i, j) for i in range(bds[0][0], bds[1][0] + 1) for j in range(bds[0][1], bds[1][1] + 1) if inside(polygon, bds, i, j))
    visited = set()
    todo = [first]

    while todo:
        curr = todo.pop()
        if curr in visited:
            continue
        visited.add(curr)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nex = curr[0] + di, curr[1] + dj
            if on_perimeter(polygon, *nex): continue
            todo.append(nex)
    
    return len(visited) + perimeter

print(solve(read_input(day=18)))