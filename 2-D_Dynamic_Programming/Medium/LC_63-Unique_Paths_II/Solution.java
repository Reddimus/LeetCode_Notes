class Solution {
    // Bottom-up approach
    // T: O(m*n), M: O(n), where m = rows, n = cols
    // public int uniquePathsWithObstacles(int[][] obstacleGrid) {
    //     int rows = obstacleGrid.length, cols = obstacleGrid[0].length;
    //     int[] dp = new int[cols];
    //     dp[cols-1] = 1; // goal base case

    //     for (int r = rows-1; r >= 0; --r) {
    //         for (int c = cols-1; c >= 0; --c) {
    //             if (obstacleGrid[r][c] == 1)    // obstacle
    //                 dp[c] = 0;                      // reset steps to 0
    //             else if (c < cols-1)
    //                 dp[c] += dp[c+1];
    //         }
    //     }

    //     return dp[0];
    // }

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
}

class TestCases {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int attempt;
        int[][] obstacleGrid;

        // Ex1:
        obstacleGrid = new int[][] {
            {0,0,0},
            {0,1,0},
            {0,0,0}
        };
        attempt = sol.uniquePathsWithObstacles(obstacleGrid);
        assert attempt == 2 : "Expected 2, but got " + attempt;
        // Ex2:
        obstacleGrid = new int[][] {
            {0,1},
            {0,0}
        };
        attempt = sol.uniquePathsWithObstacles(obstacleGrid);
        assert attempt == 1 : "Expected 1, but got " + attempt;
        // Test case 3:
        obstacleGrid = new int[][] {
            {0,0},
            {1,1},
            {0,0}
        };
        attempt = sol.uniquePathsWithObstacles(obstacleGrid);
        assert attempt == 0 : "Expected 0, but got " + attempt;
        // Test case 4:
        obstacleGrid = new int[][] {
            {0,0,0,0},
            {0,1,0,0},
            {0,0,0,0},
            {0,0,0,0}
        };
        attempt = sol.uniquePathsWithObstacles(obstacleGrid);
        assert attempt == 8 : "Expected 8, but got " + attempt;
        // Test case 5:
        obstacleGrid = new int[][] {
            {0,1}
        };
        attempt = sol.uniquePathsWithObstacles(obstacleGrid);
        assert attempt == 0 : "Expected 0, but got " + attempt;
    }
}