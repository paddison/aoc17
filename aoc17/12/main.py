def parse_input(filename: str) -> list[list[int]]:
    with open(filename) as file:
        return [list(map(int, line[line.find('>') + 1:].split(','))) for line in file]


def follow_programs(visited: set[int], programs: list[list[int]], current: int):
    if current in visited:
        return
    visited.add(current)
    for program in programs[current]:
        follow_programs(visited, programs, program)


def main():
    programs = parse_input('data.txt')
    all_sets = list()
    for current, program in enumerate(programs):
        for s in all_sets:
            if current in s:
                break
        else:
            visited = set()
            follow_programs(visited, programs, current)
            all_sets.append(visited)
    # part 1
    for s in all_sets:
        if 0 in s:
            print(len(s))
            break
    # part 2
    print(len(all_sets))


if __name__ == '__main__':
    main()
