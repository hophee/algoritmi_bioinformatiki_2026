#Find the Most Frequent Words in a String
#with open(filename) as file:
#    lines = [line.rstrip() for line in file]

string = input()
k = int(input())

k_mers = []
def pattern_count(string, pattern):
    counter = 1
    for i in range((len(string) - len(pattern)+1)):
        if string[i:(i+len(pattern))] == pattern:
            counter+=1
    return int(counter)
for i in range(len(string) - k + 1):
    if string[i:(i+k)] not in k_mers:
        k_mers.append(string[i:(i+k)])

freqs = []
for ks in k_mers:
    freqs.append(pattern_count(string, ks))
idxes = []
for i in range(len(freqs)):
    if freqs[i] == max(freqs):
        idxes.append(i)


for id in idxes:
    print(k_mers[id])