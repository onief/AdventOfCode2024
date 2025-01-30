import copy
from functools import reduce
import re
import sys
from typing import List


puzzle_input = [line.strip('\n') for line in sys.stdin]
robot_description = [list(map(int, re.findall("(-?\\d+)", line))) for line in puzzle_input]
width, height = 101, 103


def generate_new_field() -> List[List[List[int]]]:
    return [[[] for i in range(width)] for i in range(height)]


def move_robots(old_field: List[List[List[int]]]):
    new_field = generate_new_field()

    for i in range(height):
        for j in range(width):
            for robot in old_field[i][j]:
                x, y = robot_directions[robot]
                new_field[(i + y) % height][(j + x) % width].append(robot)

    return new_field


# Initialize field
start_field = generate_new_field()
robot_directions = {}

for num, robot in enumerate(robot_description):
    start_field[robot[1]][robot[0]].append(num)
    robot_directions[num] = (robot[2], robot[3])


# 1)
old_field = copy.deepcopy(start_field)
for _ in range(100):
    new_field = move_robots(old_field)
    old_field = new_field

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


# 2)
def print_field(field: List[List[List[int]]]):
    for width_level in field:
        line_str = "".join(["x" if place else "." for place in width_level])
        print(line_str)


# Re-Open stdin
try:
    sys.stdin = open("/dev/tty")
except FileNotFoundError:
    sys.stdin = open("CON", "r")  

iterations = 0
continue_moving = True
while continue_moving:
    positions = [(i, j) for i in range(height) for j in range(width) if new_field[i][j]]
    surrounding = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    
    enough_neighbours = 0
    for y, x in positions:
        neighbour_count = 0

        for i, j in surrounding:
            try:
                if new_field[y + i][x + j]:
                    neighbour_count += 1
            except:
                pass

        if neighbour_count >= 2:
            enough_neighbours += 1

    # Funky Hyperparameter
    if enough_neighbours >= len(robot_description) * 0.4:
        print_field(start_field)
        if input("Is it a Tree? No -> Enter nothing, Yes -> Enter Something:") != "":
            continue_moving = False
            result_2 = iterations
            print(result_2)
    
    new_field = move_robots(start_field)
    start_field = new_field
    iterations += 1
