#include <bits/stdc++.h>

using namespace std;

// T&M: O(m * n), where m = rows and n = cols from grid input
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
};

int main() {
    int attempt;
    vector<vector<int>> grid;

    // Example 1:
    grid = {
        {0,0,1,0,0,0,0,1,0,0,0,0,0},
        {0,0,0,0,0,0,0,1,1,1,0,0,0},
        {0,1,1,0,1,0,0,0,0,0,0,0,0},
        {0,1,0,0,1,1,0,0,1,0,1,0,0},
        {0,1,0,0,1,1,0,0,1,1,1,0,0},
        {0,0,0,0,0,0,0,0,0,0,1,0,0},
        {0,0,0,0,0,0,0,1,1,1,0,0,0},
        {0,0,0,0,0,0,0,1,1,0,0,0,0}
    };
    attempt = Solution().maxAreaOfIsland(grid);
    assert(attempt == 6 && "Failed Example 1: Expected 6");

    // Example 2:
    grid = {
        {0,0,0,0,0,0,0,0}
    };
    attempt = Solution().maxAreaOfIsland(grid);
    assert(attempt == 0 && "Failed Example 2: Expected 0");

    // Test Case 3:
    grid = {{0}};
    attempt = Solution().maxAreaOfIsland(grid);
    assert(attempt == 0 && "Failed Test Case 3: Expected 0");

    // Test Case 4:
    grid = {{1}};
    attempt = Solution().maxAreaOfIsland(grid);
    assert(attempt == 1 && "Failed Test Case 4: Expected 1");
}