#Find the Reverse Complement of a String
filename = input()
with open(filename) as file:
    lines = [line.rstrip() for line in file]
string = lines[0]

comp = []
for s in string:
    if s == 'A': comp.append('T')
    if s == 'T': comp.append('A')
    if s == 'G': comp.append('C')
    if s == 'C': comp.append('G')

comp_reverse = ''.join(comp[::-1])

with open("BA1C_res.txt", "w") as f:
    f.write(comp_reverse)