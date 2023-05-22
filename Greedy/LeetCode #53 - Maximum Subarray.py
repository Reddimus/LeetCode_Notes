'''
LeetCode #53 - Maximum Subarray prompt:

Given an integer array nums, find the subarray with the largest 
sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another 
solution using the divide and conquer approach, which is more subtle.
'''

class Solution:
	# Greedy Kadane's algorithm
	# Time complexity: 	O(n), where n is size of nums arr
	# Space complexity: O(1)
	def maxSubArray(self, nums: list[int]) -> int:
		curr_sum, max_sum = 0, nums[0]	
		for num in nums:
			curr_sum = max(curr_sum, 0)		# we do not want curr_sum to fall below 0
			curr_sum += num
			max_sum = max(max_sum, curr_sum)
		return max_sum

	def testcase(self, nums: list[int], exp: int) -> bool:
		ex = self.maxSubArray(nums = nums)
		assert ex == exp, f'Expected {exp}, but got {ex}'

# Ex 1
Solution().testcase(nums = [-2,1,-3,4,-1,2,1,-5,4], exp = 6)

# Ex 2
Solution().testcase(nums = [1], exp = 1)

# Ex 3
Solution().testcase(nums = [5,4,-1,7,8], exp = 23)
