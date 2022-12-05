from copy import deepcopy

filename = "rearrangement_procedure.txt"  

with open(filename, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if line.strip()[0] == "1":
            cut_off = i
            break
    
    location_crate = [line.index(idx) for idx in line.split()]
    positions1 = []

    
    for i, idx in enumerate(location_crate):
        crates_i = []
        for line in lines[:cut_off]:
            if line[idx] != " ":
                crates_i.insert(0, line[idx])
        positions1.append(crates_i)

    positions2 = deepcopy(positions1)
    
    for line in lines[i+2:]:
        instructions = line.strip().split(" ")
        being_moved = []
        for i in range(int(instructions[1])):
            moving = positions1[int(instructions[3])-1].pop()
            positions1[int(instructions[5])-1].append(moving)
            moving2 = positions2[int(instructions[3])-1].pop()
            being_moved.append(moving2)

        positions2[int(instructions[5])-1].extend(reversed(being_moved))

    output1 = ""
    output2 = ""
    for i in range(len(positions1)):
        output1 += positions1[i][-1]
        output2 += positions2[i][-1]

    print(output1)
    print(output2)