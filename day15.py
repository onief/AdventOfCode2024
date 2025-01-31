import sys
from typing import List, Tuple


puzzle_input = [line.strip('\n') for line in sys.stdin]
split_index = puzzle_input.index("")

warehouse = [list(line) for line in puzzle_input[:split_index]]
directions = "".join(puzzle_input[split_index:])

direction_map = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def print_warehouse(x):
    for e in x:
        print(e)


def find_robot(warehouse: List[List[str]]) -> Tuple[int, int]:
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            if warehouse[i][j] == "@":
                return (i, j)
            

def move(robot: Tuple[int, int], warehouse: List[List[str]], direction: str) -> List[List[str]]:
    if warehouse[robot[0]][robot[1]] != "@":
        robot = find_robot(warehouse)
    pass

print_warehouse(warehouse)
print(directions)
