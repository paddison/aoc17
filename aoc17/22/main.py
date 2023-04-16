def parse_input(filename: str) -> (set[(int, int)], (int, int)):
    with open(filename) as file:
        content = [line.strip() for line in file]
        pos = len(content[0]) // 2, len(content) // 2
        infected = {(j, i) for i, line in enumerate(reversed(content)) for j, c in enumerate(line) if c == '#'}
    return infected, pos


def print_grid(infected: set[(int, int)], weakened: set[(int, int)], flagged: set[(int, int)]):
    unions = infected.union(weakened).union(flagged)
    xs = list(map(lambda p: p[0], unions))
    ys = list(map(lambda p: p[1], unions))
    min_x, max_x = min(xs), max(xs) + 1
    min_y, max_y = min(ys), max(ys) + 1
    grid = list()
    for y in range(min_y, max_y):
        s = ''
        for x in range(min_x, max_x):
            if (x, y) in infected:
                s += '#'
            elif (x, y) in weakened:
                s += 'W'
            elif (x, y) in flagged:
                s += 'F'
            else:
                s += '.'
        grid.append(s)
    for line in reversed(grid):
        print(line)


def run_simulation(infected: set[(int, int)], pos: (int, int), iterations: int) -> int:
    dx, dy = 0, 1
    c = 0
    for _ in range(iterations):
        if pos in infected:
            dx, dy = dy, -dx
            infected.remove(pos)
        else:
            dx, dy = -dy, dx
            infected.add(pos)
            c += 1
        pos = (pos[0] + dx, pos[1] + dy)
    return c


def run_simulation_evolved(infected: set[(int, int)], pos: (int, int), iterations: int) -> int:
    dx, dy = 0, 1
    c = 0
    weakened = set()
    flagged = set()
    for _ in range(iterations):
        if pos in infected:
            dx, dy = dy, -dx
            infected.remove(pos)
            flagged.add(pos)
        elif pos in weakened:
            weakened.remove(pos)
            infected.add(pos)
            c += 1
        elif pos in flagged:
            dx, dy = -dx, -dy
            flagged.remove(pos)
        else:
            dx, dy = -dy, dx
            weakened.add(pos)
        pos = (pos[0] + dx, pos[1] + dy)
    return c


def main():
    (infected, pos) = parse_input('data.txt')
    c = run_simulation(infected, pos, 10000)
    print(f'Part 1: {c}')

    (infected, pos) = parse_input('data.txt')
    c = run_simulation_evolved(infected, pos, 10000000)
    print(f'Part 2: {c}')


if __name__ == '__main__':
    main()
