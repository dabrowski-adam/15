from random import shuffle

from puzzle_utils import apply_move, is_solved, Puzzle


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


def _random_order():
    moves = "LRUD".split()
    shuffle(moves)
    return "".join(moves)


class StateVertex:
    def __init__(self, puzzle: Puzzle, parent: 'StateVertex' = None, move: str = None):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self._hash = None

    def __hash__(self):
        if not self._hash:
            self._hash = hash(tuple(map(tuple, self.puzzle)))

        return self._hash

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __iter__(self):
        return StateVertexIterator(self)

    def neighbors(self, order="R"):
        is_random = len(order) != 4
        moves = order if not is_random else _random_order()
        return [StateVertex(apply_move(self.puzzle, move), parent=self, move=move) for move in moves]

    def is_solved(self):
        return is_solved(self.puzzle)

    def path(self):
        moves = [parent.move for parent in self][:-1]  # Remove last because root vertex has no move
        moves.reverse()
        return "".join(moves)
