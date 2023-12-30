from advent_of_code_2023.utils import read_input


def read_data(lines: list[str]) -> list[tuple[int, int, int], tuple[int, int, int]]:
    data = []
    for line in lines:
        split = line.split('@')
        pos = tuple(int(x.strip()) for x in split[0].split(','))
        vel = tuple(int(x.strip()) for x in split[1].split(','))
        data.append((pos, vel))
    return data

def solve(lines: list[str], lower_bound, upper_bound) -> int:
    data = read_data(lines)

    total = 0
    for i in range(len(data)):
        x1, y1, _ = data[i][0]
        vx1, vy1, _ = data[i][1]
        for j in range(i):
            x2, y2, _ = data[j][0]
            vx2, vy2, _ = data[j][1]

            denom = vx2 * vy1 - vx1 * vy2
            if denom == 0:
                continue
            
            t1 = (vy2 * x1 - vy2 * x2 - vx2 * y1 + vx2 * y2) / denom
            t2 = (vy1 * x1 - vy1 * x2 - vx1 * y1 + vx1 * y2) / denom
            
            if t1 < 0 or t2 < 0:
                continue

            sx = x1 + t1 * vx1 
            sy = y1 + t1 * vy1

            if lower_bound <= sx <= upper_bound and lower_bound <= sy <= upper_bound:
                total += 1
    return total



if __name__ == "__main__":
    print(solve(read_input(day=24), 200000000000000, 400000000000000))