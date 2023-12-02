import re
import math

inputList = open("./input.txt").read().splitlines()
bag = {"green": 13, "blue": 14, "red": 12}
partOneAnswer = partTwoAnswer = 0

# I barely understand what I did here
for i, line in enumerate(inputList):
    data = re.findall("\\d+ \\w+", line)
    cubes = {"green": [], "blue": [], "red": []}
    game = [(int(number), color) for number, color in [game.split() for game in data]]

    if all(n <= bag[color] for n, color in game):
        partOneAnswer += i + 1
    for number, color in game:
        cubes[color].append(number)
        
    partTwoAnswer += math.prod([max(v) for v in cubes.values()])

print("part 1 answer:", partOneAnswer)
print("part 2 answer:", partTwoAnswer)
