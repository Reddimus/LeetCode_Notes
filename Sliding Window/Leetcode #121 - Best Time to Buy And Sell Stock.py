'''
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
'''

class Solution:
	# T: O(n), O(1), where n is size of prices list
	# We know the price of each stock in given days
	def maxProfit(self, prices: list[int]) -> int:
		max_profit, lowest = 0, prices[0]
		# As we iterate through prices list we calculate the current profit/performance
		for price in prices:
			if price < lowest:
				lowest = price
			perf = price - lowest
			# if a new max profit found change max profit value
			max_profit = max(max_profit, perf)
		return max_profit

s = Solution()
# Ex 1
attempt = s.maxProfit(prices = [7, 1, 5, 3, 6, 4])
assert attempt == 5, f'Expected 5 but got {attempt}'
# Ex 2
attempt = s.maxProfit(prices = [7, 6, 4, 3, 1])
assert attempt == 0, f'Expected 0 but got {attempt}'
# Ex 1
attempt = s.maxProfit(prices = [7, 5, 3, 6, 4])
assert attempt == 3, f'Expected 3 but got {attempt}'
