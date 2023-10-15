// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

/*
void print2DArr(vector<vector<int>> arr) {
    for (auto row : arr) {
        for (auto col : row) {
            cout << col << " ";
        }
        cout << endl;
    }
}
*/

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
        // cout << "Input grid: " << endl;
        // print2DArr(obstacleGrid);

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

        // cout << "DP grid: " << endl;
        // print2DArr(dp);
        // cout << endl;

        return dp[0][0];
    }
    */

    /*
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
    */

    /*
    // Top-Down Approach with full dp grid
    // T: O(m*n), M: O(m*n), where m = rows, n = cols
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        // cout << "Input grid: " << endl;
        // print2DArr(obstacleGrid);

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

        // cout << "DP grid: " << endl;
        // print2DArr(dp);
        // cout << endl;

        return dp[rows][cols];
    }
    */
};

int main() {
    Solution sol;
    int attempt;
    vector<vector<int>> obstacleGrid;

    // Ex1
    obstacleGrid = {{0,0,0},{0,1,0},{0,0,0}};
    attempt = sol.uniquePathsWithObstacles(obstacleGrid);
    assert(attempt == 2);
    // Ex2:
    obstacleGrid = {{0,1},{0,0}};
    attempt = sol.uniquePathsWithObstacles(obstacleGrid);
    assert(attempt == 1);
    // Test case 3:
    obstacleGrid = {{0,0},{1,1},{0,0}};
    attempt = sol.uniquePathsWithObstacles(obstacleGrid);
    assert(attempt == 0);
    // Test case 4:
    obstacleGrid = {{0,0,0,0},{0,1,0,0},{0,0,0,0},{0,0,0,0}};
    attempt = sol.uniquePathsWithObstacles(obstacleGrid);
    assert(attempt == 8);
    // Test case 5:
    obstacleGrid = {{0,1}};
    attempt = sol.uniquePathsWithObstacles(obstacleGrid);
    assert(attempt == 0);
    return 0;
}