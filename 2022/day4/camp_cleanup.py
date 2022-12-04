import numpy as np

filename = "cleaning_sections.txt"  

with open(filename, "r") as f:
    overlap = 0
    contained = 0
    lines = f.readlines()
    for line in lines:
        pair = np.array([sections.split("-") for sections in line.strip().split(",")], dtype=int)
        max_i = np.argmax(pair[:, 1] - pair[:, 0])
        contained += set(pair[(max_i+1)%2]).issubset(range(pair[max_i, 0], pair[max_i, 1]+1))
        overlap += not(set(pair[(max_i+1)%2]).isdisjoint(range(pair[max_i, 0], pair[max_i, 1]+1)))

    print(contained)
    print(overlap)