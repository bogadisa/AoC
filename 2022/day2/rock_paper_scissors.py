
win_scores = ["X", "Y", "Z", "X", "Y", "Z"]
choose = ["A", "B", "C", "A", "B", "C"]
def simulate(opponent, you, part2=False):
    base_score = win_scores.index(you) + 1
    if not(part2):
        if choose[win_scores.index(you)] == choose[choose.index(opponent)]:
            return 3 + base_score
        elif choose[win_scores.index(you)] == choose[choose.index(opponent)+1]:
            return 6 + base_score
        else:
            return base_score
            
    elif part2:
        if you == "X":
            return simulate(opponent, win_scores[choose.index(opponent)+2])
        elif you == "Y":
            return simulate(opponent, win_scores[choose.index(opponent)])
        else:
            return simulate(opponent, win_scores[choose.index(opponent)+1])


filename = "strat.txt"  

with open(filename, "r") as f:
    lines = "  ".join(f.readlines()).split("  ")
    # print(lines)
    score1 = 0
    score2 = 0
    for line in lines:
        score1 += simulate(line[0], line[2], part2=False)
        score2 += simulate(line[0], line[2], part2=True)

    print(score1)
    print(score2)