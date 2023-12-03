import re
import math
from collections import defaultdict


total = 0
board = []
gearNums = defaultdict(list)

for line in open("./input.txt").readlines():
    board.append(line.strip())

def considerNumberNeighbors(startY, startX, endY, endX, num):
    global gearNums
    for y in range(startY, endY + 1):
        for x in range(startX, endX + 1):
            if y >= 0 and y < len(board) and x >= 0 and x < len(board[y]):
                if board[y][x] not in "0123456789.":
                    if board[y][x] == "*":
                        gearNums[(y, x)].append(num)
                    return True
    return False


numPattern = re.compile("\d+")

for rowNum in range(len(board)):
    for match in re.finditer(numPattern, board[rowNum]):
        if considerNumberNeighbors(
            rowNum - 1,
            match.start() - 1,
            rowNum + 1,
            match.end(),
            int(match.group(0)),
        ):
            total += int(match.group(0))

print(total)

ratTotal = 0
for k, v in gearNums.items():
    if len(v) == 2:
        ratTotal += v[0] * v[1]
print(ratTotal)
