#Find All Occurrences of a Pattern in a String
filename = input()
with open(filename) as file:
    lines = [line.rstrip() for line in file]

string = lines[1]
pattern = lines[0]

res = []
for i in range(len(string)):
    if string[i:(i+len(pattern))] == pattern:
        res.append(i)

result = ' '.join(map(str, res))
with open("BA1D_res.txt", "w") as f:
    f.write(result)