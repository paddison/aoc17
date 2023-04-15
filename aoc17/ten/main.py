from functools import reduce


def parse_input(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(digit) for digit in file.readline().split(',')]


def read_file(filename: str) -> str:
    with open(filename) as file:
        return file.readline()


def do_knot(position: int, length: int, nums: list[int]):
    list_length = len(nums)
    end = (position + length - 1) % list_length
    for _ in range(length // 2):
        nums[position], nums[end] = nums[end], nums[position]
        position = (position + 1) % list_length
        end = (end - 1 + list_length) % list_length


def do_round(nums: list[int], lengths: list[int], skip_size: int, position: int) -> (int, int):
    for length in lengths:
        do_knot(position, length, nums)
        position = (position + length + skip_size) % len(nums)
        skip_size += 1
    return position, skip_size


def create_sparse_hash(nums: list[int], lengths: list[int]):
    position = skip_size = 0
    for _ in range(64):
        position, skip_size = do_round(nums, lengths, skip_size, position)


def create_dense_hash(nums: list[int]) -> list[int]:
    chunks = [nums[i:i + 16] for i in range(0, len(nums), 16)]
    return [reduce(lambda acc, n: acc ^ n, chunk, 0) for chunk in chunks]


def to_hex_string(dense_hash: list[int]) -> str:
    return "".join(['{0:0>2x}'.format(n) for n in dense_hash])


def create_lengths(inp: str) -> list[int]:
    return [ord(c) for c in inp]


def knot_hash(inp: str) -> str:
    lengths = create_lengths(inp)
    lengths.extend([17, 31, 73, 47, 23])
    nums = [i for i in range(256)]
    create_sparse_hash(nums, lengths)
    dense_hash = create_dense_hash(nums)
    return to_hex_string(dense_hash)


def main():
    list_size = 256
    # part 1
    nums = [i for i in range(list_size)]
    do_round(nums, parse_input('data.txt'), 0, 0)
    print(nums[0] * nums[1])

    # part 2
    lengths = create_lengths(read_file('data.txt'))
    lengths.extend([17, 31, 73, 47, 23])
    nums = [i for i in range(list_size)]
    create_sparse_hash(nums, lengths)
    dense_hash = create_dense_hash(nums)
    print(to_hex_string(dense_hash))


if __name__ == '__main__':
    main()
