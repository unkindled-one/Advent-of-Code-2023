def read_lines(path: str) -> list[str]:
    """Reads each line of a file into a list."""
    res: list[str] = []
    with open(path) as f:
        for line in f.readlines():
            res.append(line.strip('\n'))

    return res


def read_blocks(path: str) -> list[list[str]]:
    """Reads a file separated by double newline into a 2d array."""
    res: list[list[str]] = []
    with open(path) as f:
        for line in f.read().split('\n\n'):
            res.append(line.split('\n'))

    return res
    

if __name__ == '__main__':
    print(read_blocks('input/day05_practice'))
