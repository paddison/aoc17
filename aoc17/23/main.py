def parse_input(filename: str) -> list[[str]]:
    with open(filename) as file:
        return [line.split() for line in file]


def get_registers() -> dict[str, int]:
    return {r: 0 for r in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']}


def get_value(registers: dict[str, int], val: str) -> int:
    return registers[val] if val.isalpha() else int(val)


def execute_instruction(instruction: list[str], registers: dict[str, int]) -> int:
    match instruction[0]:
        case 'set': registers[instruction[1]] = get_value(registers, instruction[2])
        case 'sub': registers[instruction[1]] -= get_value(registers, instruction[2])
        case 'mul': registers[instruction[1]] *= get_value(registers, instruction[2])
        case 'jnz':
            if get_value(registers, instruction[1]) != 0:
                return get_value(registers, instruction[2])
    return 1


def create_sieve(n: int) -> list[int]:
    sieve = [2]
    for i in range(2, n):
        for prime in sieve:
            if i % prime == 0:
                break
        else:
            sieve.append(i)
    return sieve


def main():
    instructions = parse_input('data.txt')
    registers = get_registers()
    pointer = 0
    i = 0
    mul_count = 0
    while len(instructions) > pointer >= 0:
        if instructions[pointer][0] == 'mul':
            mul_count += 1
        pointer += execute_instruction(instructions[pointer], registers)
        i += 1
    print(f'Part 1: {mul_count}')

    sieve = create_sieve(122701)
    non_primes = 0
    for n in range(105700, 122701, 17):
        if n not in sieve:
            non_primes += 1
    print(f'Part 2: {non_primes}')


if __name__ == '__main__':
    main()
