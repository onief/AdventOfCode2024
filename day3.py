from functools import reduce
import re
import sys
from typing import List, Tuple

inputs = [line for line in sys.stdin]

def get_mul_pairs(line: str) -> List[Tuple[int, int]]:
    all_mul_expressions = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)", line)
    remove_junk = [re.sub("\\)", "", re.sub("mul\\(", "", x)) for x in all_mul_expressions]
    return [tuple(map(lambda x: int(x), elem.split(","))) for elem in remove_junk]

def get_result_for_valid_lines(input: List[str]) -> int:
    mul_pairs = map(lambda line: get_mul_pairs(line), input)
    flatten = [pair for line in mul_pairs for pair in line]
    return sum([pair[0] * pair[1] for pair in flatten])


# 1)
result1 = get_result_for_valid_lines(inputs)
print(result1)


# 2)
full_input = reduce(lambda line1, line2: line1 + line2, inputs)
do_split = full_input.split("do()")
remove_dont_parts = [do_expr.split("don't()")[0] for do_expr in do_split]

result2 = get_result_for_valid_lines(remove_dont_parts)
print(result2)
