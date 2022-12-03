import string
import numpy as np

filename = "inventory.txt"  

with open(filename, "r") as f:
    s1 = 0
    s2 = 0
    lines = f.readlines()
    for i, line in enumerate(lines):
        size = len(line.strip())//2
        rucksack = [((string.ascii_lowercase.index(c.lower())+1) + c.isupper()*26)/line[:size].count(c) for c in line[:size] if c in line[size:]]
        s1 += sum(rucksack)
        if i%3 == 0:
            group = [((string.ascii_lowercase.index(c.lower())+1) + c.isupper()*26)/line.count(c) for c in line.strip() if c in lines[i+1] and c in lines[i+2]]
            s2 += np.sum(group)
    print(int(s1))
    print(int(s2))