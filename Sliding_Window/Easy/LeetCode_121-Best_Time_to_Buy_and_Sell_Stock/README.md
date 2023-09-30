# LeetCode #121 - Best Time to Buy And Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the *maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

### Example 1:
#### Input
```
prices = [7, 1, 5, 3, 6, 4]
```
#### Output
```
5
```
#### Explanation
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

### Example 2:
#### Input
```
prices = [7, 6, 4, 3, 1]
```
#### Output
```
0
```
#### Explanation
In this case, no transactions are done and the max profit = 0.

### Constraints
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`


### Hints:
- You need to purchase the stock before you can sell it.
- Cover the edge cases where the array is size 1.
# Solutions:

https://github.com/Reddimus/LeetCode_Notes/Sliding_Window/Easy/LeetCode_121-Best_Time_to_Buy_and_Sell_Stock

### **Sliding Window Approach**
### Intuition:
The problem is asking us to find the maximum difference between two numbers in the array, where the smaller number comes before the larger number. We can use a sliding window to keep track of the smallest number we've seen so far, and the maximum difference between the current number and the smallest number we've seen so far. Imagine the left pointer/element/stock price is the smallest number we've seen so far, and the right pointer/element/stock price is the current number. We can keep track of the maximum difference between the two pointers/elements/stock prices, and return that as our answer.

### Steps:
1. Initialize a `max_profit` variable to `0`, and a `buy_price` variable to the first element in the array.
2. Iterate through the array, starting at the second element.
3. Update the `buy_price` to the minimum of the current `buy_price` and the current element.
4. Update the `max_profit` to the maximum of the current `max_profit` and the difference between the current element and the `buy_price`.
5. Return the `max_profit`.

### Time & Space complexity:
**Time:** `O(n)`  
**Space:** `O(1)`

Where `n` is the length of the input array and we only passed through the array of prices once.

### Python code:
```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit, buy_price = 0, prices[0]
        for price in prices:
            buy_price = min(buy_price, price)
            max_profit = max(max_profit, price - buy_price)
        return max_profit
```

### C++ Code:
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0, buyPrice = prices[0];
        for (int price : prices){
            buyPrice = min(buyPrice, price);
            maxProfit = max(maxProfit, price - buyPrice);
        }
        return maxProfit;
    }
};
```

### C Code:
```c
int maxProfit(int* prices, int pricesSize) {
    int maxProfit = 0, buyPrice = prices[0];
    for (int idx = 0; idx < pricesSize; ++idx){
        if (buyPrice > prices[idx])
            buyPrice = prices[idx];
        
        int performance = prices[idx] - buyPrice;
        
        if (performance > maxProfit)
            maxProfit = performance;
    }
    return maxProfit;
}
```

### Java Code:
```java
class Solution {
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
```
