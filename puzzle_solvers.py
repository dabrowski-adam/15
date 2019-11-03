from collections import deque

from puzzle_utils import is_solved, apply_move


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


class StateVertex:
    def __init__(self, puzzle, parent=None, move=None):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move

    def __iter__(self):
        return StateVertexIterator(self)

    def neighbors(self, order="LRUD"):
        return [StateVertex(apply_move(self.puzzle, move), parent=self, move=move) for move in order]

    def is_solved(self):
        return is_solved(self.puzzle)

    def path(self):
        moves = [parent.move for parent in self][:-1]
        moves.reverse()
        return "".join(moves)


def bfs(puzzle, order: str):
    root = StateVertex(puzzle)
    visited, stack = {root}, deque([root])

    while stack:
        vertex = stack.popleft()
        if vertex.is_solved():
            return vertex.path()

        for neighbor in vertex.neighbors():
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)


def dfs(puzzle, order: str):
    raise NotImplementedError


def idfs(puzzle, order: str):
    raise NotImplementedError


def bf(puzzle, heuristic: int):
    raise NotImplementedError


def astar(puzzle, heuristic: int):
    raise NotImplementedError


def sma(puzzle, heuristic: int):
    raise NotImplementedError
