import sys
from collections import Counter

inputs = [line.split() for line in sys.stdin]

# 1)
left = sorted([int(x[0]) for x in inputs])
right = sorted([int(x[1]) for x in inputs])

pairs = zip(left, right)
result1 = sum([abs(x - y) for (x, y) in pairs])
print(result1)

# 2)
right_counts = Counter(right)
result2 = sum([x * right_counts[x] for x in left])
print(result2)
