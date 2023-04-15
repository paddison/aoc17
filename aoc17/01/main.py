def read_data(filename: str) -> list[int]:
    digits = []
    with open(filename) as f:
        for c in f.readline():
            digits.append(int(c))
    return digits


def sum_digits(digits: list[int], offset: int) -> int:
    sums = 0
    for idx, digit in enumerate(digits):
        list_offset = calculate_offset(idx, offset, len(digits))
        if digit == digits[list_offset]:
            sums += digit
    return sums


def calculate_offset(idx: int, offset: int, length: int) -> int:
    return (idx + offset) % length


if __name__ == "__main__":
    data = read_data("data.txt")
    print(sum_digits(data, 1))
    print(sum_digits(data, len(data) // 2))
