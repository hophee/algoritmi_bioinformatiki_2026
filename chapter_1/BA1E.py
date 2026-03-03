#Find Patterns Forming Clumps in a String
def find_clumps(genome, k, L, t):
    clumps = set()
    n = len(genome)
    
    for i in range(n - L + 1):
        window = genome[i:i + L]
        
        kmer_counts = {}
        for j in range(len(window) - k + 1):
            kmer = window[j:j + k]
            kmer_counts[kmer] = kmer_counts.get(kmer, 0) + 1
        
        for kmer, count in kmer_counts.items():
            if count >= t:
                clumps.add(kmer)
    
    return clumps


filename = input()
with open(filename) as file:
    lines = [line.rstrip() for line in file]
genome = lines[0]
params = lines[1].split(' ')
k = int(params[0])
L = int(params[1])
t = int(params[2])

result = find_clumps(genome, k, L, t)
print(' '.join(sorted(result)))
