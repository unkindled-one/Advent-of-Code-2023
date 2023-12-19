from util import read_lines


def parse(data: list[str]) -> tuple[list[int], list[int]]:
    times = [int(num) for num in data[0].split()[1:]]
    distances = [int(num) for num in data[1].split()[1:]]
    return (times, distances)


def part1(times: list[int], distances: list[int]):
    total: int = 1
    # Scan from the start and the end
    for time, distance in zip(times, distances):
        start = 0
        end = time

        while distance_elapsed(start, time) <= distance:
            start += 1

        while distance_elapsed(end, time) <= distance:
            end -= 1

        total *= (end - start) + 1

    print(f'Part 1 total: {total}')


def distance_elapsed(time_held: int, time_total: int) -> int:
    return (time_total - time_held) * time_held


def part2(times: list[int], distances: list[int]):
    time: int = int(''.join([str(num) for num in times]))
    distance: int = int(''.join([str(num) for num in distances]))
    start = 0
    end = time

    while distance_elapsed(start, time) <= distance:
        start += 1

    while distance_elapsed(end, time) <= distance:
        end -= 1

    print(f'Part 2 total: {(end - start) + 1}')


def main():
    times, distances = parse(read_lines('input/day06'))
    # times, distances = parse(read_lines('input/day06_practice'))
    part1(times, distances)
    part2(times, distances)



if __name__ == '__main__':
    main()

