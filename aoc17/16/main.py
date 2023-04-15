from collections import deque
from itertools import count


def parse_input(filename: str) -> list[str]:
    with open(filename) as file:
        return [move for move in file.readline().split(',')]


def do_move(move: str, programs: deque[str]):
    match move[0]:
        case 's': do_spin(int(move[1:]), programs)
        case 'x': do_exchange(int(move[1:move.index('/')]), int(move[move.index('/') + 1:]), programs)
        case 'p': do_partner(move[1], move[3], programs)


def do_spin(n: int, programs: deque[str]):
    programs.rotate(n)


def do_exchange(a: int, b: int, programs: deque[str]):
    programs[a], programs[b] = programs[b], programs[a]


def do_partner(a: str, b: str, programs: deque[str]):
    a_idx = programs.index(a)
    b_idx = programs.index(b)
    programs[a_idx], programs[b_idx] = programs[b_idx], programs[a_idx]


def create_programs(n: int) -> deque[str]:
    return deque(chr(i + 97) for i in range(n))


def main():
    inp = parse_input('data.txt')
    programs = create_programs(16)
    for move in inp:
        do_move(move, programs)
    print(f'Part 1: {"".join(programs)}')
    programs = create_programs(16)
    cycle = 0
    for i in count():
        for move in inp:
            do_move(move, programs)
        if ''.join(programs) == 'abcdefghijklmnop':
            cycle = i + 1
            break
    for i in range(cycle * (1_000_000_000 // cycle), 1_000_000_000):
        for move in inp:
            do_move(move, programs)
    print(f'Part 2: {"".join(programs)}')


if __name__ == '__main__':
    main()
