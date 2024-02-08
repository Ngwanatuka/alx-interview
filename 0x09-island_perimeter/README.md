# Island Perimeter

## Overview

The Island Perimeter problem involves calculating the perimeter of an island represented by a grid. Each cell in the grid is either land or water, and the goal is to determine the total perimeter of the island. The grid is completely surrounded by water, and there is only one island with no "lakes" (water inside that isn’t connected to the water surrounding the island).

## Problem Statement

Given a grid where 0 represents water and 1 represents land, the task is to calculate the perimeter of the island described in the grid. The island is a contiguous group of land cells connected horizontally or vertically. The perimeter is the total length of the boundary between the land and water cells.

### Constraints

* The grid is a rectangular 2D list of integers.
* Each cell in the grid is either 0 (water) or 1 (land).
* Cells are connected horizontally or vertically but not diagonally.
* The grid is completely surrounded by water.
* There is only one island (or none).
* The island doesn’t have any "lakes" (water inside that isn’t connected to the water surrounding the island).

## Function Signature

```python
def island_perimeter(grid: List[List[int]]) -> int:
    """
    Function to calculate the perimeter of the island described in the grid.

    Parameters:
    - grid: A list of lists of integers representing the 2D grid where 0 represents water and 1 represents land.

    Returns:
    - int: The perimeter of the island.
    """
```
### Approach

To solve the Island Perimeter problem, we can use a depth-first search (DFS) algorithm to traverse the grid and count the perimeter of the island. The key idea is to start the DFS from any land cell and recursively explore all neighboring land cells, marking them as visited to avoid revisiting. During the DFS traversal, we count the number of boundaries between land and water, which gives us the perimeter of the island.

### Algorithm

1. Start by defining a recursive DFS function that takes the grid, row index, and column index as parameters.
2. In the DFS function, check if the current cell is out of bounds or is water. If so, return 1 (indicating a boundary).
3. If the current cell is already visited, return 0 to avoid double counting.
4. Mark the current cell as visited (e.g., by changing its value to -1).
5. Recursively explore all neighboring land cells (up, down, left, right) and accumulate the perimeter.
6. After the DFS traversal, return the total perimeter counted.
7. Iterate through the grid to find the first land cell and start the DFS from there.
8. Finally, return the result obtained from the DFS traversal.

### Complexity Analysis

* Time Complexity: O(N*M), where N is the number of rows and M is the number of columns in the grid. This is because we need to visit each cell in the grid at least once to calculate the perimeter.
* Space Complexity: O(N*M) in the worst case, due to the recursive stack space used during DFS traversal. However, this can be reduced to O(1) by using an iterative DFS approach.
  

### Example

```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid)) # Output: 16
```

### Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or create a pull request.