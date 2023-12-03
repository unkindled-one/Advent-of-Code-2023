from util import readlines


def part1(data: list[str]):
    total = 0
    for line in data:
        new_line: str = ''.join(list(filter(lambda x: x.isnumeric(), line)))
        total += int(new_line[0] + new_line[-1])
        
    print(f'Total for part 1: {total}')
    

def part2(data: list[str]):
    mapping = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't333e',
        'four': 'f44r',
        'five': 'f555e',
        'six': 's6x',
        'seven': 's777n',
        'eight': 'e888t',
        'nine': 'n99e'
    }

    total: int = 0
    for line in data:
        for key, value in mapping.items():
            line = line.replace(key, value)
        new_line: str = ''.join(list(filter(lambda x: x.isnumeric(), line)))
        total += int(new_line[0] + new_line[-1])
    print(f'Total for part 2: {total}')


def main():
    data: list[str] = readlines("input/day01")
    part1(data)
    part2(data) # not 53888, 57500, or 53896, 53651

if __name__ == "__main__":
    main()
