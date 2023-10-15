
# LeetCode #63 - Unique Paths II

https://leetcode.com/problems/unique-paths-ii/

**Difficulty: `Medium`**

You are given an `m x n` integer array `grid`. There is a robot initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to `2 * 10^9`.

## Example 1
|       |   0   |     1    |   2  |
|:-----:|:-----:|:--------:|:----:|
| **0** | Robot |          |      |
| **1** |       | Obstacle |      |
| **2** |       |          | Goal |

**Input**: 
```
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
```
**Output**: 
```
2
```
**Explanation**: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

## Example 2
|       |   0   |     1    |
|:-----:|:-----:|:--------:|
| **0** | Robot | Obstacle |
| **1** |       |   Goal   |

**Input**: 
```
obstacleGrid = [[0,1],[0,0]]
```
**Output**: 
```
1
```

## Constraints
- `m == obstacleGrid.length`
- `n == obstacleGrid[i].length`
- `1 <= m, n <= 100`
- `obstacleGrid[i][j]` is `0` or `1`.

### Hints
- The robot can only move either down or right. Hence the current cell is reachable only from left cell (if exists) or upper cell (if exists) **or** the current cell impacts the right cell (if exists) or bottom cell (if exists).
- If the current cell is obstacle then the number of ways of reaching current cell is 0.

# Solution Explanation

https://github.com/Reddimus/LeetCode_Notes/tree/main/2-D_Dynamic_Programming/Medium/LC_63-Unique_Paths_II

## Approach: 2-D Dynamic Programming - Bottom Up

### Intuition
The problem closely resembles the classic "Unique Paths" problem with the added complexity of obstacles. In this modified scenario, a 2-D Dynamic Programming approach serves well. Starting from the bottom-right corner (goal), we populate each cell with the number of unique paths leading to the start. This is calculated as the sum of paths from the adjacent right and bottom cells, provided they are not blocked by obstacles. Cells containing obstacles are explicitly set to zero, as they are impassable. By progressively filling in this information from bottom to top and right to left, the top-left cell will eventually contain the total number of unique, obstacle-free paths to the goal.

### Steps:
1. Initialize dp array with a base case of 1 at the goal cell (bottom right)
2. In reverse order, iterate through each cell in the grid
    1. If the current cell is an obstacle, then set the number of unique paths to that cell to 0.
    2. Else, if the current cell is not an obstacle, then add the previous calculated number (Bootom-Up) of unique paths to current cell.
3. Return the number of unique paths to the start cell.

Note: We can optimize the space complexity of the DP array table to `O(n)` by only keeping track of the previous row (Bootom-Up) of the DP table.

### Time & Space complexity:
**Time:** `O(m*n)`  
**Space:** `O(n)` or `O(m*n)` w/ full dp grid

Where `n` is the number of rows and `m` is the number of columns in the grid.

### Python Code:
```python
class Solution:
    # Bottom-Up Approach
    # T: O(m*n), M: O(n), where m = rows, n = cols
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols
        dp[-1] = 1  # goal base case

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if obstacleGrid[r][c]:  # if obstacle
                    dp[c] = 0               # reset steps to 0
                elif c + 1 < cols:
                    dp[c] += dp[c+1]
        return dp[0]
    
    '''
    # Bottom-Up approach with full dp grid
    # T: O(m*n), M: O(m*n), where m = rows, n = cols
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (cols+1) for row in range(rows+1)]
        dp[rows-1][cols-1] = 1  # goal base case

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if obstacleGrid[r][c]:  # if obstacle
                    dp[r][c] = 0            # reset steps to 0
                else:
                    dp[r][c] += dp[r+1][c] + dp[r][c+1]
        
        return dp[0][0]
    '''
```

### C++ Code:
```cpp
class Solution {
public:
    // Bottom-up approach
    // T: O(m*n), M: O(n), where m = rows, n = cols
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int rows = obstacleGrid.size(), cols = obstacleGrid[0].size();
        vector<long long> dp(cols, 0);
        dp[cols-1] = 1; // goal base case

        for (int row = rows-1; row >= 0; row--) {
            for (int col = cols-1; col >= 0; col--) {
                if (obstacleGrid[row][col] == 1)    // obstacle
                    dp[col] = 0;                        // reset steps to 0
                else if (col < cols-1)
                    dp[col] += dp[col+1];
            }
        }

        return dp[0];
    }

    /*
    // Bottom-Up approach with full dp grid
    // T: O(m*n), M: O(m*n), where m = rows, n = cols
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {

        int rows = obstacleGrid.size(), cols = obstacleGrid[0].size();
        vector<vector<long long>> dp(rows+1, vector<long long>(cols+1, 0));
        dp[rows-1][cols-1] = 1; // goal base case

        for (int r = rows-1; r >= 0; r--) {
            for (int c = cols-1; c >= 0; c--) {
                if (obstacleGrid[r][c] == 1)    // obstacle
                    dp[r][c] = 0;                   // reset steps to 0
                else
                    dp[r][c] += dp[r+1][c] + dp[r][c+1];
            }
        }

        return dp[0][0];
    }
    */
};
```

