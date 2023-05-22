'''
LeetCode #70 - Climbing Stairs prompt:

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
'''

class Solution:
	# Time complexity:	O(n)
	# Space complexity: O(1)
	def climbStairs(self, n: int) -> int:
		if n <= 3:
			return n
		# bottom up approach
		n1, n2 = 2, 3
		for i in range(4, n + 1):	# start from 4 stair steps
			n1, n2 = n2, n1 + n2	# shift window right/ update latest varaible
		return n2

	def testcases(self, n: int, exp: int) -> bool:
		ex = self.climbStairs(n)
		assert ex == exp, f'Expected {exp}, but got {ex}' 

# Ex 1
Solution().testcases(n = 2, exp = 2)

# Ex 2
Solution().testcases(n = 3, exp = 3)

# Test case 3
Solution().testcases(n = 4, exp = 5)