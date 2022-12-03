import string

filename = "inventory.txt"  

with open(filename, "r") as f:
    s1 = 0
    s2 = 0
    lines = f.readlines()
    for i, line in enumerate(lines):
        size = len(line.strip())//2
        rucksack = [(string.ascii_lowercase.index(c.lower())+1) + c.isupper()*26 for c in line[:size] if c in line[size:]]
        s1 += rucksack[0]
        if i%3 == 0:
            group = [(string.ascii_lowercase.index(c.lower())+1) + c.isupper()*26 for c in line.strip() if c in lines[i+1] and c in lines[i+2]]
            s2 += group[0]
    print(int(s1))
    print(int(s2))