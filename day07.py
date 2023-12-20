from collections import Counter
from util import read_lines
from functools import cmp_to_key
from dataclasses import dataclass


@dataclass
class Hand:
    cards: str
    bet: int
    rank: int = 0


def parse(data: list[str]) -> list[Hand]:
    result: list[Hand] = []
    for line in data:
        cards, bet = line.split()
        result.append(Hand(cards, int(bet)))
    return result


def part1(hands: list[Hand]):
    mappings = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
    }

    def assign_rank(hand: Hand) -> None:
        counter: list[tuple[str, int]] = Counter(hand.cards).most_common()
        if counter[0][1] == 5:
            hand.rank = 7
        elif counter[0][1] == 4:
            hand.rank = 6
        elif counter[0][1] == 3 and counter[1][1] == 2:
            hand.rank = 5
        elif counter[0][1] == 3:
            hand.rank = 4
        elif counter[0][1] == 2 and counter[1][1] == 2:
            hand.rank = 3
        elif counter[0][1] == 2:
            hand.rank = 2
        else:
            hand.rank = 1

    def compare(h1: Hand, h2: Hand) -> int:
        if h1.rank != h2.rank:
            return h1.rank - h2.rank
        for c1, c2 in zip(list(h1.cards), list(h2.cards)):
            if c1 != c2:
                return mappings[c1] - mappings[c2]
        return 0

    for hand in hands:
        assign_rank(hand)

    total: int = 0
    for i, hand in enumerate(sorted(hands, key=cmp_to_key(compare))):
        total += hand.bet * (i + 1)

    print(f'Part 1 total: {total}')


def part2(hands: list[Hand]):
    mappings = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
        'J': 1
    }

    def assign_rank(hand: Hand) -> None:
        counter: Counter = Counter(hand.cards)
        num_jokers: int = counter['J']
        del counter['J']
        most_common: list[tuple[str, int]] = counter.most_common()
        if num_jokers == 5 or most_common[0][1] + num_jokers == 5:
            hand.rank = 7
        elif most_common[0][1] + num_jokers == 4:
            hand.rank = 6
        elif most_common[0][1] + num_jokers == 3 and most_common[1][1] == 2:
            hand.rank = 5
        elif most_common[0][1] + num_jokers == 3:
            hand.rank = 4
        elif most_common[0][1] + num_jokers == 2 and most_common[1][1] == 2:
            hand.rank = 3
        elif most_common[0][1] + num_jokers == 2:
            hand.rank = 2
        else:
            hand.rank = 1

    def compare(h1: Hand, h2: Hand) -> int:
        if h1.rank != h2.rank:
            return h1.rank - h2.rank
        for c1, c2 in zip(list(h1.cards), list(h2.cards)):
            if c1 != c2:
                return mappings[c1] - mappings[c2]
        return 0
    for hand in hands:
            assign_rank(hand)

    total: int = 0
    for i, hand in enumerate(sorted(hands, key=cmp_to_key(compare))):
        print(f'{hand.cards}: {hand.rank}')
        total += hand.bet * (i + 1)

    print(f'Part 2 total: {total}')


def main():
    data: list[Hand] = parse(read_lines('input/day07'))
    # data: list[Hand] = parse(read_lines('input/day07_practice'))
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()

