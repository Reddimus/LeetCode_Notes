'''
Leetcode #1 - Two sum prompt:

Given an array of integers nums and an integer target, return the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [2, 7]
Explanation: Because nums [0] + nums [1] == 9, we return [0, 1].

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [2, 4]

Example 3:
Input: nums = [3, 3], target = 6
Output: [3, 3]

Constraints:
• 2 <= nums.length <= 10^4
• -10^9 <= nums [i] <= 10^9
• -10^9 <= target <= 10^9
• Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
'''

class Solution:
	# Hashmap solution
	# Time complexity: O(n)
	# Space complexity: O(n)
	def twosum(nums: list[int], target: int) -> list[int]:
		prev_map = {}
		for idx, num in enumerate(nums):
			diff = target - num
			if diff in prev_map:
				return [prev_map[diff], num]
			prev_map[num] = diff
		return []

	# Array solution
	# Time complexity: 	O(n * (n - k)) = O(n^2)
	# Space complexity: O(n * (n - k)) = O(n^2)
	'''
	def twosum(nums: list[int], target: int) -> list[int]:
		for idx_0 in range(len(nums)):
			for idx_1 in range(idx_0 + 1, len(nums)):
				if (nums[idx_0] + nums[idx_1]) == target:
					return [nums[idx_0], nums[idx_1]]
		return []
	'''
# Ex 1
assert Solution.twosum(nums = [2, 7, 11, 15], target = 9) == [2, 7] or [7, 2]

# Ex 2
assert Solution.twosum(nums = [3, 2, 4], target = 6) == [2, 4] or [4, 2]

# Ex 3
assert Solution.twosum(nums = [3, 3], target = 6) == [3, 3]
