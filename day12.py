from collections import deque
import operator
import sys
from typing import List, Tuple


# farm = [line.strip('\n') for line in sys.stdin]
f = open("input/day12")
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


def price_for_region(region: List[Tuple[str, Tuple[int, int]]], farm: List[str]) -> int:
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


print(sum([(price_for_region(region, farm)) for region in find_regions(farm)]))