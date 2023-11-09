import java.util.*;

// T&M: O(m * n), where m = rows and n = cols from grid input
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;

        int maxArea = 0;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                // if land and coordinates not visited
                if (grid[r][c] == 1)
                    maxArea = Math.max(maxArea, dfs(r, c, rows, cols, grid));
                    // maxArea = Math.max(maxArea, bfs(r, c, rows, cols, grid));
            }
        }

        return maxArea;
    }

    private int dfs(int r, int c, int rows, int cols, int[][] grid) {
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

    private static class Indices {
        final int row, col;
        Indices(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
    private int bfs(int r, int c, int rows, int cols, int[][] grid) {
        grid[r][c] = 0; // visited cell
        Queue<Indices> q = new LinkedList<>();
        q.add(new Indices(r, c));

        int area = 1;
        Indices[] directions = {new Indices(1, 0),  // down
                                new Indices(-1, 0),     // up
                                new Indices(0, 1),  // right
                                new Indices(0, -1)};    // left
        // while there are connected land coordinates to visit
        while (!q.isEmpty()) {
            Indices currCell = q.poll();    // visit coordinates in FCFS/FIFO order
            // visit neighboring coordinates
            for (Indices dir : directions) {
                final int neighbRow = currCell.row + dir.row;
                final int neighbCol = currCell.col + dir.col;
                // if neigboring coordinates are land & not visited
                if ((-1 < neighbRow && neighbRow < rows) &&
                (-1 < neighbCol && neighbCol < cols) &&
                grid[neighbRow][neighbCol] == 1) {
                    grid[neighbRow][neighbCol] = 0; // visited cell
                    q.add(new Indices(neighbRow, neighbCol));
                    ++area;
                }
            }
        }

        return area;
    }
}

class TestCases {
    public static void main(String[] args) {
        // In terminal:
        // Compile:     "javac Solution.java"
        // Test cases:  "java -ea TestCases"
        int[][] grid;
        int attempt;
        // Example 1:
        grid = new int[][] {
            {0,0,1,0,0,0,0,1,0,0,0,0,0},
            {0,0,0,0,0,0,0,1,1,1,0,0,0},
            {0,1,1,0,1,0,0,0,0,0,0,0,0},
            {0,1,0,0,1,1,0,0,1,0,1,0,0},
            {0,1,0,0,1,1,0,0,1,1,1,0,0},
            {0,0,0,0,0,0,0,0,0,0,1,0,0},
            {0,0,0,0,0,0,0,1,1,1,0,0,0},
            {0,0,0,0,0,0,0,1,1,0,0,0,0}
        };
        attempt = new Solution().maxAreaOfIsland(grid);
        assert attempt == 6 : "Expected 6, but got " + attempt;

        // Example 2:
        grid = new int[][] {{0,0,0,0,0,0,0,0}};
        attempt = new Solution().maxAreaOfIsland(grid);
        assert attempt == 0 : "Expected 0, but got " + attempt;

        // Test case 3:
        grid = new int[][] {{0}};
        attempt = new Solution().maxAreaOfIsland(grid);
        assert attempt == 0 : "Expected 0, but got " + attempt;

        // Test case 4:
        grid = new int[][] {{1}};
        attempt = new Solution().maxAreaOfIsland(grid);
        assert attempt == 1 : "Expected 1, but got " + attempt;
    }
}