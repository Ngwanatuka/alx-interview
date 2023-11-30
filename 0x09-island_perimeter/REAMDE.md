# 0x09. Island Perimeter

**ALgorithm** **Python**

1. Initialize a variable perimeter to 0.
2. Iterate through each row and cell in the grid.

 * For each cell:
    * If the cell is land (has a value of 1):
        * Increment the perimeter by 4 (to account for all four sides of the cell).
        * Check the adjacent cells:  
            * If there is land to the left, decrement the perimeter by 1.
            * If there is land to the right, decrement the perimeter by 1.
            * If there is land above, decrement the perimeter by 1.
            * If there is land below, decrement the perimeter by 1.
3. Return the final perimeter value.

This algorithm ensures that the perimeter is incremented for each land cell and adjusted based on the presence of adjacent land cells. The use of nested loops and conditional statements allows for systematic traversal of the grid. The optimization involves using **enumerate** to obtain both the value and index during iteration, simplifying the conditions, and avoiding unnecessary index operations.