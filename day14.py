from functools import reduce
import re
import sys
from typing import List


puzzle_input = [line.strip('\n') for line in sys.stdin]
robot_description = [list(map(int, re.findall("(-?\\d+)", line))) for line in puzzle_input]
width, height = 101, 103


def generate_new_field() -> List[List[List[int]]]:
    return [[[] for i in range(width)] for i in range(height)]


# 1)
old_field = generate_new_field()
robot_directions = {}

# initialize field
for num, robot in enumerate(robot_description):
    old_field[robot[1]][robot[0]].append(num)
    robot_directions[num] = (robot[2], robot[3])

# move robots
for _ in range(100):
    new_field = generate_new_field()

    for i in range(height):
        for j in range(width):
            for robot in old_field[i][j]:
                x, y = robot_directions[robot]
                new_field[(i + y) % height][(j + x) % width].append(robot)

    old_field = new_field

# count robots in quadrants
quadrants = [((0, (height // 2)), (0, (width // 2))),
             ((0, (height // 2)), ((width // 2) + 1, width)),
             (((height // 2) + 1, height), (0, width // 2)), 
             (((height // 2) + 1, height), ((width // 2) + 1, width))]

quadrant_counts = []
for q in quadrants:
    count = 0

    for i in range(q[0][0], q[0][1]):
        for j in range(q[1][0], q[1][1]):
            count += len(new_field[i][j])

    quadrant_counts.append(count)

result_1 = reduce(lambda a,b: a * b, quadrant_counts, 1)
print(result_1)
