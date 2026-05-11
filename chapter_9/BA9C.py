# Construct the Suffix Tree of a String
# https://rosalind.info/problems/ba9c/

class Node:
    def __init__(self):
        self.edges = {}


def common_prefix_length(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return i


def add_suffix(root, suffix):
    node = root
    rest = suffix

    while rest:
        first = rest[0]
        if first not in node.edges:
            node.edges[first] = [rest, Node()]
            return

        label, child = node.edges[first]
        shared = common_prefix_length(label, rest)

        if shared == len(label):
            node = child
            rest = rest[shared:]
            continue

        middle = Node()
        old_label = label[shared:]
        new_label = rest[shared:]

        middle.edges[old_label[0]] = [old_label, child]
        if new_label:
            middle.edges[new_label[0]] = [new_label, Node()]

        node.edges[first] = [label[:shared], middle]
        return


def suffix_tree(text):
    root = Node()
    for i in range(len(text)):
        add_suffix(root, text[i:])
    return root


def collect_edge_labels(node, labels):
    for key in sorted(node.edges):
        label, child = node.edges[key]
        labels.append(label)
        collect_edge_labels(child, labels)


filename = input()
with open(filename) as f:
    text = f.read().strip()

root = suffix_tree(text)
labels = []
collect_edge_labels(root, labels)

with open("results_store/res_ba9c.txt", "w") as f:
    f.write("\n".join(labels))
