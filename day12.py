from collections import defaultdict, deque
import operator
import sys
from typing import List, Tuple


# farm = [line.strip('\n') for line in sys.stdin]
f = open("smol.txt")
farm = [line.strip('\n') for line in f.readlines()]
f.close()


def find_regions(farm: List[str]) -> List[Tuple[str, List[Tuple[int, int]]]]:
    height = len(farm)
    width = len(farm[0])
    
    visited = [[False for _ in range(width)] for _ in range(height)]
    
    def bfs(start: Tuple[int, int], field_type: str) -> List[Tuple[int, int]]:
        region = [start]
        queue = deque([start])
        visited[start[0]][start[1]] = True
        while queue:
            node = queue.popleft()
            for neighbour in [tuple(map(operator.add, node, direction)) for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]]:
                i, j = neighbour
                if 0 <= i < height and 0 <= j < width and farm[i][j] == field_type and not visited[i][j]:
                    queue.append(neighbour)
                    region.append(neighbour)
                    visited[i][j] = True
        return region

    regions = [(farm[i][j], bfs((i, j), farm[i][j])) for i in range(height) for j in range(width) if not visited[i][j]]
    return regions


# 1)
def price_for_region_1(region: List[Tuple[str, Tuple[int, int]]], farm: List[str]) -> int:
    field_type, farm_fields = region
    area = len(farm_fields)
    
    perimeter = 0
    for field in farm_fields:
        for (i, j) in [tuple(map(operator.add, field, direction)) for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]]:
            if (not (0 <= i < len(farm))) or (not 0 <= j < len(farm[0])):
                perimeter += 1
            elif farm[i][j] != field_type:
                perimeter += 1
    
    return area * perimeter

result_1 = sum([(price_for_region_1(region, farm)) for region in find_regions(farm)])
print(result_1)


# 2)
def price_for_region_2(region: List[Tuple[str, Tuple[int, int]]], farm: List[str]) -> int:
    field_type, farm_fields = region
    area = len(farm_fields)
    
    print(field_type)
    print(farm_fields)

    def get_sides(idx: int) -> int:
        other_idx = abs(idx - 1)

        grouped_by_idx_slice = {} 
        for field in farm_fields:
            grouped_by_idx_slice.setdefault(field[idx], []).append(field)
        print(grouped_by_idx_slice)
        
        sides = 0
        for idx_slice in grouped_by_idx_slice.values():
            side_list = []
            for t in sorted(idx_slice, key=lambda x: x[other_idx]):
                if side_list:
                    if abs(side_list[-1][-1][other_idx] - t[other_idx]) <= 1:
                        side_list[-1].append(t)
                    else:
                        side_list.append([t])
                else:
                    side_list.append([t])
            sides += len(side_list)
        
        return sides

    num_sides = get_sides(0) + get_sides(1)

    return area * num_sides


for region in find_regions(farm):
    price_for_region_2(region, farm)
    print()
# result_2 = sum([(price_for_region_2(region, farm)) for region in find_regions(farm)])
# print(result_2)
