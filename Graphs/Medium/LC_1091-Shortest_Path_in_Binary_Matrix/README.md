# [LeetCode #1091 - Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

**Difficulty: `Medium`**

---

Given an `n x n` binary matrix `grid`, return the length of the shortest **clear path** in the matrix. If there is no clear path, return `-1`.

A **clear path** in a binary matrix is a path from the top-left cell (i.e., `(0, 0)`) to the bottom-right cell (i.e., `(n - 1, n - 1)`) such that:

- All the visited cells of the path are `0`.
- All the adjacent cells of the path are **8-directionally** connected (i.e., they are different and they share an edge or a corner).

The **length of a clear path** is the number of visited cells of this path.

---

### Example 1:

![Shortest Path in Binary Matrix Example 1](shortestpath1-grid.png)

Input:
```
grid = [[0,1],[1,0]]
```

Output:
```
2
```


### Example 2:

![Shortest Path in Binary Matrix Example 2](shortestpath2-grid.png)

Input:
```
grid = [[0,0,0],[1,1,0],[1,1,0]]
```

Output:
```
4
```


### Example 3:

Input:
```
grid = [[1,0,0],[1,1,0],[1,1,0]]
```

Output:
```
-1
```


---

### Constraints:

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j]` is `0` or `1`.

---
### Hints:

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Graphs/Medium/LC_1091-Shortest_Path_in_Binary_Matrix)

### Approach: Graphs - Breadth First Search (BFS)

#### Intuition

#### Complexity Analysis
- Time Complexity: `O(N^2)`  
- Space Complexity: `O(N^2)`  

Where `N` is the number of `rows` and `columns` in the `grid`.

## Python Code
```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)   # n * n grid, n == rows == cols
        q = deque()     # queue cells w/ length
        # If starting cell & goal cell are not blocked
        if grid[0][0] == 0 and grid[n-1][n-1] == 0:
            grid[0][0] = 1       # visited cell
            q.append((0, 0, 1))  # First cell (row, col), length = 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                        (1, 1), (-1, -1), (1, -1), (-1, 1)]

        # While there is a valid path queued or goal not reached
        while q:
            curr_row, curr_col, curr_len = q.popleft()
            if curr_row == n-1 and curr_col == n-1:
                return curr_len
            
            # Explore if neighboring nodes are a valid path
            for dir_row, dir_col in directions:
                nghbr_row = curr_row + dir_row
                nghbr_col = curr_col + dir_col
                # if neighboring cell is not blocked & has not been visited
                if ((-1 < nghbr_row < n) and 
                (-1 < nghbr_col < n) and 
                grid[nghbr_row][nghbr_col] == 0):
                    grid[nghbr_row][nghbr_col] = 1  # visited cell
                    q.append((nghbr_row, nghbr_col, curr_len + 1))
            
        return -1
```

## C++ Code
```cpp
```

## Java Code
```java
```
