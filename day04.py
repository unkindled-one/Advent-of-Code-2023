from util import read_lines
from dataclasses import dataclass


@dataclass
class Card:
    index: int
    winning_numbers: list[int]
    owned_numbers: list[int]
    count: int = 1

    def num_matching(self) -> int:
        """Returns the number of owned numbers that are also in the winning numbers list"""
        total = 0
        for num in self.owned_numbers:
            if num in self.winning_numbers:
                total += 1
        return total


def parse(data: list[str]) -> list[Card]:
    """Parse the data into Card objects"""
    result = []
    for i, line in enumerate(data):
        line = line.split(': ')[1]
        line = line.split(' | ')
        winning = [int(x) for x in line[0].split()]
        owned = [int(x) for x in line[1].split()]
        result.append(Card(i, winning, owned))
    return result


def part1(data: list[Card]) -> None:
    total = 0
    for card in data:
        winning_count = card.num_matching()
        total += 2 ** (winning_count - 1) if winning_count != 0 else 0

    print(f'Total for part 1: {total}')


def part2(data: list[Card]) -> None:
    for i, card in enumerate(data):
        winning_count = card.num_matching()
        for future_card in data[i + 1: i + winning_count + 1]:
            future_card.count += card.count
    total = sum([card.count for card in data])
    print(f'Total for part 2: {total}')


def main() -> None:
    data: list[Card] = parse(read_lines('input/day04'))
    # data: list[Card] = parse(read_lines('input/day04_practice'))
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()

