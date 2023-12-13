from util import read_lines
import re

def check_surrounding(data: list[str], row: int, col: int) -> bool:
    """Checks all positions around a given index for nonsymbols."""
    non_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    for i in range(max(0, row - 1), min(len(data), row + 2)):
        for j in range(max(0, col - 1), min(len(data[i]), col + 2)):
            if data[i][j] not in non_symbols:
                return True
    return False



def part1(data: list[str]):
    # Scan around the numbers instead of the symbols because it avoids overcounting
    total = 0
    number_regex = re.compile(r'\d+')
    for i, line in enumerate(data):
        for match in re.finditer(number_regex, line):
            for span in range(*match.span()):
                if check_surrounding(data, i, span):
                    total += int(match[0])
                    print(match[0])
                    break

    print(f'Total for part 1: {total}')



def part2(data: list[str]):
    total = 0
    number_regex = re.compile(r'\d+')
    all_numbers = [list(re.finditer(number_regex, s)) for s in data]
    all_gears = []
    for i, line in enumerate(data):  # Find the position of every potential gear
        for j, symbol in enumerate(list(line)):
            if symbol == '*':
                all_gears.append((i, j))

    for gear in all_gears:  # Find out which potential gears are actual gears
        row, col = gear
        surrounding_numbers = set()  # Set to weed out duplicates
        # Loop in a 3x3 area around the gear
        for i in range(max(0, row - 1), min(len(data), row + 2)):
            for j in range(max(0, col - 1), min(len(data[i]), col + 2)):
                for potential_number in all_numbers[i]:
                    if j in range(*potential_number.span()):
                        surrounding_numbers.add(potential_number)
        
        if len(surrounding_numbers) != 2:
            continue  # Must be exactly two numbers for a valid gear
        surrounding_numbers = list(surrounding_numbers)
        total += int(surrounding_numbers[0][0]) * int(surrounding_numbers[1][0])
        
    print(f'Total for part 2: {total}')


def main():
    data: list[str] = read_lines('input/day03')    
    # data: list[str] = read_lines('input/day03_practice')    
    part1(data)
    part2(data)

if __name__ == "__main__":
    main() 
