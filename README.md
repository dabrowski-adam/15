# How to build

1. Use the virtual environment

   ```bash
   source venv/bin/activate
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. If you install new libraries update requirements.txt

   ```bash
   pip freeze > requirements.txt
   ```

4. Once you're done you can leave the virtual environment

   ```bash
   deactivate
   ```

# Solving problems by searching

## Fifteen puzzle

"Fifteen puzzle" can be described as a frame with embedded 15 pieces. They can be moved as there is one piece missing in the puzzle and the frame has size 4x4. The goal of the game is to move pieces inside frame in such a way to achieve ordered state, e.g. from initial state:

|        | **1**  | **2**  | **7**  |
| :----: | :----: | :----: | :----: |
| **8**  | **9**  | **12** | **10** |
| **13** | **3**  | **6**  | **4**  |
| **15** | **14** | **11** | **5**  |

transform puzzle to target one:

| **1**  | **2**  | **3**  | **4**  |
| :----: | :----: | :----: | :----: |
| **5**  | **6**  | **7**  | **8**  |
| **9**  | **10** | **11** | **12** |
| **13** | **14** | **15** |        |

## Problem and task

The task presented to groups is to write a program that will solve the puzzle, which mean it will find a sequence of actions that transforms initial state (given as input at program startup) to the final pattern thus solving the puzzle
Students are expected to implement various searching strategies and compare their characteristics. Comparison must be made basing on exhaustive empirical study. The results should be presented on technical report level (directions will be given during the classes). Following search strategies are compulsory:

- BFS
- DFS
- IDFS
- Best-first search
- A*
- SMA*

Informed search strategies must be tested using at least 2 heuristics. Additionally they should be teted with h(x)=0 heuristic.

## Functional requirements

It is expected from each group to present two programs. The first one, verifiable in linux/unix environment, reads initial state of a puzzle from standard input and on standard output presents the solution found - sequence of actions solving the puzzle. It is assumed, that letter 'L' denotes a move of a piece having freedom to the left, R to the right, U up, and D down. The program must be parametrised using following command line arguments.

### Command line arguments:

| -b   | --bfs   | *order*          | Breadth-first search      |
| ---- | ------- | ---------------- | ------------------------- |
|      |         |                  | Strategy                  |
| -d   | --dfs   | *order*          | Depth-first search        |
| -i   | --idfs  | *order*          | Iterative deepenening DFS |
| -h   | --bf    | *id_of_heurisic* | Best-first strategy       |
| -a   | --astar | *id_of_heurisic* | A* strategy               |
| -s   | --sma   | *id_of_heurisic* | SMA* strategy             |

Where *order* is a permutation of a set {'L','R','U','D'} defining an order in which successors of given state are processed, e.g. string DULR means the following search order: down, up, left, right. If *order* starts with 'R' it should be random (each node has random neighborhood search order).

### Input

In the first line of standard input two integer values *R* *C* are given: row count and column count respectively, defining frame size. In each subsequent *R* lines of standard input contains *C* space separated integer values describing a piece in the puzzle. Value 0 denotes empty space in the given frame.

### Output

Standard output of a given program should consist of at least two lines. The first line should contain one value *n*: the length of the solution found by the program or -1 if puzzle has not been solved. Second line of standard output should be a string of length *n* containing uppercase latin characters from set {'L','R', 'U', 'D'} describing the solution. If the solution does not exist the second line should be empty.

## Viewer

Students are also required to present a second application that allows to view previously found solution step by step (with jumps).

*Last modified: Thursday, 19 September 2019, 9:57 AM*