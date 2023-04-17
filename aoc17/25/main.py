Instruction = (int, int, str)  # value_to_write, movement, next_state


def get_lines(filename: str) -> list[str]:
    with open(filename) as file:
        return list(reversed([line.strip() for line in file if line.strip() != '']))


def parse_lines(lines: list[str]) -> (str, int, dict[str, (Instruction, Instruction)]):
    statemachine = dict()
    starting_state = lines.pop()[-2]
    iterations = int(lines.pop().split()[-2])
    while lines:
        state = lines.pop()[-2]
        statemachine[state] = parse_instruction(lines), parse_instruction(lines)
    return starting_state, iterations, statemachine


def parse_instruction(lines: list[str]) -> Instruction:
    lines.pop()  # ignore line for cur value == 0/1
    value_to_write = int(lines.pop()[-2])
    movement = 1 if lines.pop().split()[-1].startswith('right') else -1
    next_state = lines.pop()[-2]
    return value_to_write, movement, next_state


def main():
    current_state, iterations, statemachine = parse_lines(get_lines('data.txt'))
    memory = dict()  # pos, value
    cursor = 0
    for _ in range(iterations):
        memory[cursor], movement, current_state = statemachine[current_state][memory.get(cursor, 0)]
        cursor += movement
    checksum = sum(v for v in memory.values())
    print(f'Part 1: {checksum}')


if __name__ == '__main__':
    main()
