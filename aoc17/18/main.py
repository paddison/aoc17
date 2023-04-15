def parse_input(filename: str) -> list[[list[str]]]:
    with open(filename) as file:
        return [line.split() for line in file]


instructions = parse_input('data.txt')


def get_value(value: str, registers: dict[str, int]) -> int:
    return int(value) if not value.isalpha() else int(registers[value])


def do_math_instruction(registers: dict[str, int], instruction: list[str]):
    match instruction[0]:
        case 'set': registers[instruction[1]] = get_value(instruction[2], registers)
        case 'add': registers[instruction[1]] += get_value(instruction[2], registers)
        case 'mul': registers[instruction[1]] *= get_value(instruction[2], registers)
        case 'mod': registers[instruction[1]] %= get_value(instruction[2], registers)


def solve_one():
    registers = {instruction[1]: 0 for instruction in instructions if instruction[1].isalpha()}
    instruction_pointer = 0
    last_played = 0
    while True:
        instruction = instructions[instruction_pointer]
        jump = 1
        match instruction[0]:
            case 'snd': last_played = registers[instruction[1]]
            case 'rcv':
                if get_value(instruction[1], registers) != 0:
                    if last_played != 0:
                        break
            case 'jgz':
                if get_value(instruction[1], registers) > 0:
                    jump = get_value(instruction[2], registers)
            case _: do_math_instruction(registers, instruction)
        instruction_pointer += jump
    print(f'Part 1: {last_played}')


def run_program(instruction_pointer: int, registers: dict[str, int], rcv_buffer: list[int], send: int) -> (int, dict[str, int], int):
    snd_buffer = list()
    while True:
        instruction = instructions[instruction_pointer]
        jump = 1
        match instruction[0]:
            case 'snd':
                snd_buffer.append(get_value(instruction[1], registers))
                send += 1
            case 'rcv':
                if rcv_buffer:
                    registers[instruction[1]] = rcv_buffer.pop(0)
                else:
                    return instruction_pointer, snd_buffer, send
            case 'jgz':
                if get_value(instruction[1], registers) > 0:
                    jump = get_value(instruction[2], registers)
            case _: do_math_instruction(registers, instruction)
        instruction_pointer += jump


def solve_two():
    registers_a = {instruction[1]: 0 for instruction in instructions if instruction[1].isalpha()}
    registers_b = registers_a.copy()
    registers_a['p'], registers_b['p'] = 0, 1
    pointer_a = pointer_b = 0
    b_send = 0
    rcv_buffer_a = list()
    while True:
        pointer_a, rcv_buffer_b, _ = run_program(pointer_a, registers_a, rcv_buffer_a, 0)
        pointer_b, rcv_buffer_a, b_send = run_program(pointer_b, registers_b, rcv_buffer_b, b_send)
        if not (rcv_buffer_b or rcv_buffer_a):
            break
    print(f'Part 2: {b_send}')


def main():
    solve_one()
    solve_two()


if __name__ == '__main__':
    main()
