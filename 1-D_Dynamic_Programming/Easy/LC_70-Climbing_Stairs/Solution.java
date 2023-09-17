class Solution {
    // T: O(n), M: O(1), where n is size of nums
    public int climbStairs(int n) {
        if (n <= 3)
            return n;
        
        // Bottom up approach
        int n1 = 2, n2 = 3;
        for (int stairs = 4; stairs <= n; stairs++) {
            // Shift window to the right
            int temp = n1 + n2;
            n1 = n2;
            n2 = temp;
        }
        return n2;
    }
}

class TestCases {
    public static void main(String[] args) {
        // In terminal:
        // Compile:     "javac Solution.java"
        // Test cases:  "java -ea TestCases"
        Solution sol = new Solution();
        int attempt;

        // Ex1
        attempt = sol.climbStairs(attempt = 2);
        assert attempt == 2 : "Expected 2, but got " + attempt;
        // Ex2
        attempt = sol.climbStairs(attempt = 3);
        assert attempt == 3 : "Expected 3, but got " + attempt;
        // Test Case 3
        attempt = sol.climbStairs(attempt = 4);
        assert attempt == 5 : "Expected 5, but got " + attempt;
        // Test Case 4
        attempt = sol.climbStairs(attempt = 5);
        assert attempt == 8 : "Expected 8, but got " + attempt;
    }
}