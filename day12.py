from collections import defaultdict, deque
import operator
import sys
from typing import List, Tuple


farm = [line.strip('\n') for line in sys.stdin]


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
def price_for_region_2(region: List[Tuple[str, Tuple[int, int]]]) -> int:
    _, farm_fields = region
    area = len(farm_fields)

    min_i = min(farm_fields, key=lambda x: x[0])[0]
    max_i = max(farm_fields, key=lambda x: x[0])[0]
    min_j = min(farm_fields, key=lambda x: x[1])[1]
    max_j = max(farm_fields, key=lambda x: x[1])[1]

    i_size = max_i - min_i + 3
    j_size = max_j - min_j + 3

    field = [[False for _ in range(j_size)] for _ in range(i_size)]

    for (i, j) in farm_fields:
        field[i - min_i + 1][j - min_j + 1] = True


    def get_sides(f: List[List[bool]]) -> int:
        sides = 0
        
        iterations = len(f) - 1
        for k in range(iterations):
            first = f[k]
            second = f[k+1]
            currently_top_side = False
            currently_bottom_side = False
            for i in range(len(first)):
                if currently_top_side and (not second[i] or not (first[i] ^ second[i])):
                    sides += 1
                    currently_top_side = False
                if currently_bottom_side and (not first[i] or not (first[i] ^ second[i])):
                    sides += 1 
                    currently_bottom_side = False
                if not currently_top_side and not first[i] and second[i]:
                    currently_top_side = True
                if not currently_bottom_side and first[i] and not second[i]:
                    currently_bottom_side = True

        return sides

    horizontally = get_sides(field)
    vertically = get_sides([[row[i] for row in field] for i in range(len(field[0]))])

    num_sides = horizontally + vertically

    return area * num_sides

result_2 = sum([(price_for_region_2(region)) for region in find_regions(farm)])
print(result_2)
