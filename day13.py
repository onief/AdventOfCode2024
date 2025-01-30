import sys
import re
from typing import List
import numpy as np


def get_int_values_by_regex(regex: str, line: str) -> List[int]:
    return list(map(int, re.findall(regex, line)))


puzzle_input = list(enumerate([line.strip('\n') for line in sys.stdin if line.strip('\n')]))

values_by_line = [get_int_values_by_regex(r'=(\d+)', line) if i % 3 == 2 else get_int_values_by_regex(r'\+\d+', line) for (i, line) in puzzle_input]
grouped_input_values = [values_by_line[i:i+3] for i in range(0, len(values_by_line), 3)]

# 1)
solved_1 = [np.linalg.solve([[g[0][0], g[1][0]], [g[0][1], g[1][1]]], g[2]) for g in grouped_input_values]

result_1 = int(sum([np.round(result[0] * 3 + result[1] * 1) for result in solved_1 if np.all(np.isclose(result, np.round(result))) and result[0] <= 100 and result[1] <= 100]))
print(result_1)
