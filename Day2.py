# Advent of Code 2022 Day 2
# Part 1
# Scores Rock(A/X) - 1, Paper(B/Y) - 2, Scissor(C/Z) - 3, Loss - 0, Draw - 3, Win - 6.
def battle(x, y):
    score = 0
    if x == "A":
        match y:
            case "X":
                score = 4
            case "Y":
                score = 8
            case "Z":
                score = 3
    if x == "B":
        match y:
            case "X":
                score = 1
            case "Y":
                score = 5
            case "Z":
                score = 9
    if x == "C":
        match y:
            case "X":
                score = 7
            case "Y":
                score = 2
            case "Z":
                score = 6
    return score


with open("Day2input.txt", "r") as Strat:
    TotalScore = 0
    for game in Strat:
        played = [x for x in game.strip().split(" ")]
        points = battle(played[0], played[1])
        TotalScore = TotalScore + points
    print("Your final score is : " + str(TotalScore))

# Part 2
# X now means Lose, Y means Draw, Z means Win.


def battle2(x, y):
    score = 0
    if x == "A":
        match y:
            case "X":
                score = 3
            case "Y":
                score = 4
            case "Z":
                score = 8
    if x == "B":
        match y:
            case "X":
                score = 1
            case "Y":
                score = 5
            case "Z":
                score = 9
    if x == "C":
        match y:
            case "X":
                score = 2
            case "Y":
                score = 6
            case "Z":
                score = 7
    return score


with open("Day2input.txt", "r") as Strat2:
    TotalScore = 0
    for game in Strat2:
        played = [x for x in game.strip().split(" ")]
        points = battle2(played[0], played[1])
        TotalScore = TotalScore + points
    print("Your final score (part2) is : " + str(TotalScore))
