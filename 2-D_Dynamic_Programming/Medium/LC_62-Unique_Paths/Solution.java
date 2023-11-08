class Solution {
    // 2-D Dynamic Programming - Full Grid/Bottom-Up Approach
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        
        // Solve base case; last row and last column
        for (int col = 0; col < n; ++col)
            dp[m-1][col] = 1;
        for (int row = 0; row < m; ++row)
            dp[row][n-1] = 1;

        // Solve remaining cases using bottom up approach
        for (int row = m - 2; 0 <= row; --row) {
            for (int col = n - 2; 0 <= col; --col) {
                dp[row][col] = dp[row][col+1] + dp[row+1][col];
            }
        }

        return dp[0][0];
    }
}

class TestCases {
    public static void main(String[] args) {
        // In terminal:
        // Compile:     "javac Solution.java"
        // Test cases:  "java -ea TestCases"
        Solution sol = new Solution();
        int attempt;

        // Ex 1
        attempt = sol.uniquePaths(3, 7);
        assert attempt == 28 : "Expected 28, but got " + attempt;
        // Ex 2
        attempt = sol.uniquePaths(3, 2);
        assert attempt == 3 : "Expected 3, but got " + attempt;
    }
}