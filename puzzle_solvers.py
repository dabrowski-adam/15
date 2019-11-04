from collections import defaultdict
from collections import deque
from functools import reduce
from itertools import chain
from math import inf

from puzzle_utils import Puzzle
from state_vertex import StateVertex
from utils import first_true


# # # # # # # # # # # # #
# breadth-first search
#

def bfs(puzzle: Puzzle, order: str):
    root = StateVertex(puzzle)
    visited, stack = {root}, deque([root])

    while stack:
        vertex = stack.popleft()
        if vertex.is_solved():
            return vertex.path()

        for neighbor in vertex.neighbors(order):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return None


# # # # # # # # # # # # #
# depth-first search
#

def dfs(puzzle: Puzzle, order: str):
    raise NotImplementedError


# # # # # # # # # # # # #
# iterative deepening DFS
#

def _dls(vertex, depth, order="R"):
    if depth == 0:
        return (vertex, True) if vertex.is_solved() else (None, True)

    results = [_dls(neighbor, depth - 1) for neighbor in vertex.neighbors(order)]
    found, remaining = zip(*results)
    return first_true(found, default=None), first_true(remaining)


def idfs(puzzle: Puzzle, order: str, max_depth=30):
    root = StateVertex(puzzle)

    for depth in range(max_depth + 1):
        found, remaining = _dls(root, depth, order=order)
        if found:
            return found.path()
        elif not remaining:
            return None


# # # # # # # # # # # # #
# best-first
#

def bf(puzzle: Puzzle, heuristic: int):
    raise NotImplementedError


# # # # # # # # # # # # #
# A*
#

def _d(current, neighbor):
    return len(neighbor.path())


def _dijkstra(vertex: StateVertex):
    return 0


# number of pieces out of place
def _hamming(vertex: StateVertex):
    puzzle = vertex.puzzle
    pieces = len(puzzle) * len(puzzle[0])

    solved = [*range(1, pieces), 0]
    current = list(chain(*puzzle))

    mismatches = [(a, b) for (a, b) in zip(solved, current) if a != b]
    return len(mismatches)


def _distance(p1, p2):
    y1, x1 = p1
    y2, x2 = p2
    return abs(y1 - y2) + abs(x1 - x2)


def _manhattan(vertex: StateVertex):
    puzzle = vertex.puzzle
    rows = len(puzzle)
    columns = len(puzzle[0])

    solved = [*range(1, rows * columns), 0]
    current = list(chain(*puzzle))

    positions = [(i // rows, i % columns) for i in range(rows * columns)]
    current_positions = dict(zip(current, positions))
    solved_positions = dict(zip(solved, positions))

    distances = [_distance(current_positions[n], solved_positions[n]) for n in range(rows * columns)]
    return sum(distances)


DIJKSTRA, HAMMING, MANHATTAN = 0, 1, 2

heuristics = {
    DIJKSTRA: _dijkstra,
    HAMMING: _hamming,
    MANHATTAN: _manhattan
}


def astar(puzzle: Puzzle, heuristic: int):
    h = heuristics[heuristic]
    root = StateVertex(puzzle)

    open_set = {root}
    # came_from = {}

    gscore = defaultdict(lambda: inf)
    gscore[root] = 0

    fscore = defaultdict(lambda: inf)
    fscore[root] = h(root)

    while open_set:
        current = reduce(lambda a, b: b if fscore[b] < fscore[a] else a, open_set)

        if current.is_solved():
            return current.path()

        open_set.remove(current)

        for neighbor in current.neighbors():
            tentative_gscore = gscore[current] + _d(current, neighbor)

            if tentative_gscore < gscore[neighbor]:
                gscore[neighbor] = tentative_gscore
                fscore[neighbor] = gscore[neighbor] + h(neighbor)

                if neighbor not in open_set:
                    open_set.add(neighbor)

    return None


# # # # # # # # # # # # #
# SMA*
#

def sma(puzzle: Puzzle, heuristic: int):
    raise NotImplementedError
