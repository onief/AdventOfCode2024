import sys
from typing import List


inputs = [list(map(int, line.replace(':', '').split())) for line in sys.stdin]


def find_combination(value_to_achieve: int, elems_to_combine: List[int], plus_concat: bool) -> int:
    
    if elems_to_combine[0] > value_to_achieve or (len(elems_to_combine) == 1 and elems_to_combine[0] != value_to_achieve):
        return 0
    
    elif len(elems_to_combine) == 1 and elems_to_combine[0] == value_to_achieve:
        return value_to_achieve
    
    else:
        add = find_combination(value_to_achieve, [elems_to_combine[0] + elems_to_combine[1]] + elems_to_combine[2:], plus_concat)
        mul = find_combination(value_to_achieve, [elems_to_combine[0] * elems_to_combine[1]] + elems_to_combine[2:], plus_concat)
        concat = find_combination(value_to_achieve, [int(str(elems_to_combine[0]) + str(elems_to_combine[1]))] + elems_to_combine[2:], plus_concat)
        if (add == mul != 0) or (add == concat != 0):
            return add
        elif (mul == concat != 0):
            return mul
        elif not plus_concat:
            return add + mul
        else:
            return add + mul + concat


# 1)
result_1 = sum([find_combination(calibration[0], calibration[1:], False) for calibration in inputs])
print(result_1)

# 2)
result_2 = sum([find_combination(calibration[0], calibration[1:], True) for calibration in inputs])
print(result_2)
