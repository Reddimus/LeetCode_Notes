#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    // 1-D Dynamic Programming - Bottom-Up Approach
    // T: O(m*n), M: O(n), where m is num of rows, n is num of cols
    int uniquePaths(int m, int n) {
        vector<int> prevRow(n, 1);  // Solve last row base case

        for (int row = m-2; 0 <= row; row--) {
            vector<int> currRow(n, 0);
            currRow[n-1] = 1;   // Solve last col base case

            // Solve curr case using bottom up approach
            for (int col = n-2; 0 <= col; col--)
                currRow[col] = currRow[col+1] + prevRow[col];
            
            prevRow = currRow;
        }
        
        return prevRow[0];
    }

    /*
    // 2-D Dynamic Programming - Full Grid/Bottom-Up Approach
    // T&M: O(m*n), where m is num of rows, n is num of cols
    int uniquePaths(int m, int n) {
        vector<vector<int>> grid(m, vector<int>(n, 0));

        // Solve base case; last row and last cols
        for (int col = 0; col < n; col++)
            grid[m - 1][col] = 1;
        for (int row = 0; row < m; row++)
            grid[row][n-1] = 1;
        printGrid(grid);

        // Solve remaining cases using bottom up approach
        for (int row = m - 2; 0 <= row; row--) {
            for (int col = n - 2; 0 <= col; col--) {
                grid[row][col] = grid[row][col+1] + grid[row+1][col];
            }
        }
        printGrid(grid);
        
        return grid[0][0];
    }

    void printGrid(vector<vector<int>> &grid) {
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++)
                cout << grid[i][j] << " ";
            cout << endl;
        }
        cout << endl;
    }
    */
};

int main() {
    Solution sol;

    // Ex1
    assert(sol.uniquePaths(3, 7) == 28);
    // Ex2
    assert(sol.uniquePaths(3, 2) == 3);
}