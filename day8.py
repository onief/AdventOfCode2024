from collections import defaultdict
from itertools import combinations
import operator
import sys


# grid = [list(line.strip("\n")) for line in sys.stdin]
f = open("input/day8")
grid = [list(line.strip("\n")) for line in f.readlines()]
f.close()

antenna_positions = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        sign = grid[i][j]
        if sign != '.':
            antenna_positions.setdefault(sign, []).append((i, j))

#print(antenna_positions)

for _, positions in antenna_positions.items(): 
    for combination in combinations(positions, 2):
        dist = tuple(map(operator.sub, combination[0], combination[1]))
        min_thing = min(map(abs, dist))
        rolf = [x for xx in [[tuple(map(operator.sub, combination[0], tuple(map(operator.mul, tuple(map(operator.sub, combination[0], combination[1])), (i, i))))), tuple(map(operator.add, combination[0], tuple(map(operator.mul, tuple(map(operator.sub, combination[0], combination[1])), (i, i)))))] for i in range(0, 2 * max(len(grid), len(grid[0])))] for x in xx]
        for i, j in rolf:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                grid[i][j] = '#'
        

resutlt_1 = len({location for add_sub_combination in [[tuple(map(operator.sub, combination[0], tuple(map(operator.mul, tuple(map(operator.sub, combination[0], combination[1])), (2, 2))))), tuple(map(operator.add, combination[0], tuple(map(operator.sub, combination[0], combination[1]))))] for _, positions in antenna_positions.items() for combination in list(combinations(positions, 2))] for location in add_sub_combination if 0 <= location[0] < len(grid) and 0 <= location[1] < len(grid[0])})
print(resutlt_1)

resutlt_2 = len({location for add_sub_combination in [[x for xx in [[tuple(map(operator.sub, combination[0], tuple(map(operator.mul, tuple(map(operator.sub, combination[0], combination[1])), (i, i))))), tuple(map(operator.add, combination[0], tuple(map(operator.mul, tuple(map(operator.sub, combination[0], combination[1])), (i, i)))))] for i in range(0, 2 * max(len(grid), len(grid[0])))] for x in xx] for _, positions in antenna_positions.items() for combination in list(combinations(positions, 2))] for location in add_sub_combination if 0 <= location[0] < len(grid) and 0 <= location[1] < len(grid[0])})
print(resutlt_2)
