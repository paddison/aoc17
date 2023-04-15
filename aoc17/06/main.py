def parse_input(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(blocks) for blocks in file.readline().split()]


def redistribute(blocks: list[int]) -> (int, int):
    seen = list()
    while blocks not in seen:
        seen.append(blocks.copy())
        max_blocks = max(blocks)
        idx = blocks.index(max_blocks)
        blocks[idx] = 0
        for i in range(max_blocks):
            blocks[(idx + i + 1) % len(blocks)] += 1
    return len(seen), len(seen) - seen.index(blocks)


def main():
    print(redistribute(parse_input('data.txt')))


if __name__ == '__main__':
    main()
