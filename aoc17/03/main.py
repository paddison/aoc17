import math

PUZZLE_INPUT = 361527


def spiral():
    pos = (0, 0)
    adders = (1, 0)
    while True:
        pos = pos[0] + adders[0], pos[1] + adders[1]
        if pos[0] == pos[1] and pos[0] > 0:
            adders = (-1, 0)
        elif -pos[0] == pos[1] and pos[0] < 0:
            adders = (0, -1)
        elif pos[0] == pos[1] and pos[0] < 0:
            adders = (1, 0)
        elif pos[0] + pos[1] == 1 and pos[0] > 0:
            adders = (0, 1)
        yield pos


def calculate_numbers(nums: dict[(int, int), int], pos: [int, int]) -> int:
    return sum([nums.get((pos[0] + x, pos[1] + y), 0) for x in range(-1, 2) for y in range(-1, 2)])


def calculate_radius_n_root(n: int) -> int:
    root = math.sqrt(n)
    if int(root) == root and root % 2 == 1:
        return int(root)

    if int(root) % 2 == 0:
        return int(root) + 1

    return math.ceil(root) + 1


def calculate_radius(radius_n_root: int) -> int:
    return radius_n_root // 2


def calculate_position(n: int, radius_n: int, radius: int, ) -> (int, int):
    diff = radius_n - n
    # determine side and position on the side where number will be
    # 0 = down, 1 = left, 2 = up, 3 = right
    side = diff // (2 * radius)
    position = diff % (2 * radius)
    return calculate_coordinates(side, position, radius)


def calculate_coordinates(side: int, position: int, radius: int) -> (int, int):
    match side:
        case 0: return radius - position, -radius
        case 1: return -radius, -radius + position
        case 2: return -radius + position, radius
        case 3: return radius, radius - position


def manhattan(x: int, y: int) -> int:
    return abs(x) + abs(y)


def main():
    n = PUZZLE_INPUT
    radius_n_root = calculate_radius_n_root(n)
    radius_n = radius_n_root * radius_n_root
    radius = calculate_radius(radius_n_root)
    x, y = calculate_position(n, radius_n, radius)
    dist = manhattan(x, y)
    print(dist)
    nums = {(0, 0): 1}
    for next_pos in spiral():
        num = calculate_numbers(nums, next_pos)
        if num >= PUZZLE_INPUT:
            print(num)
            break
        nums[next_pos] = num


if __name__ == '__main__':
    main()
