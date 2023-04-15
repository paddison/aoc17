import math


START = '.#./..#/###'


def parse_input(filename) -> dict[str, str]:
    with open(filename) as file:
        return {line.split('=>')[0].strip(): line.split('=>')[1].strip() for line in file}


def str_to_list(pattern: str) -> list[list[bool]]:
    return [[c == '#' for c in p] for p in pattern.split('/')]


def list_to_str(pattern: list[list[bool]]):
    return '/'.join(''.join('#' if x else '.' for x in row) for row in pattern)


def rotate(pattern: list[list[bool]]) -> list[list[bool]]:
    assert(4 > len(pattern) > 1)
    length = len(pattern)
    return [[pattern[r][c] for r in reversed(range(length))] for c in range(length)]


def flip(pattern: list[list[bool]]) -> list[list[bool]]:
    return [list(reversed(row)) for row in pattern]


def split(pattern: list[list[bool]]) -> list[list[list[bool]]]:
    splits = list()
    for r in [0, 2]:
        for c in [0, 2]:
            splits.append([p[c:c + 2] for p in pattern[r:r + 2]])
    return splits


def apply_rule(pattern: list[list[bool]], rules: dict[str, str]) -> list[list[bool]]:
    assert(4 > len(pattern) > 1)
    for _ in range(2):
        for _ in range(4):
            pattern_str = list_to_str(pattern)
            if rules.get(pattern_str, None):
                return str_to_list(rules[pattern_str])
            pattern = rotate(pattern)
        pattern = flip(pattern)


def print_grid(grid: list[list[list[bool]]]):
    length = int(math.sqrt(len(grid)))
    

def main():
    rules = parse_input('data.txt')
    grid = [str_to_list(START)]
    for _ in range(5):
        new_grid = list()
        for pattern in grid:
            new_pattern = apply_rule(pattern, rules)
            if len(new_pattern) == 4:
                new_grid.extend(split(new_pattern))
            else:
                new_grid.append(new_pattern)
        grid = new_grid  # verify this works

    print(sum(1 for p in grid for r in p for pixel in r if pixel))


if __name__ == '__main__':
    main()
