class Solution {
    public int uniquePaths(int m, int n) {
        return -1;
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