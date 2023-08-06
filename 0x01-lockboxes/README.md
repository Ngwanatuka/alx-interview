Discription 

This Python script provides a method 'canUnlockAll(boxes)' that determines if all the boxes can be opened, given a list of boxes containing keys to other boxes.

Problem Statement

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes. A key with the same number as a box opens that box. The first box[0] is already unlocked. The task is to determine if it's possible to unlock all the boxes.

Input

- 'boxes': A list of lists where each sublist represents a box contains keys (positive integers) to other boxes.

Output

- 'True' if all boxes can be opened or 'False' if not.

Implementation

- The method 'canUnlockAll(boxes)' checks whether all locked boxes can be opened by simulating the process of finding and using keys. It follows the following steps:

1. Create a list 'reachable' to track which boxes can be reached. Initialize all elements as 'False'
2. Start 'reachable[0]' as 'True' since the first box is unlocked
3. Start iteratign through the list of boxes. For each box 'i', if 'reachable[i]' is 'True', iterate through the keys in box 'i' and update the 'reachable' list for the corresponding box numbers.
4. Repeat step 3 until no more changes occurs in the 'reachable' list. This ensures that reachable boxes are updated based on the keys found.
5. Finally, check if all boxes are reachable by verifying if all elements in the 'reachable' list are 'True'.

Usage

1. Clone the repository or copy the of the '0-lockboxes.py' script.
2. Import the 'canUnlockAll' function in your Python code:
    
    ```from 0-lockboxes import canUnlockAll```

    1. Use the 'canUnlockAll' function to determine if all boxes can be opened:
        
        ```canUnlockAll(boxes)```
    
        # Example boxes
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False

Contributing

Contributions are welcome! if you find any bugs or have any comments/questions, feel free to open an issue or contact me directly at [ngwanatuka@gmail.com]