# Advent of Code 2022 Day3

lowerletters = [chr(i) for i in range(97, 123)]
lower = dict(zip(lowerletters, range(1, 27)))
upperletters = [chr(i) for i in range(65, 91)]
upper = dict(zip(upperletters, range(27, 53)))
Encoder = lower | upper


def convert(x):
    NumberList = []
    for letter in x:
        new = Encoder[letter]
        NumberList.append(new)
    return NumberList


# part 1
# with open('Day3input.txt', 'r') as data:
#     total = 0
#     for sack in data:
#         stripped = sack.strip()
#         CompSize = int(len(stripped) / 2)
#         Comp1 = stripped[:CompSize]
#         Comp2 = stripped[CompSize:]
#         Numbers1 = convert(Comp1)
#         Numbers2 = convert(Comp2)
#         Shared = list(set(Numbers1) & set(Numbers2))[0] #Assumes there will only be one shared element
#         print(Shared)
#         total = total + Shared
#     print('The total sum is : ' + str(total))


# part 2
with open('Day3input.txt', 'r') as data:
    i = 0 #counter
    y = data.readlines()
    LineList = []
    for line in y: #Getting rid of newline characters/whitespace
        new = line.strip()
        LineList.append(new)
    x = len(LineList) #limit
    total = 0
    while i < x:
        Line1 = LineList[i]
        Line2 = LineList[i + 1]
        Line3 = LineList[i + 2]
        Numbers1 = convert(Line1)
        Numbers2 = convert(Line2)
        Numbers3 = convert(Line3)
        Shared = list(set(Numbers1) & set(Numbers2) & set(Numbers3))[0]
        total = total + Shared
        i = i + 3
    print('The total sum is : ' + str(total))
