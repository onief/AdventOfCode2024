import copy
import sys
from typing import List, Set, Tuple


grid = [list(line.strip("\n")) for line in sys.stdin]


class Position:
    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j

    def __check_class(self, other):
        if not isinstance(other, Position):
            return NotImplemented

    def __add__(self, direction: "Position") -> "Position":
        self.__check_class(direction)
        self.i += direction.i
        self.j += direction.j
        return self
    
    def __sub__(self, direction: "Position") -> "Position":
        self.__check_class(direction)
        self.i -= direction.i
        self.j -= direction.j
        return self
    
    def __eq__(self, other: "Position"): 
        self.__check_class(other)
        return self.i == other.i and self.j == other.j
    
    def is_valid(self, grid: List[List[str]]) -> bool:
        return 0 <= self.i < len(grid) and 0 <= self.j < len(grid[0])
    
    def rotate(self):
        temp_i = self.i
        self.i = self.j
        self.j = -temp_i


def find_start(grid: List[List[str]]) -> Position:
    i, j = 0, 0

    for k in range(len(grid)):
        try:
            j = grid[k].index('^')
            i = k
            break
        except ValueError:
            continue

    return Position(i, j)


def run_throuh_grid(grid: List[List[str]], position: Position, direction: Position) -> Tuple[int, bool]:
    distinct_fields_visited = set()

    pos_dir_visited = set()

    while position.is_valid(grid) and (position.i, position.j, direction.i, direction.j) not in pos_dir_visited:
        distinct_fields_visited.add((position.i, position.j))
        position + direction

        if not position.is_valid(grid):
            break

        if grid[position.i][position.j] == '#':
            position - direction
            pos_dir_visited.add((position.i, position.j, direction.i, direction.j))
            direction.rotate()

    cyclic = (position.i, position.j, direction.i, direction.j) in pos_dir_visited

    return len(distinct_fields_visited), cyclic


start = find_start(grid)
direction = Position(-1, 0)

# 1)
result_1, _ = run_throuh_grid(grid, Position(start.i, start.j), Position(direction.i, direction.j))
print(result_1)

# 2)
# Bruteforce it in (might take some time xD):
result_2 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if start.i != i or start.j != j:
            new_grid = copy.deepcopy(grid)
            new_grid[i][j] = '#'
            if run_throuh_grid(new_grid, Position(start.i, start.j), Position(direction.i, direction.j))[1]:
                result_2 += 1
print(result_2)
