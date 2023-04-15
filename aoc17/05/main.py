def parse_input(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(line) for line in file]


def escape(jumps: list[int]) -> int:
    cursor = 0
    n_jumps = 0
    while cursor < len(jumps):
        offset = jumps[cursor]
        if offset >= 3:
            jumps[cursor] -= 1
        else:
            jumps[cursor] += 1
        cursor += offset
        n_jumps += 1
    return n_jumps


def main():
    print(escape(parse_input('data.txt')))


if __name__ == '__main__':
    main()
