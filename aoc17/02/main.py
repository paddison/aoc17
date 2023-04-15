def get_data(filename: str) -> list[list[int]]:
    with open(filename) as f:
        return [list(map(int, line.split())) for line in f]


def calculate_difference(nums: list[int]) -> int:
    return max(nums) - min(nums)


def get_division(data: list[int]) -> int:
    for left in data:
        for right in data:
            if left != right and left % right == 0:
                return left // right


if __name__ == "__main__":
    s = sum([calculate_difference(line) for line in get_data("data.txt")])
    print(s)
    s2 = sum([get_division(line) for line in get_data("data.txt")])
    print(s2)
