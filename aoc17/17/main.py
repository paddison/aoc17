STEP_SIZE = 356
TEST = 3


def do_step(buffer: list[int], step_size: int, n: int, start: int) -> int:
    idx = (start + step_size) % len(buffer) + 1
    buffer.insert(idx, n)
    return idx


def main():
    buffer = [0]
    start = 0
    for n in range(1, 2018):
        start = do_step(buffer, STEP_SIZE, n, start)
    print(f'Part 1: {buffer[(start + 1) % len(buffer)]}')

    start = 0
    after_zero = 0
    for n in range(1, 50000001):
        start = (start + STEP_SIZE) % n + 1
        if start == 1:
            after_zero = n
    print(f'Part 2: {after_zero}')


if __name__ == '__main__':
    main()
