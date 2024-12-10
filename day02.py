import sys
from typing import List

inputs = [list(map(lambda x: int(x), line.split())) for line in sys.stdin]

# 1)
def is_ascending(number: int) -> int:
    if number > 0:
        return 1
    else:
        return -1

def is_safe_1(report: List[int]) -> bool:
    is_ascending_report = None
    previous_elem = None

    for elem in report:
        if not is_ascending_report and previous_elem:
            is_ascending_report = is_ascending(elem - previous_elem)

        if not previous_elem:
            previous_elem = elem
            continue
        
        if not (is_ascending_report == is_ascending(elem - previous_elem) and 1 <= abs(elem - previous_elem) <= 3):
            return False
        
        previous_elem = elem
    
    return True

result1 = sum([is_safe_1(report) for report in inputs])
print(result1)

# 2)
def is_safe_2(report: List[int]) -> bool:
    if is_safe_1(report):
        return True
    
    for i in range(len(report)):
        if is_safe_1(report[:i] + report[i+1:]):
            return True
    
    return False

result2 = sum([is_safe_2(report) for report in inputs])
print(result2)

