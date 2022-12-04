# Advent of Code Day1:

with open("Day1input.txt", "r") as Calories:
    Totals = []
    CurrentSum = 0
    lines = Calories.read().splitlines()
    last_line = lines[-1]
    for line in lines:
        if line == "":
            Totals.append(CurrentSum)
            CurrentSum = 0
        else:
            if line == last_line:
                CurrentSum = CurrentSum + int(line)
                Totals.append(CurrentSum)
            else:
                CurrentSum = CurrentSum + int(line)

MostCal = max(Totals)
print(MostCal)

# Part2
Totals.sort(reverse=True)
ThreeTopCal = Totals[0] + Totals[1] + Totals[2]
print(ThreeTopCal)
