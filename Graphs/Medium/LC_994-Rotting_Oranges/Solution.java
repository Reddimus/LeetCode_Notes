import java.util.*;

// Matrix Graphs - Breadth First Search (BFS) approach
// T & M: O(m*n), where m == rows and n = columns
class Solution {
    public int orangesRotting(int[][] grid) {
        final int rows = grid.length, cols = grid[0].length;
        int fresh = 0;
        Queue<Indices> rottenIdxs = new LinkedList<>(); // q indices of rotten oranges
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == 1)
                    ++fresh;
                if (grid[r][c] == 2)
                    rottenIdxs.add(new Indices(r, c));
            }
        }

        int minutes = 0;
        Indices[] directions = {new Indices(1, 0),
                                new Indices(0, 1),
                                new Indices(-1, 0),
                                new Indices(0, -1)};
        // While there are fresh oranges and rotten oranges queued
        while(fresh > 0 && !rottenIdxs.isEmpty()) {
            // Rotten all neighboring oranges at the same time
            final int qSize = rottenIdxs.size();
            for (int sameMinute = 0; sameMinute < qSize; ++sameMinute) {
                Indices currRotten = rottenIdxs.poll();
                for (Indices dir : directions) {
                    final int nghbrRow = currRotten.row + dir.row;
                    final int nghbrCol = currRotten.col + dir.col;
                    if ((-1 < nghbrRow && nghbrRow < rows) &&
                    (-1 < nghbrCol && nghbrCol < cols) &&
                    grid[nghbrRow][nghbrCol] == 1) {
                        grid[nghbrRow][nghbrCol] = 2;
                        rottenIdxs.add(new Indices(nghbrRow, nghbrCol));
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

    private static class Indices {
        final int row, col;
        Indices(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
}

class TestCases {
    public static void main(String[] args) {
        // In terminal:
        // Compile:     "javac Solution.java"
        // Test cases:  "java -ea TestCases"
        int attempt;
        int[][] grid;

        // Example 1:
        grid = new int[][] {{2,1,1},
                            {1,1,0},
                            {0,1,1}};
        attempt = new Solution().orangesRotting(grid);
        assert attempt == 4 : "Expected 4, but got " + attempt;

        // Example 2:
        grid = new int[][] {{2,1,1},
                            {0,1,1},
                            {1,0,1}};
        attempt = new Solution().orangesRotting(grid);
        assert attempt == -1 : "Expected -1, but got " + attempt;

        // Example 3:
        grid = new int[][] {{0,2}};
        attempt = new Solution().orangesRotting(grid);
        assert attempt == 0 : "Expected 0, but got " + attempt;

        // Test Case 4:
        grid = new int[][] {{0}};
        attempt = new Solution().orangesRotting(grid);
        assert attempt == 0 : "Expected 0, but got " + attempt;

        // Test Case 5:
        grid = new int[][] {{1}};
        attempt = new Solution().orangesRotting(grid);
        assert attempt == -1 : "Expected -1, but got " + attempt;

        // Test Case 6:
        grid = new int[][] {{2}};
        attempt = new Solution().orangesRotting(grid);
        assert attempt == 0 : "Expected 0, but got " + attempt;

        // Test Case 7:
        grid = new int[][] {{1,2}};
        attempt = new Solution().orangesRotting(grid);
        assert attempt == 1 : "Expected 1, but got " + attempt;
    }
}
