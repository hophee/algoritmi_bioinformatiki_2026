#Find a Position in a Genome Minimizing the Skew

def skew_calc(genome):
    skew = 0
    skews = []
    for letter in genome:
        skews.append(skew)
        if letter == 'C': skew -= 1
        if letter == 'G': skew += 1
    skews.append(skew)
    min_val = min(skews)
    return [i for i, x in enumerate(skews) if x == min_val]

print(skew_calc('CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG'))