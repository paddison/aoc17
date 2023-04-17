def parse_input(filename: str) -> list[(int, int)]:
    with open(filename) as file:
        return [(int(line.split('/')[0]), int(line.split('/')[1])) for line in file]


def follow_pipes(pipes: list[(int, int)], vals: list[(int, int)], current: int, s: int, length: int):
    length += 1
    for pipe in pipes:
        does_connect = connects(current, pipe)
        if does_connect != -1:
            new_pipes = pipes.copy()
            new_pipes.remove(pipe)
            new_s = s + pipe[0] + pipe[1]
            vals.append((new_s, length))
            follow_pipes(new_pipes, vals, pipe[does_connect], new_s, length)


def connects(current, rhs: (int, int)) -> int:
    return 1 if current == rhs[0] else 0 if current == rhs[1] else -1


def main():
    pipes = parse_input('data.txt')
    vals = []
    follow_pipes(pipes, vals, 0, 0, 0)
    print(f'Part 1: {max(vals, key=lambda t: t[0])[0]}')
    max_length = max(vals, key=lambda t: t[1])[1]
    max_pipes = [val[0] for val in vals if val[1] == max_length]
    print(f'Part 2: {max(max_pipes)}')


if __name__ == '__main__':
    main()
