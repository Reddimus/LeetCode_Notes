# [LeetCode #200 - Number of Islands](https://leetcode.com/problems/number-of-islands/)

**Difficulty: `Medium`**

---

Given an `m x n` 2D binary grid which represents a map of `'1's` (land) and `'0's` (water), return the *number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

---

### Examples:

**Example 1**:  
Input: 
```
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
```
Output: 
```
1
```

**Example 2**:  
Input:  
```
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
```
Output: 
```
3
```

---

### Constraints:

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

---

### Hints:
- 

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Graphs/Medium/LC_200-Number_of_Islands)

### Approach: Graphs - Depth-First Search (DFS) & Breadth-First Search (BFS)

#### Intuition

#### Complexity Analysis
- Time Complexity: `O(m*n)`
- Space Complexity: `O(m*n)`

Where `m` is the amount of rows and `n` is the amount of columns. The worst case is that the entire grid is filled with land, so we would have to visit and store every coordinate in the grid.

## Python Code
```python
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        self.visited = set()

        count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                # If the current cell is land & not visited
                if grid[r][c] == "1" and (r, c) not in self.visited:
                    self.dfs(r, c)
                    # self.bfs(r, c)
                    count += 1
        return count

    def dfs(self, r: int, c: int) -> None:
        if (
            r < 0 or self.rows <= r or
            c < 0 or self.cols <= c or
            self.grid[r][c] == "0" or
            (r, c) in self.visited 
        ):
            return  # water reached or cell already visited
        
        self.visited.add((r, c))

        # Recursively check neighboring cells
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dir_r, dir_c in directions:
            self.dfs(r + dir_r, c + dir_c)  # go deeper into path
'''
    def bfs(self, r: int, c: int) -> None:
        self.visited.add((r, c))
        q = collections.deque() # visit cells in FCFS/FIFO order
        q.append((r, c))

        # while there are connected land cells to visit
        while q:
            curr_r, curr_c = q.popleft()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dir_r, dir_c in directions:
                neighb_r, neighb_c = curr_r + dir_r, curr_c + dir_c
                # if neigboring coordinates are land & not visited
                if (
                    -1 < neighb_r < self.rows and
                    -1 < neighb_c < self.cols and
                    self.grid[neighb_r][neighb_c] == "1" and
                    (neighb_r, neighb_c) not in self.visited
                ):
                    q.append((neighb_r, neighb_c))
                    self.visited.add((neighb_r, neighb_c))
'''
```

## C++ Code
```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size(), cols = grid[0].size();

        int count = 0;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                // If the current cell is land & not visited
                if (grid[r][c] == '1') {
                    dfs(r, c, rows, cols, grid);
                    // bfs(r, c, rows, cols, grid);
                    ++count;
                }
            }
        }
        return count;
    }

private:
    void dfs(int r, int c, int rows, int cols, vector<vector<char>>& grid) {
        if (r < 0 || rows <= r ||
        c < 0 || cols <= c ||
        grid[r][c] != '1')
            return; // water reached or cell already visited

        grid[r][c] = 'V';   // cell visited

        // Recursively check neighboring cells
        dfs(r+1, c, rows, cols, grid);
        dfs(r-1, c, rows, cols, grid);
        dfs(r, c+1, rows, cols, grid);
        dfs(r, c-1, rows, cols, grid);
    }
    

    /*
    struct indicies {const int row, col;};

    void bfs(int r, int c, int rows, int cols, vector<vector<char>>& grid) {
        queue<indicies> q;
        grid[r][c] = 'V';
        q.push({r, c});

        // while there are connected land cells to visit
        while (!q.empty()) {
            indicies currCell = q.front();
            q.pop();	// visit cells in FCFS/FIFO order
            vector<indicies> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            for (indicies &dir : directions) {
                int neighbR = currCell.row + dir.row;
                int neighbC = currCell.col + dir.col;
                // if neigboring cells are land & not visited
                if ((-1 < neighbR && neighbR < rows) &&
                (-1 < neighbC && neighbC < cols) &&
                grid[neighbR][neighbC] == '1') {
                    q.push({neighbR, neighbC});
                    grid[neighbR][neighbC] = 'V';
                }
            }
        }
    }
    */
};
```

## Java Code
```java
```
