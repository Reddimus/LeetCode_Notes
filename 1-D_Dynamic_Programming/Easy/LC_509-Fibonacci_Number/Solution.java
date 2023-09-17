class Solution {
    // T: O(n), M: O(1)
    public int fib(int n) {
        if (n <= 1)
            return n;
        
        // start from 2
        int n0 = 0, n1 = 1;
        for (int num = 2; num <= n; num++) {
            int temp = n0 + n1;
            n0 = n1;
            n1 = temp;
        }
        return n1;
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
        attempt = sol.fib(2);
        assert attempt == 1 : "Expected 1, but got " + attempt;
        // Ex2
        attempt = sol.fib(3);
        assert attempt == 2 : "Expected 2, but got " + attempt;
        // Ex3
        attempt = sol.fib(4);
        assert attempt == 3 : "Expected 3, but got " + attempt;
    }
}