# Implement TrieMatching
# https://rosalind.info/problems/ba9b/

def trie_construction(patterns):
    trie = [{}]
    terminal = [False]

    for pattern in patterns:
        node = 0
        for symbol in pattern:
            if symbol not in trie[node]:
                trie[node][symbol] = len(trie)
                trie.append({})
                terminal.append(False)
            node = trie[node][symbol]
        terminal[node] = True

    return trie, terminal


def prefix_trie_matching(text, start, trie, terminal):
    node = 0
    i = start

    while True:
        if terminal[node]:
            return True
        if i == len(text):
            return False

        symbol = text[i]
        if symbol not in trie[node]:
            return False

        node = trie[node][symbol]
        i += 1


filename = input()
with open(filename) as f:
    lines = [line.strip() for line in f if line.strip()]

text = lines[0]
patterns = lines[1:]

trie, terminal = trie_construction(patterns)
positions = []

for i in range(len(text)):
    if prefix_trie_matching(text, i, trie, terminal):
        positions.append(i)

with open("results_store/res_ba9b.txt", "w") as f:
    f.write(" ".join(map(str, positions)))
