from itertools import count


def parse_input(filename: str) -> dict[int, int]:
    with open(filename) as file:
        return {int(line.split(':')[0]): int(line.split(':')[1]) for line in file}


def collides(scanner: int, depth: int) -> bool:
    return scanner % (2 * depth - 2) == 0


def main():
    scanners = parse_input('data.txt')
    s = sum(scanner * depth for scanner, depth in scanners.items() if collides(scanner, depth))
    print(f'Part 1: {s}')
    for delay in count():
        if all(not collides(scanner + delay, depth) for scanner, depth in scanners.items()):
            print(f'Part 2: {delay}')
            break


if __name__ == '__main__':
    main()
