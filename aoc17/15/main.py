from itertools import islice


def next_value(n: int, factor: int, mod: int = 1):
    while True:
        n = n * factor % 2147483647
        if n % mod == 0:
            yield n & 0xffff


def main():
    a, b = (618, 814)
    a_factor, b_factor = 16807, 48271
    print(
        sum(1 for left, right in islice(
            zip(next_value(a, a_factor), next_value(b, b_factor)), 40000000
        ) if left == right)
    )
    print(
        sum(1 for left, right in islice(
            zip(next_value(a, a_factor, 4), next_value(b, b_factor, 8)), 5000000
        ) if left == right)
    )


if __name__ == '__main__':
    main()
