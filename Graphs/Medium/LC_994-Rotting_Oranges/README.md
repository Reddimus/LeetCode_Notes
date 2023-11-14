# [LeetCode #994 - Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

**Difficulty: `Medium`**

---

You are given an `m x n` `grid` where each cell can have one of three values:

- `0` representing an empty cell;
- `1` representing a fresh orange;
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If this is impossible, return `-1`.

---

### Example 1:

![Rotting Oranges Example 1](oranges.png)

Input:
```
[[2,1,1],
 [1,1,0],
 [0,1,1]]
```
Output:
```
4
```

### Example 2:

Input:
```
[[2,1,1],
 [0,1,1],
 [1,0,1]]
```
Output:
```
-1
```
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

### Example 3:

Input:
```
[[0,2]]
```
Output:
```
0
```
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

---

### Constraints:

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

---

### Hints:
- Ask yourself if any of the following approaches work: `dynamic programming`, `BFS`, or `DFS`?
- It is possible for all the rotten oranges rotten fresh neighboring oranges simultaneously with each minute passing.

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Graphs/Medium/LC_1091-Shortest_Path_in_Binary_Matrix)

### Approach: Graphs - Breadth First Search (BFS)

#### Intuition

#### Complexity Analysis
- Time Complexity: `O(M*N)`  
- Space Complexity: `O(M*N)`  

Where `M` is the number of rows and `N` is the number of columns in the `grid`.

## Python Code
```python
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        rotten_cells = deque()  # queue indices of rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten_cells.append((r, c))
        
        minutes = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # While there are fresh oranges and rotten oranges queued
        while fresh > 0 and rotten_cells:
            # Rotten all neighboring oranges at the same time
            for same_minute in range(len(rotten_cells)):
                curr_row, curr_col = rotten_cells.popleft()
                for dir_row, dir_col in directions:
                    nghbr_row = dir_row + curr_row
                    nghbr_col = dir_col + curr_col
                    if ((-1 < nghbr_row < rows) and
                    (-1 < nghbr_col < cols) and
                    grid[nghbr_row][nghbr_col] == 1):
                        grid[nghbr_row][nghbr_col] = 2
                        rotten_cells.append((nghbr_row, nghbr_col))
                        fresh -= 1

            minutes += 1
        
        if fresh == 0:
            return minutes
        return -1
```

## C++ Code
```cpp
```

## Java Code
```java
```
