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

#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

class Solution {
public:
    // Sliding Window algorithm; buyPrice = lPtr, price = rPtr
    // T: O(n), M: O(1), where n is size of prices
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0, buyPrice = prices[0];
        for (int price : prices){
            buyPrice = min(buyPrice, price);
            maxProfit = max(maxProfit, price - buyPrice);
        }
        return maxProfit;
    }

    // Brute force method; check every overlapping combination
    // T: O(n^2), M: O(1), where n is size of prices
    // int maxProfit(vector<int>& prices){
    //     int max_prof = 0;
    //     for (int idx0 = 0; idx0 < prices.size() - 1; idx0++){
    //         for (int idx1 = idx0 + 1; idx1 < prices.size(); idx1++){
    //             int perf = prices[idx1] - prices[idx0];
    //             max_prof = max(max_prof, perf);
    //         }
    //     }
    //     return max_prof;
    // }
};

int main(){
    Solution s;
    // Ex1
    vector<int> ex1 = {7, 1, 5, 3, 6, 4};
    assert(s.maxProfit(ex1) == 5);
    // Ex2
    vector<int> ex2 = {7, 6, 4, 3, 1};
    assert(s.maxProfit(ex2) == 0);
}
