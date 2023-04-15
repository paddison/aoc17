class Instruction:

    def __init__(self, parts: list[str]):
        self.name = parts[0]
        self.op = parts[1]
        self.val = int(parts[2])
        self.cond = (parts[4], parts[5], int(parts[6]))

    def evaluate(self, registers: dict[str, int]) -> bool:
        reg, op, val = self.cond
        reg_val = registers.get(reg, 0)
        return eval(f'{reg_val} {op} {val}')

    def execute(self, registers: dict[str, int]) -> int:
        registers[self.name] = registers.get(self.name, 0) + self.val * (1 if self.op == 'inc' else -1)
        return abs(registers[self.name])


def parse_input(filename) -> list[(str, int, str)]:
    with open(filename) as file:
        return [Instruction(line.split()) for line in file]


def main():
    registers, my_max = dict(), 0
    for instruction in parse_input('data.txt'):
        if instruction.evaluate(registers):
            my_max = max(my_max, instruction.execute(registers))
    print(max(v for v in registers.values()))
    print(my_max)


if __name__ == '__main__':
    main()