### Java Code:
```java
class Solution {
    // Bottom-up approach
    // T: O(m*n), M: O(n), where m = rows, n = cols
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int rows = obstacleGrid.length, cols = obstacleGrid[0].length;
        int[] dp = new int[cols];
        dp[cols-1] = 1; // goal base case

        for (int r = rows-1; r >= 0; --r) {
            for (int c = cols-1; c >= 0; --c) {
                if (obstacleGrid[r][c] == 1)    // obstacle
                    dp[c] = 0;                      // reset steps to 0
                else if (c < cols-1)
                    dp[c] += dp[c+1];
            }
        }

        return dp[0];
    }

    /*
    // Bottom-Up approach with full dp grid
    // T: O(m*n), M: O(m*n), where m = rows, n = cols
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int rows = obstacleGrid.length, cols = obstacleGrid[0].length;
        int[][] dp = new int[rows+1][cols+1];
        dp[rows-1][cols-1] = 1; // goal base case

        for (int r = rows-1; r >= 0; --r) {
            for (int c = cols-1; c >= 0; --c) {
                if (obstacleGrid[r][c] == 1)    // obstacle
                    dp[r][c] = 0;                      // reset steps to 0
                else
                    dp[r][c] += dp[r+1][c] + dp[r][c+1];
            }
        }

        return dp[0][0];
    }
    */
}
```

## Approach: 2-D Dynamic Programming - Top Down

### Intuition
The problem closely resembles the classic "Unique Paths" problem with the added complexity of obstacles. In this modified scenario, a 2-D Dynamic Programming approach serves well. Starting from the top-left corner (start), we populate each cell with the number of unique paths leading to the goal. This is calculated as the sum of paths from the adjacent left and top cells, provided they are not blocked by obstacles. Cells containing obstacles are explicitly set to zero, as they are impassable. By progressively filling in this information from top to bottom and left to right, the bottom-right cell will eventually contain the total number of unique, obstacle-free paths to the goal.

### Steps:
1. Initialize dp array with a base case of 1 at the start cell (top left)
2. Iterate through each cell in the grid
    1. If the current cell is an obstacle, then set the number of unique paths to that cell to 0.
    2. Else, if the current cell is not an obstacle, then add the previous calculated number (Top-Down) of unique paths to current cell.
3. Return the number of unique paths to the goal cell.

### Time & Space complexity:
**Time:** `O(m*n)`  
**Space:** `O(n)` or `O(m*n)` w/ full dp grid

Where `n` is the number of rows and `m` is the number of columns in the grid.

### Python Code:
```python
class Solution:
    # Top-Down Approach
    # T: O(m*n), M: O(n), where m = rows, n = cols
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols
        dp[0] = 1   # start base case

        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c]:  # if obstacle
                    dp[c] = 0               # reset steps to 0
                elif c - 1 >= 0:
                    dp[c] += dp[c-1]

        return dp[-1]

    '''
    # Top-Down Approach with full dp grid
    # T: O(m*n), M: O(m*n), where m = rows, n = cols
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (cols+1) for row in range(rows+1)]
        dp[1][1] = 1    # start base case

        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if obstacleGrid[r-1][c-1]:  # if obstacle
                    dp[r][c] = 0                # reset steps to 0
                else:
                    dp[r][c] += dp[r-1][c] + dp[r][c-1]

        return dp[-1][-1]
    '''
```

### C++ Code:
```cpp
class Solution {
public:
    // Top-Down Approach
    // T: O(m*n), M: O(n), where m = rows, n = cols
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int rows = obstacleGrid.size(), cols = obstacleGrid[0].size();
        vector<long long> dp(cols, 0);
        dp[0] = 1; // start base case

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++)
                if (obstacleGrid[r][c] == 1)    // obstacle
                    dp[c] = 0;                      // reset steps to 0
                else if (c > 0)
                    dp[c] += dp[c-1];
        }

        return dp[cols-1];
    }

    /*
    // Top-Down Approach with full dp grid
    // T: O(m*n), M: O(m*n), where m = rows, n = cols
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int rows = obstacleGrid.size(), cols = obstacleGrid[0].size();
        vector<vector<long long>> dp(rows+1, vector<long long>(cols+1, 0));
        dp[1][1] = 1;   // start base case

        for (int r = 1; r <= rows; r++) {
            for (int c = 1; c <= cols; c++)
                if (obstacleGrid[r-1][c-1] == 1)    // obstacle
                    dp[r][c] = 0;                       // reset steps to 0
                else
                    dp[r][c] += dp[r-1][c] + dp[r][c-1];
        }

        return dp[rows][cols];
    }
    */
};
```

### Java Code:
```java
class Solution {
    // Top-Down Approach
    // T: O(m*n), M: O(n), where m = rows, n = cols
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int rows = obstacleGrid.length, cols = obstacleGrid[0].length;
        int[] dp = new int[cols];
        dp[0] = 1; // start base case

        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c)
                if (obstacleGrid[r][c] == 1)    // obstacle
                    dp[c] = 0;                      // reset steps to 0
                else if (c > 0)
                    dp[c] += dp[c-1];
        }

        return dp[cols-1];
    }

    /*
    // Top-Down Approach with full dp grid
    // T: O(m*n), M: O(m*n), where m = rows, n = cols
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int rows = obstacleGrid.length, cols = obstacleGrid[0].length;
        int[][] dp = new int[rows+1][cols+1];
        dp[1][1] = 1; // start base case

        for (int r = 1; r <= rows; ++r) {
            for (int c = 1; c <= cols; ++c)
                if (obstacleGrid[r-1][c-1] == 1)    // obstacle
                    dp[r][c] = 0;                      // reset steps to 0
                else
                    dp[r][c] += dp[r-1][c] + dp[r][c-1];
        }

        return dp[rows][cols];
    }
    */
}
```
