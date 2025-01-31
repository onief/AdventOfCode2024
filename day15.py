import sys
from typing import List, Tuple


puzzle_input = [line.strip('\n') for line in sys.stdin]
split_index = puzzle_input.index("")

warehouse_map = [list(line) for line in puzzle_input[:split_index]]
directions = "".join(puzzle_input[split_index:])


class Warehouse:

    def __init__(self, warehouse_map: List[List[str]]):
        self.map = warehouse_map
        self.direction_map = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    def __str__(self) -> str:
        return "".join(["".join(row) + "\n" for row in self.map])


    def find_robot(self) -> Tuple[int, int]:
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == "@":
                    return (i, j)
            

    def push(self, current: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
        
        obj = self.map[current[0]][current[1]]
        new_i, new_j = current[0] + direction[0], current[1] + direction[1]
        target = self.map[new_i][new_j]

        if target == "#":
            return current
        elif target == ".":
            self.map[new_i][new_j] = obj
            self.map[current[0]][current[1]] = "."
            return (new_i, new_j)
        else:
            push_result = self.push((new_i, new_j), direction)
            if push_result == (new_i, new_j):
                return current
            elif push_result == (new_i + direction[0], new_j + direction[1]):
                self.map[new_i][new_j] = obj
                self.map[current[0]][current[1]] = "."
                return (new_i, new_j)        


    def move(self, robot: Tuple[int, int], direction: str) -> Tuple[int, int]:
        if self.map[robot[0]][robot[1]] != "@":
            robot = self.find_robot()

        robot = self.push(robot, self.direction_map[direction])
        return robot
    

    def get_score(self) -> int:
        return sum([100 * i + j for i in range(len(self.map)) for j in range(len(self.map[0])) if self.map[i][j] == "O"])



# 1)
warehouse = Warehouse(warehouse_map)
robot = warehouse.find_robot()

for d in directions:
    robot = warehouse.move(robot, d)

result_1 = warehouse.get_score()
print(result_1)
