from aoc17.ten.main import knot_hash

INPUT = 'oundnydw'
TEST = 'flqrgnkx'


def create_input_strings(inp: str) -> list[str]:
    return [inp + f'-{i}' for i in range(128)]


def create_binary_map(inp: str) -> list[str]:
    return ['{0:0>128b}'.format(int(knot_hash(inp_str), 16)) for inp_str in create_input_strings(inp)]


def determine_subgroup(coords: set[(int, int)], row: int, col: int) -> set[(int, int)]:
    subgroup = {(row, col)}
    frontier = neighbours(coords, row, col)
    while frontier:
        row, col = frontier.pop()
        subgroup.add((row, col))
        frontier.extend(neighbours(coords, row, col))
    return subgroup


def neighbours(coords: set[(int, int)], row: int, col: int) -> list[(int, int)]:
    ns = list()
    for row, col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
        if (row, col) in coords:
            coords.remove((row, col))
            ns.append((row, col))
    return ns


def main():
    boolean_map = [[d == '1' for d in line] for line in create_binary_map(INPUT)]
    subgroups = list()
    coords = {(row, col) for row in range(128) for col in range(128) if boolean_map[row][col]}
    print(f'Part 1: {len(coords)}')
    while coords:
        row, col = coords.pop()
        subgroups.append(determine_subgroup(coords, row, col))
    print(f'Part 2: {len(subgroups)}')


if __name__ == '__main__':
    main()
