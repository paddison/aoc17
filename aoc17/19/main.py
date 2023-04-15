def parse_input(filename: str) -> list[list[str]]:
    with open(filename) as file:
        return [[char for char in line.strip('\n')] for line in file]


def add_padding(pipes: list[list[str]]):
    m = max(len(row) for row in pipes)
    for row in pipes:
        while len(row) < m:
            row.append(' ')


def follow_pipes(pipes: list[list[str]]) -> (str, int):
    letters = list()
    row, col = 0, pipes[0].index('|')
    direction = 1, 0
    steps = 0
    while True:
        if pipes[row][col] == '+':
            direction = change_direction(pipes, row, col, direction)
        elif pipes[row][col].isalpha():
            letters.append(pipes[row][col])
        elif pipes[row][col] == ' ':
            return ''.join(letters), steps
        row += direction[0]
        col += direction[1]
        steps += 1


def change_direction(pipes: list[list[str]], row: int, col: int, direction: (int, int)) -> (int, int):
    if direction[1] == 0:  # check left or right
        if col + 1 < len(pipes[row]) and (pipes[row][col + 1] == '-' or pipes[row][col + 1].isalpha()):
            return 0, 1  # right
        else:
            return 0, -1  # left
    if row + 1 < len(pipes) and (pipes[row + 1][col] == '|' or pipes[row + 1][col].isalpha()):
        return 1, 0  # down
    return -1, 0  # up


def main():
    pipes = parse_input('data.txt')
    add_padding(pipes)
    letters, steps = follow_pipes(pipes)
    print(f'Part 1: {letters}')
    print(f'Part 2: {steps}')


if __name__ == '__main__':
    main()
