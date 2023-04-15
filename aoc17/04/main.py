def parse_input(file_name: str) -> list[list[str]]:
    with open(file_name) as file:
        return [list(line.split()) for line in file]


def is_valid(passphrase: list[str]) -> bool:
    for i, phrase in enumerate(passphrase):
        for other_phrase in passphrase[i + 1:]:
            if phrase == other_phrase:
                return False
    return True


def is_valid_anagram(passphrase: list[str]) -> bool:
    for i, phrase in enumerate(passphrase):
        for other_phrase in passphrase[i + 1:]:
            if set(phrase) == set(other_phrase):
                return False
    return True


def main():
    inp = parse_input('data.txt')
    print(len(list(filter(is_valid, inp))))
    print(len(list(filter(is_valid_anagram, inp))))


if __name__ == '__main__':
    main()
