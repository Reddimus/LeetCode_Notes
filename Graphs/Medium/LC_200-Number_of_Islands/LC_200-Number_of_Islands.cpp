#include <bits/stdc++.h>

using namespace std;

// T & M: O(m * n), where m = rows and n = cols from grid input
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

/*
// BFS Solution with set of visited coordinates (object(s))
private:
    vector<vector<char>> grid;
    int rows, cols;
    struct coordinates {const int row, col;};
    struct coordinates_hash {
        size_t operator()(const coordinates &coord) const {
            return hash<int>()(coord.row) ^ hash<int>()(coord.col);
        }
    };
    struct coordinates_equal {
        bool operator()(const coordinates &lhs, const coordinates &rhs) const {
            return lhs.row == rhs.row && lhs.col == rhs.col;
        }
    };
    unordered_set<coordinates, coordinates_hash, coordinates_equal> visited;

    void bfs(int r, int c) {
        queue<coordinates> q;
        visited.insert({r, c});
        q.push({r, c});

        // while there are connected land coordinates to visit
        while (!q.empty()) {
            coordinates currCoords = q.front();
            q.pop();	// visit coordinates in FCFS/FIFO order
            vector<coordinates> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            for (coordinates &dir : directions) {
                int neighbR = currCoords.row + dir.row;
                int neighbC = currCoords.col + dir.col;
                // if neigboring coordinates are land & not visited
                if ((-1 < neighbR && neighbR < rows) &&
                (-1 < neighbC && neighbC < cols) &&
                grid[neighbR][neighbC] == '1' &&
                visited.find({neighbR, neighbC}) == visited.end()) {
                    q.push({neighbR, neighbC});
                    visited.insert({neighbR, neighbC});
                }
            }
        }
    }
*/
};

int main() {
    int attempt;
    vector<vector<char>> grid;

    // Example 1
    grid = {
        {'1','1','1','1','0'},
        {'1','1','0','1','0'},
        {'1','1','0','0','0'},
        {'0','0','0','0','0'}
    };
    attempt = Solution().numIslands(grid);
    assert(attempt == 1 && "Failed Example 1: Expected 1 island");

    // Example 2
    grid = {
        {'1','1','0','0','0'},
        {'1','1','0','0','0'},
        {'0','0','1','0','0'},
        {'0','0','0','1','1'}
    };
    attempt = Solution().numIslands(grid);
    assert(attempt == 3 && "Failed Example 2: Expected 3 islands");

    // Test Case 3:
    grid = {
        {'0','0','1','0','0','1','0','0','0','0','0','0','0','0','1','1','0','1','0','0'},
        {'0','1','0','0','0','0','1','1','0','0','0','1','0','0','1','1','0','0','0','0'},
        {'1','0','1','1','0','0','0','0','0','1','0','0','0','1','0','1','1','1','1','0'},
        {'1','1','0','0','0','0','0','0','0','0','1','0','0','1','1','1','1','1','1','1'},
        {'0','0','0','0','0','1','0','0','0','1','1','1','1','0','1','0','0','0','0','0'},
        {'0','1','1','1','0','0','0','1','0','1','0','1','0','0','1','0','1','1','0','0'},
        {'0','0','0','0','0','0','0','0','1','1','1','0','0','1','1','0','0','0','0','0'},
        {'0','1','1','0','0','0','0','0','1','0','1','1','0','1','1','0','0','1','0','0'},
        {'0','0','1','1','1','0','0','1','0','0','0','0','0','0','0','1','1','1','0','1'},
        {'1','1','0','0','0','1','0','1','0','0','0','1','1','0','0','1','0','1','1','0'},
        {'0','0','0','0','0','0','1','0','1','1','0','0','1','0','1','1','1','1','0','1'},
        {'0','0','1','1','0','0','1','0','1','0','0','1','0','0','1','0','0','1','0','1'},
        {'0','1','0','0','0','0','0','1','0','0','0','0','0','0','1','1','1','0','0','0'},
        {'0','0','1','0','1','0','0','1','1','0','1','1','1','0','0','1','1','0','0','1'},
        {'1','0','1','0','1','0','1','0','0','0','0','0','0','0','1','0','0','1','1','0'},
        {'1','0','1','1','1','0','1','0','0','0','0','0','0','1','0','0','0','0','1','1'},
        {'1','0','0','0','0','1','0','0','0','0','0','0','1','0','0','0','0','0','1','1'},
        {'0','0','0','0','0','0','1','0','0','0','1','0','1','0','1','1','0','1','0','1'},
        {'1','0','0','1','0','0','0','0','0','0','1','0','0','0','0','0','1','1','1','1'},
        {'0','0','0','1','1','0','0','0','0','0','0','0','0','1','0','0','0','1','0','0'}
    };
    attempt = Solution().numIslands(grid);
    assert(attempt == 45 && "Failed Test Case 3: Expected 45 islands");

    return 0;
}