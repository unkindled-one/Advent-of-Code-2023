from util import read_lines
import math
from itertools import count


def part1(data: list[str]):
    directions: str = data[0]
    direction_map: dict[str, str] = {} 
    for line in data[2:]:
        line_parts: list[str] = line.split()
        start: str = line_parts[0]
        left: str = line_parts[2][1:-1]
        right: str = line_parts[3][:-1]
        direction_map[start + 'L'] = left
        direction_map[start + 'R'] = right

    curr: str = 'AAA'
    for i in count():
        curr_direction = directions[i % len(directions)]
        curr = direction_map[curr + curr_direction]
        if curr == 'ZZZ':
            print(f'Part 1 total: {i + 1}')
            break
        

def part2(data: list[str]):
    # This solution assumes that the data is a closed loop that will eventually sync, uses the LCM to compute this.
    directions: str = data[0]
    direction_map: dict[str, str] = {} 
    for line in data[2:]:
        line_parts: list[str] = line.split()
        start: str = line_parts[0]
        left: str = line_parts[2][1:-1]
        right: str = line_parts[3][:-1]
        direction_map[start + 'L'] = left
        direction_map[start + 'R'] = right
    
    loop_counts: list[int] = []

    starting: list[str] = [x[:-1] for x in direction_map.keys() if x[2] == 'A']
    for node in starting:  # Count the length of loop for each starting node
        for i in count():
            curr_direction: str = directions[i % len(directions)]
            node: str = direction_map[node + curr_direction]
            if node[2] == 'Z':
                loop_counts.append(i + 1)
                break

    print(f'Part 2 total: {math.lcm(*loop_counts)}')


def main():
    graph = read_lines('input/day08')
    # graph = read_lines('input/day08_practice')
    part1(graph)
    # graph = read_lines('input/day08_practice_2')
    part2(graph)


if __name__ == '__main__':
    main()

