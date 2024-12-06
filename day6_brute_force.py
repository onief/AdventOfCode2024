import copy
import sys
from typing import List, Set, Tuple


# grid = [list(line.strip("\n")) for line in sys.stdin]
f = open("input/day6", "r")
grid = [list(line.strip("\n")) for line in f.readlines()]
f.close()


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

    def look_right(self) -> "Position":
        return Position(self.j, -self.i)
    

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


# unnecessary
# def mark_grid(grid: List[List[str]], position: Position, direction: Position):
#     marker = '-' if direction.i == 0 else '|'
#     grid_mark = grid[position.i][position.j]
    
#     combined_marker = None
#     if grid_mark == '.' or grid_mark == '^':
#         combined_marker = marker
#     elif grid_mark == marker:
#         combined_marker = marker
#     else:
#         combined_marker = '+'

#     grid[position.i][position.j] = combined_marker


def check_circle(grid: List[List[str]], position: Position, direction: Position, obstacle: Tuple[int, int], already_circle: Set[Tuple[int, int]]) -> bool:
    # grid = copy.deepcopy(grid)
    new_pos = Position(position.i, position.j)
    new_dir = Position(direction.i, direction.j)

    # obstacle = Position(new_pos.i + new_dir.i, new_pos.j + new_dir.j)
    if not Position(obstacle[0], obstacle[1]).is_valid(grid) or obstacle in already_circle:
        return False
    
    obstacle_marker = grid[obstacle[0]][obstacle[1]]
    grid[obstacle[0]][obstacle[1]] = '#'

    #big = len(new_grid) * len(new_grid[0]) * 10
    #iter_counter = 0

    pos_dir_visited = set()

    while new_pos.is_valid(grid) and (new_pos.i, new_pos.j, new_dir.i, new_dir.j) not in pos_dir_visited:
        # mark_grid(grid, new_pos, new_dir)
        new_pos + new_dir

        if not new_pos.is_valid(grid):
            break

        if grid[new_pos.i][new_pos.j] == '#':
            new_pos - new_dir
            # mark_grid(grid, new_pos, new_dir)
            pos_dir_visited.add((new_pos.i, new_pos.j, new_dir.i, new_dir.j))
            new_dir.rotate()
        
        #iter_counter += 1

    grid[obstacle[0]][obstacle[1]] = obstacle_marker

    if (new_pos.i, new_pos.j, new_dir.i, new_dir.j) in pos_dir_visited:
        already_circle.add(obstacle)
        return True
    else:
        return False
    

def check_circle_bruteforce(grid: List[List[str]], position: Position, direction: Position) -> bool:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if position.i != i or position.j != j:
                new_grid = grid.copy()
                new_grid[i][j] = '#'
                if run_throuh_grid(new_grid, position, direction)[1]:
                    return True
    

def run_throuh_grid(grid: List[List[str]], position: Position, direction: Position) -> Tuple[int, bool]:
    distinct_fields_visited = set()
    already_circle_plus_guard_start = set([(position.i, position.j)])
    circle_counter = 0

    pos_dir_visited = set()

    while position.is_valid(grid) and (position.i, position.j, direction.i, direction.j) not in pos_dir_visited:
        distinct_fields_visited.add((position.i, position.j))
        # mark_grid(grid, position, direction)

        # if check_circle_bruteforce(grid, position, direction, already_circle_plus_guard_start):
        #     circle_counter += 1
    
        position + direction

        if not position.is_valid(grid):
            break

        if grid[position.i][position.j] == '#':
            position - direction
            pos_dir_visited.add((position.i, position.j, direction.i, direction.j))
            # mark_grid(grid, position, direction)
            direction.rotate()

    cyclic = (position.i, position.j, direction.i, direction.j) in pos_dir_visited

    return len(distinct_fields_visited), cyclic


start = find_start(grid)
direction = Position(-1, 0)

# 1)
result_1, _ = run_throuh_grid(grid, Position(start.i, start.j), Position(direction.i, direction.j))
print(result_1)

# 2)
# Bruteforce it in:

print(len(grid), len(grid[0]))
result_2 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(i, j)
        if start.i != i or start.j != j:
            new_grid = copy.deepcopy(grid)
            new_grid[i][j] = '#'
            if run_throuh_grid(new_grid, Position(start.i, start.j), Position(direction.i, direction.j))[1]:
                result_2 += 1
print(result_2)
