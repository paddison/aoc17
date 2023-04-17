Instruction = (int, int, str)  # value_to_write, movement, next_state


def parse_input(filename: str) -> (str, int, dict[str, list[Instruction]]):
    with open(filename) as file:
        statemachine = dict()
        starting_state = file.readline().strip()[-2]
        iterations = int(file.readline().strip().split()[-2])
        file.readline()  # ignore empty line
        while True:
            state_line = file.readline().strip()
            if state_line == '':
                break
            state = state_line[-2]
            instructions = [None, None]
            for i in range(2):
                file.readline()  # ignore line for cur value == 0/1
                value_to_write = int(file.readline().strip()[-2])
                movement = 1 if file.readline().strip().split()[-1].startswith('right') else -1
                next_state = file.readline().strip()[-2]
                instructions[i] = (value_to_write, movement, next_state)
            statemachine[state] = instructions
            file.readline()  # ignore empty line

        return starting_state, iterations, statemachine


def main():
    current_state, iterations, statemachine = parse_input('data.txt')
    memory = dict()  # pos, value
    current_position = 0
    for _ in range(iterations):
        memory_value = memory.get(current_position, 0)
        value_to_write, movement, next_state = statemachine[current_state][memory_value]
        memory[current_position] = value_to_write
        current_position += movement
        current_state = next_state
    checksum = sum(v for v in memory.values())
    print(f'Part 1: {checksum}')


if __name__ == '__main__':
    main()
