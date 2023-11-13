//#include <bits/stdc++.h>
#include <vector>
#include <queue>
#include <cassert>

using namespace std;

// Matrix Graphs - Breadth First Search (BFS) approach
// T: O(n^2), M: O(n^2), where n is the number of rows and columns in the grid
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


int main() {
    int attempt;
    vector<vector<int>> grid;

    // Example 1
    grid = {{0, 1}, 
            {1, 0}};
    attempt = Solution().shortestPathBinaryMatrix(grid);
    assert(attempt == 2);

    // Example 2:
    grid = {{0,0,0}, 
            {1,1,0},
            {1,1,0}};
    attempt = Solution().shortestPathBinaryMatrix(grid);
    assert(attempt == 4);

    // Example 3:
    grid = {{1,0,0},
            {1,1,0},
            {1,1,0}};
    attempt = Solution().shortestPathBinaryMatrix(grid);
    assert(attempt == -1);

    // Test Case 4:
    grid = {{0}};
    attempt = Solution().shortestPathBinaryMatrix(grid);
    assert(attempt == 1);

    // Test Case 5:
    grid = {{1}};
    attempt = Solution().shortestPathBinaryMatrix(grid);
    assert(attempt == -1);

    // Test Case 6:
    grid = {{0,0,0,0,0,0,1}, 
            {1,1,1,1,1,0,1}, 
            {1,0,0,1,1,0,0}, 
            {0,1,1,0,1,0,1}, 
            {0,1,1,1,0,0,1}, 
            {0,1,1,1,1,1,1}, 
            {0,0,0,0,0,0,0}};
    attempt = Solution().shortestPathBinaryMatrix(grid);
    assert(attempt == 21);
    return 0;
}