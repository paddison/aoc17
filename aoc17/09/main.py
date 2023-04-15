def parse_input(filename: str) -> list[str]:
    with open(filename) as file:
        return [line for line in file]


def determine_score(chars: str) -> (int, int):
    level = score = cursor = garbage_count = 0
    is_garbage = False

    while cursor < len(chars):
        if is_garbage and chars[cursor] != '!':
            garbage_count += 1
        match chars[cursor]:
            case '{':
                if not is_garbage:
                    level += 1
            case '}':
                if not is_garbage:
                    score += level
                    level -= 1
            case '!':
                cursor += 1
            case '<':
                is_garbage = True
            case '>':
                if is_garbage:
                    is_garbage = False
                    garbage_count -= 1
        cursor += 1

    return score, garbage_count


def main():
    for inp in parse_input('data.txt'):
        print(determine_score(inp))


if __name__ == '__main__':
    main()
