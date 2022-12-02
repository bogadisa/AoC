
win_scores = ["X", "Y", "Z", "X", "Y", "Z"]
choose = ["A", "B", "C", "A", "B", "C"]
def simulate(opponent, you, part2=False):
    base_score = win_scores.index(you) + 1
    if not(part2):
        if opponent == "A":
            if you == "X":
                return base_score + 3 
            elif you == "Y":
                return base_score + 6 
            else:
                return base_score + 0 
        elif opponent == "B":
            if you == "X":
                return base_score + 0 
            elif you == "Y":
                return base_score + 3 
            else:
                return base_score + 6 
        elif opponent == "C":
            
            if you == "X":
                return base_score + 6 
            elif you == "Y":
                return base_score + 0 
            else:
                return base_score + 3 
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
    score1 = 0
    score2 = 0
    for line in lines:
        score1 += simulate(line[0], line[2], part2=False)
        score2 += simulate(line[0], line[2], part2=True)

    print(score1)
    print(score2)