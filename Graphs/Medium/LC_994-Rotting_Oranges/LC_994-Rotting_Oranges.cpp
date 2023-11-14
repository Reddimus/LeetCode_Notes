//#include <bits/stdc++.h>
#include <vector>
#include <cassert>
#include <queue>

using namespace std;

// Matrix Graphs - Breadth First Search (BFS) approach
// T & M: O(m*n), where m == rows and n = columns
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int rows = grid.size(), cols = grid[0].size();
        int fresh = 0;
        queue<indices> rottenIdxs;  // queue indices of rotten oranges
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == 1) 
                    ++fresh;
                if (grid[r][c] == 2)
                    rottenIdxs.push({r, c});
            }
        }

        int minutes = 0;
        vector<indices> directions = {{1,0}, {0,1}, {-1,0}, {0,-1}};
        // While there are fresh oranges and rotten oranges queued
        while (fresh > 0 && !rottenIdxs.empty()) {
            // Rotten all neighboring oranges at the same time
            int qSize = rottenIdxs.size();
            for (int sameMinute = 0; sameMinute < qSize; ++sameMinute) {
                indices currIdx = rottenIdxs.front();
                rottenIdxs.pop();
                for (indices& dir : directions) {
                    int nghbrRow = dir.row + currIdx.row;
                    int nghbrCol = dir.col + currIdx.col;
                    if ((-1 < nghbrRow && nghbrRow < rows) &&
                    (-1 < nghbrCol && nghbrCol < cols) &&
                    grid[nghbrRow][nghbrCol] == 1) {
                        grid[nghbrRow][nghbrCol] = 2;
                        rottenIdxs.push({nghbrRow, nghbrCol});
                        --fresh;
                    }
                }
            }

            ++minutes;
        }

        if (fresh == 0)
            return minutes;
        return -1;
    }
private:
    struct indices {const int row, col;};
};

int main() {
    int attempt;
    vector<vector<int>> grid;

    // Example 1:
    grid = {{2,1,1},
            {1,1,0},
            {0,1,1}};
    attempt = Solution().orangesRotting(grid);
    assert(attempt == 4);

    // Example 2:
    grid = {{2,1,1},
            {0,1,1},
            {1,0,1}};
    attempt = Solution().orangesRotting(grid);
    assert(attempt == -1);

    // Example 3:
    grid = {{0,2}};
    attempt = Solution().orangesRotting(grid);
    assert(attempt == 0);

    // Test Case 4:
    grid = {{0}};
    attempt = Solution().orangesRotting(grid);
    assert(attempt == 0);

    // Test Case 5:
    grid = {{1}};
    attempt = Solution().orangesRotting(grid);
    assert(attempt == -1);

    // Test Case 6:
    grid = {{2}};
    attempt = Solution().orangesRotting(grid);
    assert(attempt == 0);

    // Test Case 7:
    grid = {{2,1,1},
            {1,1,1},
            {0,1,2}};
    attempt = Solution().orangesRotting(grid);
    assert(attempt == 2);
    return 0;
}