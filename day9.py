from itertools import chain
from typing import List


disk_map = enumerate(map(int, list(input())))
disk = list(chain.from_iterable([[i // 2] * elem if i % 2 == 0 else [-1] * elem for i, elem in disk_map]))

# 1)
def compact_task_1(disk: List[int]) -> List[int]:
    compacted_disk = disk.copy()
    last = len(compacted_disk) - 1
    for i in range(len(compacted_disk)):
        if i > last:
            break

        if compacted_disk[i] == -1:

            for j in range(last, 0, -1):
                if compacted_disk[j] != -1:
                    last = j
                    break

            compacted_disk[i], compacted_disk[last] = compacted_disk[last], -2
            last -= 1

    return compacted_disk

result_1 = sum([index * file_id for index, file_id in enumerate(compact_task_1(disk)) if file_id != -2 and file_id != -1])
print(result_1)

# 2)
def compact_task_2(disk: List[int]) -> List[int]:
    compacted_disk = disk.copy()

    last_file_id = None
    block = []
    already_moved = set()
    for i in range(len(compacted_disk)-1, 0, -1):
        file_id = compacted_disk[i]
        
        if not last_file_id:
            last_file_id = file_id
        elif file_id != last_file_id and last_file_id:
            last_file_id = file_id

            free_counter = 0 
            for j in range(len(compacted_disk)):
                if not block or j > i:
                    break
                elif compacted_disk[j] == -1:
                    free_counter += 1
                    if free_counter == len(block):
                        already_moved.add(block[0])
                        swapped = 0
                        for k in range(j-free_counter+1, j+1):
                            swapped += 1
                            compacted_disk[k] = block.pop()
                            compacted_disk[i+swapped] = -2
                else:
                    free_counter = 0
            
            block = []

        if file_id != -1 and file_id not in already_moved:
            block.append(file_id)
    
    return compacted_disk

result_2 = sum([index * file_id for index, file_id in enumerate(compact_task_2(disk)) if file_id != -2 and file_id != -1])
print(result_2)