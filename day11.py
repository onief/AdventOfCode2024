from typing import List


stones = input().split(" ")

# 1 + 2)
def blink_stones(stones: List[str], amount: int) -> int:
    stone_dict = {}
    for stone in stones:
        stone_dict[stone] = 1


    for i in range(amount):
        new = {}
        for stone, amount in stone_dict.items():
            if stone == "0":
                new["1"] = new.setdefault("1", 0) + amount
            elif len(stone) % 2 == 0:
                first = str(int(stone[:len(stone)//2]))
                second = str(int(stone[len(stone)//2:]))
                new[first] = new.setdefault(first, 0) + amount
                new[second] = new.setdefault(second, 0) + amount
            else:
                mult = str(int(stone) * 2024)
                new[mult] = new.setdefault(mult, 0) + amount
        stone_dict = new
    
    return sum(stone_dict.values())

result_1 = blink_stones(stones, 25)
print(result_1)

result_2 = blink_stones(stones, 75)
print(result_2)