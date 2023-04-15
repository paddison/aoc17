import math
from itertools import count


test_data = [['ne', 'ne', 'ne'], ['ne', 'ne', 'sw', 'sw'], ['ne', 'ne', 's', 's'], ['se', 'sw', 'se', 'sw', 'sw']]


def parse_input(filename: str) -> list[str]:
    with open(filename) as file:
        return [direction for direction in file.readline().split(',')]


def update_pos(pos: (int, int), direction: str) -> (int, int):
    match direction:
        case 'n': return pos[0], pos[1] + 1
        case 's': return pos[0], pos[1] - 1
        case 'ne': return pos[0] + 1, pos[1] + (pos[0] % 2)
        case 'se': return pos[0] + 1, pos[1] - ((pos[0] + 1) % 2)
        case 'nw': return pos[0] - 1, pos[1] + (pos[0] % 2)
        case 'sw': return pos[0] - 1, pos[1] - ((pos[0] + 1) % 2)


def get_neighbours(pos: (int, int)) -> list[(int, int)]:
    return [
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
        (pos[0] + 1, pos[1] + (pos[0] % 2)),
        (pos[0] + 1, pos[1] - ((pos[0] + 1) % 2)),
        (pos[0] - 1, pos[1] + (pos[0] % 2)),
        (pos[0] - 1, pos[1] - ((pos[0] + 1) % 2))
    ]


def distance(current: (int, int), goal: (int, int)) -> float:
    return math.sqrt(math.pow(abs(current[0] - goal[0]), 2) + math.pow(abs(current[1] - goal[1]), 2))


def calculate_min_steps(goal: (int, int)) -> int:
    current_position = 0, 0
    for steps in count():
        if current_position == goal:
            return steps
        neighbours = get_neighbours(current_position)
        current_position = min(neighbours, key=lambda n: distance(n, goal))


def main():
    inp = parse_input('data.txt')
    pos = 0, 0
    all_steps = list()
    for direction in inp:
        pos = update_pos(pos, direction)
        all_steps.append(calculate_min_steps(pos))

    print(calculate_min_steps(pos))
    print(max(all_steps))


if __name__ == '__main__':
    main()
