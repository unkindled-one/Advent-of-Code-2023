from util import read_lines


def part1(data: list[str]):
    total: int = 0
    parsed_data: list[list[int]] = [list(map(int, x.split())) for x in data]
    for line in parsed_data:
        triangle: list[list[int]] = []
        triangle.append(line)
        while True:
            new_line: list[int] = []
            for i in range(len(triangle[-1]) - 1):
                new_line.append(triangle[-1][i+1] - triangle[-1][i]) 
            if not any(new_line):
                break
            triangle.append(new_line)
        curr: int = 0
        for li in reversed(triangle):
            curr += li[-1]
        total += curr

    print(f'Part 1 total: {total}')


def part2(data: list[str]):
    total: int = 0
    parsed_data: list[list[int]] = [list(map(int, x.split())) for x in data]
    for line in parsed_data:
        triangle: list[list[int]] = []
        triangle.append(line)
        while True:
            new_line: list[int] = []
            for i in range(len(triangle[-1]) - 1):
                new_line.append(triangle[-1][i+1] - triangle[-1][i]) 
            if not any(new_line):
                break
            triangle.append(new_line)
        curr: int = 0
        for li in reversed(triangle):
            curr = li[0] - curr
        total += curr

    print(f'Part 2 total: {total}')


def main():
    data: list[str] = read_lines('input/day09')
    # data: list[str] = read_lines('input/day09_practice')
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()

