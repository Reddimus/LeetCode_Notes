class Solution {
    // Sliding window method; buyPrice = lPtr, price = rPtr
    // T: O(n), M: O(1), where n is size of prices
    public int maxProfit(int[] prices) {
        int maxProfit = 0, buyPrice = prices[0];
        for (int price : prices) {
            buyPrice = Math.min(buyPrice, price);
            int performance = price - buyPrice;
            maxProfit = Math.max(maxProfit, performance);
        }
        return maxProfit;
    }
}

class TestCases {
    public static void main(String[] args) {
        // In terminal:
        // $ javac Solution.java
        // $ java -ea TestCases
        Solution sol = new Solution();
        int attempt;

        // Ex1
        attempt = sol.maxProfit(new int[]{7,1,5,3,6,4});
        assert attempt == 5 : "Expected 5, but got " + attempt;
        // Ex2
        attempt = sol.maxProfit(new int[]{7,6,4,3,1});
        assert attempt == 0 : "Expected 0, but got " + attempt;
        // Test case 3
        attempt = sol.maxProfit(new int[]{1});
        assert attempt == 0 : "Expected 0, but got " + attempt;
    }
}