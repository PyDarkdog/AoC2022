# Advent of Code 2022 Day4

# part1
with open('Day4input.txt', 'r') as data:
    counter = 0
    for pair in data:
        pairs = [x for x in pair.strip().split(",")]
        assignment1 = pairs[0].split("-")
        assignment2 = pairs[1].split("-")
        assignment1max = int(assignment1[1])
        assignment1min = int(assignment1[0])
        assignment1len = assignment1max - assignment1min
        assignment2max = int(assignment2[1])
        assignment2min = int(assignment2[0])
        assignment2len = assignment2max - assignment2min
        if assignment1len == assignment2len:
            if assignment1max == assignment2max:
                counter = counter + 1
            else:
                pass
        if assignment1len > assignment2len:
            if (assignment1max >= assignment2max) and (assignment1min <= assignment2min):
                counter = counter + 1
            else:
                pass
        if assignment1len < assignment2len:
            if (assignment2max >= assignment1max) and (assignment2min <= assignment1min):
                counter = counter + 1
            else:
                pass
    print("total number of fully encompassed assignment pairs is : " + str(counter))

#[Part 2]
with open('Day4input.txt', 'r') as data:
    counter = 0
    for pair in data:
        pairs = [x for x in pair.strip().split(",")]
        assignment1 = pairs[0].split("-")
        assignment2 = pairs[1].split("-")
        assignment1max = int(assignment1[1])
        assignment1min = int(assignment1[0])
        assignment1len = assignment1max - assignment1min
        assignment2max = int(assignment2[1])
        assignment2min = int(assignment2[0])
        assignment2len = assignment2max - assignment2min
        if assignment1max < assignment2min:
            pass
        elif assignment2max < assignment1min:
            pass
        else:
            counter = counter + 1
    print("Number of ANY overlapping work is : " + str(counter))
