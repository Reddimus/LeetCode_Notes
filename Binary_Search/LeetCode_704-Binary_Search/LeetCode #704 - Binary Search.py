'''
LeetCode #704 - Binary Search prompt:

Given an array of integers nums which is sorted in ascending order, and an 
integer target, write a function to search target in nums. If target 
exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:
1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.
'''

class Solution:
	# Binary Search
	# T: O(log n), M: O(1), where n is size of nums
	def search(self, nums: list[int], target: int) -> int:
		l_idx, r_idx = 0, len(nums) - 1
		while l_idx <= r_idx:
			m_idx = (l_idx + r_idx) // 2
			# if number not within +-mid range throw away subarray range
			if nums[m_idx] < target:
				l_idx = m_idx + 1
			elif nums[m_idx] > target:
				r_idx = m_idx - 1
			# else mid element = target
			else:
				return m_idx
		return -1

sol = Solution()
# Ex 1:
attempt = sol.search(nums = [-1, 0, 3, 5, 9, 12], target = 9)
assert attempt == 4, f'Expected 4 but got {attempt}'
# Ex 2:
attempt = sol.search(nums = [-1, 0, 3, 5, 9, 12], target = 2)
assert attempt == -1, f'Expected -1 but got {attempt}'
# Test case 3:
attempt = sol.search(nums = [9], target = 9)
assert attempt == 0, f'Expected 0 but got {attempt}'
# Test case 4:
attempt = sol.search(nums = [9], target = 10)
assert attempt == -1, f'Expected -1 but got {attempt}'
# Test case 5:
attempt = sol.search(nums = [2, 5, 7, 9, 11, 11, 11], target = 9)
assert attempt == 3, f'Expected 3 but got {attempt}'
# Test case 6:
attempt = sol.search(nums = [2, 5, 7, 9, 11, 11, 11], target = 11)
assert attempt == 4 or 5 or 6, f'Expected 4 or 5 or 6 but got {attempt}'
# Test case 7:
attempt = sol.search(nums = [2, 5, 7, 9, 11, 11, 11], target = 12)
assert attempt == -1, f'Expected -1 but got {attempt}'
