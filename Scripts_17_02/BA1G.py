#Compute the Hamming Distance Between Two Strings

dna1 = 'GGGCCGTTGGT' #example. Comment reading file finction for correct input
dna2 = 'GGACCGTTGAC'

filename = input()
with open(filename) as file:
    lines = [line.rstrip() for line in file]
dna1 = lines[0]
dna2 = lines[1]

ham_dist = 0
for i in range(len(dna1)):
    if dna1[i] != dna2[i]: ham_dist += 1

print(ham_dist)