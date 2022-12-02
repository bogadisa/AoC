filename = "calories_per_elf.txt"

with open(filename, "r") as f:
    cals_per_elf = []
    info = f.read().replace("\n", "+").split("++")[:-1]
    for elf in info:
        cals_sum = 0
        for cals in elf.split("+"):
            cals_sum += int(cals)
        cals_per_elf.append(cals_sum)
    cals_per_elf.sort(reverse=True)

    print(max(cals_per_elf))
    print(sum(cals_per_elf[:3]))