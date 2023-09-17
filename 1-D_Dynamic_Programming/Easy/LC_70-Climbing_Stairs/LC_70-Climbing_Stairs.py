class Solution:
	# T: O(n), M: O(1), where n is the number of stairs
	def climbStairs(self, n: int) -> int:
		if n <= 3:
			return n
		# bottom up approach
		n1, n2 = 2, 3
		for i in range(4, n + 1):	# start from 4 stair steps
			n1, n2 = n2, n1 + n2	# shift window right/ update latest varaible
		return n2

sol = Solution()

# Ex 1
attempt = sol.climbStairs(n = 2)
assert attempt == 2, f'Expected {2}, but got {attempt}'
# Ex 2
attempt = sol.climbStairs(n = 3)
assert attempt == 3, f'Expected {3}, but got {attempt}'
# Test case 3
attempt = sol.climbStairs(n = 4)
assert attempt == 5, f'Expected {5}, but got {attempt}'