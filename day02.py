from util import read_lines


def parse(data: list[str]) -> list[list[list[str]]]:
    """Parse the data into an easier form to work with."""
    parsed_data = []
    for line in data:
        new_str = line.split(': ')[1]
        rounds = []
        for round in new_str.split('; '):
            current_hand = []
            for color in round.split(', '):
                c = color.split(' ')
                current_hand.append(f'{c[0]} {c[1]}')
            rounds.append(current_hand)
        parsed_data.append(rounds)

    return parsed_data


def part1(data: list[str]) -> None:
    total = 0
    max_amounts = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    final_input = parse(data)
    for i, round in enumerate(final_input):
        is_possible = True
        for hand in round:
            if not is_possible:
                break
            for color in hand:
                color = color.split(' ')
                if int(color[0]) > max_amounts[color[1]]:
                    is_possible = False
                    break
        if is_possible:
            total += i + 1
    print(f'Total for part 1: {total}')


def part2(data: list[str]) -> None:
    final_input = parse(data)
    total = 0
    for round in final_input:
        max_blue = 0
        max_red = 0
        max_green = 0
        for hand in round:
            for color in hand:
                color = color.split(' ')
                if color[1] == 'blue' and int(color[0]) > max_blue:
                    max_blue = int(color[0])
                elif color[1] == 'red' and int(color[0]) > max_red:
                    max_red = int(color[0])
                elif color[1] == 'green' and int(color[0]) > max_green:
                    max_green = int(color[0])
        total += max_red * max_green * max_blue

    print(f'Total for part 2: {total}')


def main() -> None:
    # data: list[str] = read_lines('input/day02_practice')
    data: list[str] = read_lines('input/day02')
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()

