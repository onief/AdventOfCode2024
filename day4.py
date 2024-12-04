import sys
from typing import List, Tuple

inputs = [line.strip("\n") for line in sys.stdin]
rows = len(inputs)
columns = len(inputs[0])


# 1)
def find_x_s(lines: List[str]) -> List[Tuple[int, int]]:
    return [(i, j) for i in range(rows) for j in range(columns) if lines[i][j] == 'X']

def count_xmas_of_x(x: Tuple[int, int], data: List[str]) -> int:
    i, j = x
    to_check = [
        [(i, j), (i, j+1), (i, j+2), (i, j+3)], # right
        [(i, j), (i, j-1), (i, j-2), (i, j-3)], # left
        [(i, j), (i+1, j), (i+2, j), (i+3, j)], # up
        [(i, j), (i-1, j), (i-2, j), (i-3, j)], # down
        [(i, j), (i+1, j+1), (i+2, j+2), (i+3, j+3)], # right_up
        [(i, j), (i-1, j+1), (i-2, j+2), (i-3, j+3)], # right_down
        [(i, j), (i+1, j-1), (i+2, j-2), (i+3, j-3)], # left_up
        [(i, j), (i-1, j-1), (i-2, j-2), (i-3, j-3)] # left_down
    ]
    possible_xmas = [''.join([data[i][j] for (i, j) in direction if 0 <= i < rows and 0 <= j < columns]) for direction in to_check]

    return sum(1 for elem in possible_xmas if elem == 'XMAS')

result1 = sum(count_xmas_of_x(x, inputs) for x in find_x_s(inputs))
print(result1)


# 2)
def eval_x_shaped_mas(top_left: Tuple[int, int], data: List[str]) -> int:
    i, j = top_left
    shape = [
        (i+1, j+1),           # middle
        (i, j), (i, j+2),     # top
        (i+2, j), (i+2, j+2)  # bottom
    ]
    possible_mas_x = ''.join([data[i][j] for (i, j) in shape])

    if (possible_mas_x[0] == 'A') and \
       (possible_mas_x.count('M') == possible_mas_x.count('S') == 2) and \
       (possible_mas_x[1] != possible_mas_x[4] and possible_mas_x[2] != possible_mas_x[3]):
        return 1
    else:
        return 0

result2 = sum(eval_x_shaped_mas((i, j), inputs) for i in range(rows-2) for j in range(columns-2))
print(result2)
