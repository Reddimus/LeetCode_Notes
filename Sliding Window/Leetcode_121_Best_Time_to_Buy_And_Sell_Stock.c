/*
Leetcode #121 - Best Time to Buy And Sell Stock prompt:

You are given an array prices where prices[i] is the price of a given stock on 
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot 
achieve any profit, return 0.

Example 1:
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), 
profit = 6 - 1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed 
because you must buy before you sell.

Example 2:
Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
*/

#include <alg.h>
#include <assert.h>

int maxProfit(int* prices, int pricesSize){
    int max_prof = 0, min_price = prices[0];
    for (int idx = 0; idx < pricesSize; idx++){
        min_price = min(min_price, prices[idx]);
        int perf = prices[idx] - min_price;
        max_prof = max(max_prof, perf);
    }
    return max_prof;
}

int main(){
    // Ex1
    int prices1[] = {7, 1, 5, 3, 6, 4};
    int pricesSize1 = sizeof(prices1)/sizeof(prices1[0]);
    assert(maxProfit(prices1, pricesSize1) == 5);
    // Ex2
    int prices2[] = {7, 6, 4, 3, 1};
    int pricesSize2 = sizeof(prices2)/sizeof(prices2[0]);
    assert(maxProfit(prices2, pricesSize2) == 0);
}