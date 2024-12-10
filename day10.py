from functools import reduce
import operator
import sys
from typing import List, Tuple


topographic_map = [list(map(int, line.strip('\n'))) for line in sys.stdin]


def find_trailheads(topographic_map: List[List[int]]) -> List[Tuple[int, int]]:
    return [(i, j) for i in range(len(topographic_map)) for j in range(len(topographic_map[0])) if topographic_map[i][j] == 0]


def hike(topographic_map: List[List[int]], start: Tuple[int, int], point: Tuple[int, int], last_height: int):
    if last_height == 9:
        return set([(start, point)]), 1
    new_points = [tuple(map(operator.add, point, direction)) for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]]
    valid_points = list(filter(lambda x: 0 <= x[0] < len(topographic_map) and 0 <= x[1] < len(topographic_map[0]), new_points))
    res_1, res_2 = set(), 0
    for i, j in valid_points:
        if topographic_map[i][j] == last_height + 1:
            point_pairs, count = hike(topographic_map, start, (i,j), last_height + 1)
            res_1.update(point_pairs)
            res_2 += count
    return res_1, res_2

hike_trailheads = [hike(topographic_map, trailhead, trailhead, 0) for trailhead in find_trailheads(topographic_map)]

result_1 = len(reduce(lambda a, b: a.union(b), map(lambda x: x[0], hike_trailheads)))
print(result_1)

result_2 = sum(map(lambda x: x[1], hike_trailheads))
print(result_2)