class Node:

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.children = list()

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'{self.name}: {self.weight} ({self.children})'


def parse_input(filename: str) -> (dict[str, int], dict[str, (set[str])]):
    children = dict()
    nodes = dict()
    with open(filename) as file:
        for line in file:
            parts = line.split()
            name = parts[0]
            weight = int(parts[1].strip('()'))
            nodes[name] = weight
            if "->" in parts:
                children[parts[0]] = set(child.strip(',') for child in parts[3:])
    return nodes, children


def parse_tree(name: str, nodes: dict[str, int], children: dict[str, (int, set[str])]) -> Node:
    weight = nodes[name]
    node = Node(name, weight)
    if name not in children:
        return node
    for child in children[name]:
        node.add_child(parse_tree(child, nodes, children))
    return node


def find_head(nodes: dict[str, int], children: dict[str, set[str]]) -> str:
    all_children = set(node for subtree in children.values() for node in subtree)
    return (set(nodes.keys()) - all_children).pop()


def calculate_weight_subtree(node: Node) -> int:
    return sum(calculate_weight_subtree(child) for child in node.children) + node.weight


def is_balanced(node: Node) -> bool:
    return len(set(calculate_weight_subtree(child) for child in node.children)) == 1


def get_unbalanced_child(node: Node) -> (Node, int):
    children = sorted(list((calculate_weight_subtree(child), child) for child in node.children), key=lambda c: -c[0])
    diff = abs(children[0][0] - children[1][0])
    return children[0][1], diff


def main():
    nodes, children = parse_input('data.txt')
    head = find_head(nodes, children)
    print(head)
    tree = parse_tree(head, nodes, children)
    while not is_balanced(tree):
        tree, diff = get_unbalanced_child(tree)
    print(tree.weight - diff)


if __name__ == '__main__':
    main()
