#Find the Most Frequent Words in a String

#with open(filename) as file:
#    lines = [line.rstrip() for line in file]

def most_frequent_kmers(string, k):
    counts = {}
    for i in range(len(string) - k + 1):
        kmer = string[i:i+k]
        counts[kmer] = counts.get(kmer, 0) + 1
    max_count = max(counts.values())
    return [kmer for kmer, cnt in counts.items() if cnt == max_count]

string = input()
k = int(input())

print(' '.join(most_frequent_kmers(string, k)))