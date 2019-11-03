from collections import deque
from random import shuffle
from collections import defaultdict
from math import inf
from functools import reduce
from itertools import chain

from puzzle_utils import is_solved, apply_move
from utils import first_true


class StateVertexIterator:
    def __init__(self, vertex):
        self.vertex = vertex

    def __iter__(self):
        return self

    def __next__(self):
        vertex = self.vertex

        if vertex:
            self.vertex = vertex.parent
            return vertex

        raise StopIteration


def random_order():
    moves = "LRUD".split()
    shuffle(moves)
    return "".join(moves)


class StateVertex:
    def __init__(self, puzzle, parent=None, move=None):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move

    def __iter__(self):
        return StateVertexIterator(self)

    def neighbors(self, order="R"):
        is_random = len(order) != 4
        moves = order if not is_random else random_order()
        return [StateVertex(apply_move(self.puzzle, move), parent=self, move=move) for move in moves]

    def is_solved(self):
        return is_solved(self.puzzle)

    def path(self):
        moves = [parent.move for parent in self][:-1]  # Remove last because root vertex has no move
        moves.reverse()
        return "".join(moves)


def bfs(puzzle, order: str):
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


def dfs(puzzle, order: str):
    raise NotImplementedError


def dls(vertex, depth, order="R"):
    if depth == 0:
        return (vertex, True) if vertex.is_solved() else (None, True)

    results = [dls(neighbor, depth - 1) for neighbor in vertex.neighbors(order)]
    found, remaining = zip(*results)
    return first_true(found, default=None), first_true(remaining)


def idfs(puzzle, order: str, max_depth=30):
    root = StateVertex(puzzle)

    for depth in range(max_depth + 1):
        found, remaining = dls(root, depth, order=order)
        if found:
            return found.path()
        elif not remaining:
            return None


def bf(puzzle, heuristic: int):
    raise NotImplementedError


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


# sum of Manhattan distances between pieces and goal
def _manhattan(vertex: StateVertex):
    return 0


DIJKSTRA, HAMMING, MANHATTAN = 0, 1, 2

heuristics = {
    DIJKSTRA: _dijkstra,
    HAMMING: _hamming,
    MANHATTAN: _manhattan
}


def astar(puzzle, heuristic: int):
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


def sma(puzzle, heuristic: int):
    raise NotImplementedError
