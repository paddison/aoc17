from math import sqrt


def parse_input(filename) -> dict[str, str]:
    with open(filename) as file:
        return {line.split('=>')[0].strip(): line.split('=>')[1].strip() for line in file}


def str_to_list(pattern: str) -> list[str]:
    return pattern.split('/')


def list_to_str(pattern: list[str]):
    return '/'.join(row for row in pattern)


def rotate(pattern: list[str]) -> list[str]:
    return list(map(lambda chars: ''.join(chars), zip(*pattern[::-1])))


def flip(pattern: list[str]) -> list[str]:
    return pattern[::-1]


def split(pattern: list[str]) -> list[list[str]]:
    length = len(pattern)
    divisor = 2 if length % 2 == 0 else 3
    grid = list()
    for i in range(0, length, divisor):
        for j in range(0, length, divisor):
            sublist = list()
            for k in range(i, i + divisor):
                sublist.append(pattern[k][j:j + divisor])
            grid.append(sublist)
    return grid


def join(patterns: list[list[str]]) -> list[str]:
    total_length = len(patterns)
    divisor = len(patterns[0])
    length = int(sqrt(divisor * divisor * len(patterns)))
    grid = list()
    for i in range(0, total_length, length // divisor):
        s = ''
        for j in range(0, divisor):
            s = ''
            for k in range(i, i + length // divisor):
                s += patterns[k][j]
            grid.append(s)
    return grid


def apply_rule(pattern: list[str], rules: dict[str, str]) -> list[str]:
    assert (4 > len(pattern) > 1)
    for _ in range(2):
        for _ in range(4):
            pattern_str = list_to_str(pattern)
            if rules.get(pattern_str, None):
                return str_to_list(rules[pattern_str])
            pattern = rotate(pattern)
        pattern = flip(pattern)


def iterate(n: int, pattern: list[str], rules: dict[str, str]) -> list[str]:
    for n in range(n):
        patterns = split(pattern)
        new_patterns = list()
        for pattern in patterns:
            new_patterns.append(apply_rule(pattern, rules))
        pattern = join(new_patterns)
    return pattern


def count_on(pattern: list[str]) -> int:
    return sum(1 for row in pattern for p in row if p == "#")


def main():
    start = '.#./..#/###'
    rules = parse_input('data.txt')
    pattern = str_to_list(start)
    pattern = iterate(5, pattern, rules)
    print(f'Part 1: {count_on(pattern)}')
    pattern = iterate(13, pattern, rules)
    print(f'Part 2: {count_on(pattern)}')


if __name__ == '__main__':
    main()
