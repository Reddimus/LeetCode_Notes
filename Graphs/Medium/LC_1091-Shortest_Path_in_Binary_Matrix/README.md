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
- Ask yourself if any of the following approaches work: `dynamic programming`, `BFS`, or `DFS`?
- How can you store the length of each path?

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Graphs/Medium/LC_1091-Shortest_Path_in_Binary_Matrix)

### Approach: Graphs - Breadth First Search (BFS)

#### Intuition
The problem can be modeled as a graph problem. Each cell in the grid is a node in the graph. Each node has 8 neighbors (up, down, left, right, and 4 diagonals). The goal is to find the shortest path from the top-left node to the bottom-right node. We can efficiently solve this problem using Breadth First Search (BFS) as we traverse paths level by level until the fastest path reaches the goal node first. 

The reason Depth First Search (DFS) does not work is because the algorithm traverses all the way through a path before backtracking. This means that the algorithm will have to traverse through all the paths before finding the shortest path in the worst case. 

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
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();    // n * n grid, n == rows == cols
        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) 
            return -1;

        queue<indices> qCell;   // queue cells; first cell is queued (r, c)
        qCell.push({0, 0});
        queue<int> qLength;     // accompany queued cells with length
        qLength.push(1);
        grid[0][0] = 1;         // visited cell
        vector<indices> directions = {{1, 0}, {-1, 0},  // down, up
                                    {0, 1}, {0, -1},    // right, left
                                    {1, 1}, {-1, -1},   // bottom right, top left
                                    {1, -1}, {-1, 1}};  // bottom left, top right

        // While there is a valid path queued or goal not reached
        while (!qCell.empty()) {
            indices currCell = qCell.front();
            qCell.pop();
            int length = qLength.front();
            qLength.pop();
            if (currCell.row == n-1 && currCell.col == n-1)
                return length;
            
            // Explore if neighboring nodes are a valid path
            for (indices& dir : directions) {
                int nghbrRow = dir.row + currCell.row;
                int nghbrCol = dir.col + currCell.col;
                // if neighboring cell is not blocked & has not been visited
                if ((-1 < nghbrRow && nghbrRow < n) &&
                (-1 < nghbrCol && nghbrCol < n) &&
                grid[nghbrRow][nghbrCol] == 0) {
                    grid[nghbrRow][nghbrCol] = 1;   // visited cell
                    qCell.push({nghbrRow, nghbrCol});
                    qLength.push(length+1);
                }
            }
        }

        return -1;
    }
private:
    struct indices {const int row, col;};
};
```

## Java Code
```java
class Solution {
    private static class Indices {
        final int row, col;
        Indices(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
    int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;    // n * n grid, n == rows == cols
        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) 
            return -1;

        Queue<Indices> qCell = new LinkedList<>();  // queue cell indices
        qCell.add(new Indices(0, 0));
        Queue<Integer> qLen = new LinkedList<>();   // accompany queued cells with length
        qLen.add(1);
        grid[0][0] = 1;                             // visited cell
        Indices[] directions = {new Indices(1, 0),      // down
                                new Indices(-1, 0),     // up
                                new Indices(0, 1),      // right
                                new Indices(0, -1),     // left
                                new Indices(1, 1),      // down-right
                                new Indices(-1, -1),    // up-left
                                new Indices(1, -1),     // down-left
                                new Indices(-1, 1)};    // up-right

        // While there is a valid path queued or goal not reached
        while (!qCell.isEmpty()) {
            Indices currCell = qCell.poll();
            int length = qLen.poll();
            if (currCell.row == n-1 && currCell.col == n-1) 
                return length;

            // Explore if neighboring nodes are a valid path
            for (Indices dir : directions) {
                int nghbrRow = dir.row + currCell.row;
                int nghbrCol = dir.col + currCell.col;
                // if neighboring cell is not blocked & has not been visited
                if ((-1 < nghbrRow && nghbrRow < n) &&
                (-1 < nghbrCol && nghbrCol < n) &&
                grid[nghbrRow][nghbrCol] == 0) {
                    grid[nghbrRow][nghbrCol] = 1;   // visited cell
                    qCell.add(new Indices(nghbrRow, nghbrCol));
                    qLen.add(length+1);
                }
            }
        }

        return -1;
    }
}
```
