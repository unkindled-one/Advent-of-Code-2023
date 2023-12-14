from util import read_blocks


class Mapping:
    def __init__(self, dest_start: int, source_start: int, range_len: int) -> None:
        self.dest_start = dest_start
        self.source_start = source_start
        self.range_len = range_len
        self._source_range = range(source_start, source_start + range_len)
        self._dest_range = range(dest_start, dest_start + range_len)

    def map_value(self, value: int) -> int:
        """Maps the given value to the destination space."""
        return value + (self.dest_start - self.source_start)

    def reverse_map_value(self, value: int):
        """Maps the value to the source space."""
        return value + (self.source_start - self.dest_start) 

    def in_range(self, value: int):
        """Returns whether the given value is part of any source range."""
        return value in self._source_range

    def in_reverse_range(self, value: int) -> bool:
        """Returns whether the given value is part of any destination range."""
        return value in self._dest_range


class Transformation:
    def __init__(self, mappings: list[Mapping]) -> None:
        self.mappings = mappings

    def transform_value(self, value: int) -> int:
        """
        Finds the mapping that contains the given value and map it according to specification.
        If there is no match, return the given value.
        """
        for mapping in self.mappings:
            if mapping.in_range(value):
                return mapping.map_value(value)
        return value

    def reverse_transform_value(self, value: int) -> int:
        """
        Finds the reverse mapping and maps it. If there is no match, return the given value.
        """
        for mapping in self.mappings:
            if mapping.in_reverse_range(value):
                return mapping.reverse_map_value(value)
        return value


def parse(data: list[list[str]]) -> tuple[list[int], list[Transformation]]: 
    seeds: list[int] = list(map(int, data[0][0].removeprefix('seeds: ').split()))
    transformations: list[Transformation] = []
    for block in data[1:]:
        mappings: list[Mapping] = []
        for li in block[1:]:
            mappings.append(Mapping(*list(map(int, li.split()))))
        transformations.append(Transformation(mappings))
    return (seeds, transformations)


def part1(seeds: list[int], transformations: list[Transformation]) -> None:
    results: list[int] = []
    for seed in seeds:
        curr: int = seed
        for transformation in transformations:
            curr = transformation.transform_value(curr)
        results.append(curr)
    print(f'Part 1 minimum value: {min(results)}')


def part2(seeds: list[int], transformations: list[Transformation]) -> None:
    # Takes several minutes. Goes through all the possible location values until one that reverse maps to a key is found.
    seed_ranges: list[range] = [range(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

    def value_is_seed(value: int) -> bool:
        return any(value in r for r in seed_ranges)

    for i in range(max(seed_ranges, key=lambda x: x.stop).stop):
        if not (i % 100_000):
            print(i)

        curr: int = i
        for transformation in transformations[::-1]:  # reverse the values
            curr = transformation.reverse_transform_value(curr)
        if value_is_seed(curr):
            print(f'Part 2 minimum value: {i}')
            break


def main() -> None:
    seeds: list[int]
    data: list[Transformation]
    # seeds, data = parse(read_blocks('input/day05_practice'))
    seeds, data = parse(read_blocks('input/day05'))
    part1(seeds, data)
    part2(seeds, data)


if __name__ == '__main__':
    main() 

