from collections import deque
from functools import reduce
import sys
from typing import Deque, Dict, List, Set, Tuple


inputs = [line.strip("\n") for line in sys.stdin]

split = inputs.index('')
rules = [[int(x) for x in r.split('|')] for r in inputs[:split]]
orderings = [[int(x) for x in o.split(',')] for o in inputs[split+1:]]


def create_graph(nodes: Set[int], rules: List[Tuple[int, int]]) -> Dict[(int, List[int])]:
    graph = {}
    
    for u in nodes:
        graph[u] = []

    for (u, v) in rules:
        if u in nodes and v in nodes:
            graph[u].append(v)

    return graph


def create_topol_sorting(nodes: Set[int], graph: Dict[(int, List[int])]) -> Deque[int]:
    result = deque([])
    marked = set()
    temp_marked = set()

    def visit(node: int):
        if node in marked:
            return
        
        if node in temp_marked:
            raise Exception("why is it cyclic?")
        
        temp_marked.add(node)
        
        for neighbour in graph[node]:
            visit(neighbour)
        
        marked.add(node)
        result.appendleft(node)

    for node in nodes:
        if node not in marked:
            visit(node)
            temp_marked = set()
    
    return result


def check_and_eval_ordering(ordering: List[int], topol_sorting: Dict[(int, int)]) -> Tuple[int, int]:
    sort_of_order = [topol_sorting[u] for u in ordering]

    task1, task2 = 0, 0

    if all(sort_of_order[i] < sort_of_order[i+1] for i in range(len(sort_of_order) - 1)):
        task1 = ordering[len(ordering) // 2]
    else:
        sorted_ordering = sorted(ordering, key=lambda u: topol_sorting[u])
        task2 = sorted_ordering[len(sorted_ordering) // 2]

    return task1, task2

# 1 + 2)

def eval_ordering(ordering: List[int]) -> Tuple[int, int]:
    nodes = set(ordering)
    graph = create_graph(nodes, rules)
    topol_sorting = create_topol_sorting(nodes, graph)
    sorting_dict = {u: topol_sorting.index(u) for u in topol_sorting} 
    return check_and_eval_ordering(ordering, sorting_dict)

result1, result2 = reduce(lambda a, b: (a[0]+b[0], a[1]+b[1]), map(eval_ordering, orderings))
print(result1)
print(result2)
