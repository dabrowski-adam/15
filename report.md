# Fifteen – Report

The puzzle consists of 15 pieces and one empty tile in a square 4x4 grid. Although there can be other variants, such as a 3x3 grid with 8 pieces.

The pieces are shuffled. To solve the puzzle they have to be arranged in a specific pattern.

In our case, pieces are marked by numbers, and the goal is to arrange them in an ascending order – starting with the top row and going down, ending at the blank tile in the bottom-right corner.

# Puzzle Complexity

In an NxN grid there are N! possible permutations, however only N! / 2 are valid puzzle states.

| Grid | Total Permutations  | Puzzle States  |
| :----: | :----: | :----:                    |
| 2x2    | 4!   | 8                           |
| 3x3    | 9!   | 1.81440 * 10<sup>5</sup>    |
| 4x4    | 16!  | 1.0461395 * 10<sup>13</sup> |
| 5x5    | 25!  | 7.755605 * 10<sup>24</sup>  |

Such large state space mandates usage of more clever approaches than simply brute-forcing the solution.

# Detecting Unsolvable States

Checking all permutations to determine if a puzzle is unsolvable is very inefficient.

Fortunately there exists a simple formula that lets us determine whether that is the case.

We have to take into account the number of inversions in the puzzle. An inversion occurs when a tile precedes another tile with a lower number on it.

Any NxN puzzle is solvable if:
- N is odd, and the number of inversions is even,
- N is even, the blank tile is on an even row (counting from the bottom), and the number of inversions is odd,
- N is even, the blank tile is on an odd row (counting from the bottom), and the number of inversions is even.

Otherwise there exist no solutions.

# Benchmarks

 Given the following 3x3 puzzle:
 
| **4**  | **1**  | **3**  |
| :----: | :----: | :----: |
|        | **2**  | **6**  |
| **7**  | **5**  | **8**  |

Different approaches yielded the following results (average of 5 runs):

| Algorithm | **Solution**  | **Solution Length**  | **Time Elapsed [ms]**  | **Memory Used [kB]**  |
| :----: | :----: | :----: | :----: | :----: |
| **BFS (Random)**  | DLUUL  | 5 | 1.426 | 110.592 |
| **BFS (LRUD)**  | DLUUL  | 5 | 1.335 | 110.592 |
| **BFS (DLUR)**  | DLUUL  | 5 | 0.875 | 69.632 |
| **DFS (Random)** | DLUURDDLUU... | 43411 | 4877.929  | 17399.808 |
| **DFS (DLUR)** | ULLDRRULLD... | 99443 | 3676.788  | 28573.696 |
| **DFS (RDLU)** | ULLDDRUULD... | 1059 | 24.263  | 1466.368 |
| **DFS (RULD)** | DLLUURDDLU... | 29 | 0.706  | 69.632 |
| **IDFS (Random)** | DLUUL | 5 | 8.969  | 40.960 |
| **A\* (Dijkstra)** | DLUUL | 5 | 1.411  | 131.072 |
| **A\* (Hamming)** | DLUUL | 5 | 1.354  | 77.824 |
| **A\* (Manhattan)** | DLUUL | 5 | 1.250  | 77.824 |


As can be seen in the results, the order in which neighbors are checked can greatly impact the time to find the result. 

And even though it seemed that choosing at random would yield stable, albeit not impressive results, it fared the worst. Perhaps speed of the randomization method is to blame.

We can also clearly see that depth-first search performed abysmally compared to breadth-first. Iterative deepening DFS is still behind, but much closer.

On this input A* performed comparably to BFS. It can be noted that when using heuristics the memory usage decreased in half.

 