
# [LeetCode #695 - Max Area of Island](https://leetcode.com/problems/max-area-of-island/)

**Difficulty: `Medium`**

---

You are given an `m x n` binary matrix `grid`. An island is a group of `1's` (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value `1` in the island.

Return the maximum area of an island in `grid`. If there is no island, return `0`.

---

### Example 1:

![Max Area of Island Example 1](maxarea1-grid.jpg)

Input:
```
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
```
Output:
```
6
```
Explanation: The answer is `not 11`, because the island must be connected 4-directionally.

### Example 2:

Input:
```
grid = [[0,0,0,0,0,0,0,0]]
```
Output:
```
0
```

---

### Constraints:

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` is either `0` or `1`.

### Hints:
1. First imagine you need to solve the problem of the number of Islands. How do you know when two parts of land are connected? See `LeetCode #200 - Number of Islands` for reference.
    - Can you use a similar approach to find the area of the island?
2. Solve using either a Depth First Search (DFS) or Breadth First Search (BFS).
    - Can you solve it both ways?

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Graphs/Medium/LC_695-Max_Area_of_Island)

### Approach: Graphs - Depth First Search (DFS) & Breadth First Search (BFS)

#### Intuition
The "Max Area of Island" problem can be approached similarly to the "Number of Islands" problem. In both cases, we are tasked with exploring a grid comprised of land (`1's`) and water (`0's`). However, while the "Number of Islands" problem requires us to count the number of distinct islands, "Max Area of Island" asks us to find the largest area of contiguous land.

We can utilize either Depth First Search (DFS) or Breadth First Search (BFS) to traverse the grid. These algorithms allow us to visit each piece of land and keep track of the size of the area we're exploring. The fundamental idea is to iterate over each cell in the grid, and upon finding a piece of land (`1`), we initiate a traversal that marks visited parts of the island by setting them to `0` (or any other marker to indicate visited land) to prevent revisiting. During this traversal, we increment a counter for each piece of land encountered, thereby calculating the area of the current island.

The maximum area is updated whenever we find an island with a larger area than the previously recorded maximum. The traversal continues until all lands have been visited, ensuring that each island's area is considered.

#### Complexity Analysis
- Time Complexity: `O(M*N)`
- Space Complexity: `O(M*N)`

Where `M` is the number of rows and `N` is the number of columns in the grid. In the worst-case scenario, the grid is filled with land, and we need to store the entire grid in the call stack (for DFS) or the queue (for BFS).

## Python Code
```python
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                # if land and coordinates not visited
                if (grid[r][c] == 1):
                    max_area = max(max_area, self.dfs(r, c, rows, cols, grid))
                    # max_area = max(max_area, self.bfs(r, c, rows, cols, grid))
        return max_area
    
    def dfs(self, r: int, c: int, rows: int, cols: int, grid: list[list[int]]) -> int:
        # If the current cell is out of bounds or not land/not visited
        if (
            r < 0 or rows <= r or
            c < 0 or cols <= c or
            grid[r][c] != 1
        ):
            return 0    # stop adding

        grid[r][c] = 0  # cell visited

        # Recursively add the area of the neighboring land cells
        return (1 + 
        self.dfs(r+1, c, rows, cols, grid) +    # down
        self.dfs(r-1, c, rows, cols, grid) +    # up
        self.dfs(r, c+1, rows, cols, grid) +    # right
        self.dfs(r, c-1, rows, cols, grid))     # left
    
    '''
    def bfs(self, r: int, c: int, rows: int, cols: int, grid: list[list[int]]) -> int:
        grid[r][c] = 0  # visited cell
        q = collections.deque() # visit coordinates in FCFS/FIFO order
        q.append((r, c))

        area = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # while there are connected land coordinates to visit
        while q:
            curr_r, curr_c = q.popleft()
            for dir_r, dir_c in directions:
                neighb_r, neighb_c = curr_r + dir_r, curr_c + dir_c
                # if neigboring coordinates are land & not visited
                if (
                (-1 < neighb_r < rows) and
                (-1 < neighb_c < cols) and
                grid[neighb_r][neighb_c] == 1
                ):
                    grid[neighb_r][neighb_c] = 0    # visited cell
                    q.append((neighb_r, neighb_c))
                    area += 1
        
        return area # return island's area
    '''
```

## C++ Code
```cpp
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int rows = grid.size(), cols = grid[0].size();

        int maxArea = 0;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                // if land and coordinates not visited
                if (grid[r][c] == 1)
                    maxArea = max(maxArea, dfs(r, c, rows, cols, grid));
                    // maxArea = max(maxArea, bfs(r, c, rows, cols, grid));
            }
        }

        return maxArea;
    }
private:
    int dfs(int r, int c, int rows, int cols, vector<vector<int>>& grid) {
        // If the current cell is out of bounds or not land/not visited
        if (r < 0 || rows <= r ||
        c < 0 || cols <= c ||
        grid[r][c] != 1)
            return 0;   // stop adding

        grid[r][c] = 0; // cell visited

        // Recursively add the area of the neighboring land cells
        return 1 + 
        dfs(r+1, c, rows, cols, grid) +     // down
        dfs(r-1, c, rows, cols, grid) +     // up
        dfs(r, c+1, rows, cols, grid) +     // right
        dfs(r, c-1, rows, cols, grid);      // left
    }

    /*
    struct indices {const int row, col;};
    int bfs(int r, int c, int rows, int cols, vector<vector<int>>& grid) {
        grid[r][c] = 0; // visited cell
        queue<indices> q;  // visit coordinates in FCFS/FIFO order
        q.push({r, c});

        int area = 1;
        vector<indices> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        // while there are connected land coordinates to visit
        while (!q.empty()) {
            indices currCell = q.front();
            q.pop();

            for (indices &dir : directions) {
                int neighbR = currCell.row + dir.row;
                int neighbC = currCell.col + dir.col;
                // if neigboring coordinates are land & not visited
                if ((-1 < neighbR && neighbR < rows) &&
                (-1 < neighbC && neighbC < cols) &&
                grid[neighbR][neighbC] == 1) {
                    grid[neighbR][neighbC] = 0; // visited cell
                    q.push({neighbR, neighbC});
                    ++area;
                }
            }
        }
        
        return area;    // return island's area
    }
    */
};
```

## Java Code
```java
```
