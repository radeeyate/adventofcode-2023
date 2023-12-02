inputList = open("./input.txt", "r").read().splitlines()


# part one answer
partOneAnswer = 0
for line in inputList:
    digitsInLine = []
    for value in list(line):
        if value.isnumeric():
            digitsInLine.append(value)
    partOneAnswer += int(digitsInLine[0] + digitsInLine[-1])
print("part one answer:", partOneAnswer)

partTwoAnswer = 0
spelledNumbers = {
    "oneight": "oneeight",
    "threeight": "threeeight",
    "fiveight": "fiveeight",
    "nineight": "nineeight",
    "twone": "twoone",
    "sevenine": "sevennine",
    "eightwo": "eighttwo",
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
for line in inputList:
    digitsInLine = []
    wordDigits = []
    for word, number in spelledNumbers.items():
        if word in line:
            line = line.replace(word, str(number))
    for value in list(line):
        if value.isnumeric():
            digitsInLine.append(value)
    partTwoAnswer += int(digitsInLine[0] + digitsInLine[-1])
print("part two answer:", partTwoAnswer)
