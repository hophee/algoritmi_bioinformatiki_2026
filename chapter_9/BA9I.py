# Construct the Burrows-Wheeler Transform of a String
# https://rosalind.info/problems/ba9i/

filename = input()
with open(filename) as f:
    text = f.read().strip()

rotations = sorted(text[i:] + text[:i] for i in range(len(text)))
bwt = ''.join(rotation[-1] for rotation in rotations)

with open("results_store/res_ba9i.txt", "w") as f:
    f.write(bwt)
