import operator
import re


Particle = ((int, int, int), (int, int, int), (int, int, int))


def parse_input(filename) -> list[Particle]:
    with open(filename) as file:
        return [tuple(tuple(map(int, parts.split(','))) for parts in re.findall(r'(?<=<).*?(?=>)', line))
                for line in file]


def update_particle(particle: Particle) -> Particle:
    vel = tuple(map(operator.add, particle[1], particle[2]))
    pos = tuple(map(operator.add, particle[0], vel))
    return pos, vel, particle[2]


def main():
    particles = parse_input('data.txt')
    idx = -1
    c = 0
    while c < 300:
        particles = [update_particle(p) for p in particles]
        dists = [sum(abs(coord) for coord in p[0]) for p in particles]
        new_idx = dists.index(min(dists))
        c = 0 if new_idx != idx else c + 1
        idx = new_idx
    print(f'Part 1: {idx}')

    particles = parse_input('data.txt')
    c = 0
    while c < 50:
        colliding = set()
        for i, lhs in enumerate(particles):
            for rhs in particles[i + 1:]:
                if lhs[0] == rhs[0]:
                    colliding.add(lhs[0])
                    break
        particles = [update_particle(p) for p in particles if p[0] not in colliding]
        c = c + 1 if not colliding else 0
    print(f'Part 2: {len(particles)}')


if __name__ == '__main__':
    main()
