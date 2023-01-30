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
	# Time complexity: 	O(log n)
	# Space complexity: O(1)
	def search(self, nums: list[int], target: int) -> int:
		l_ptr, r_ptr = 0, len(nums) - 1
		while l_ptr <= r_ptr:
			# midpoint = left_ptr + ((total dist) // 2) = left_ptr + half dist
			mid = l_ptr + ((r_ptr - l_ptr) // 2)
			#mid = (l_ptr + r_ptr) // 2 	# can lead to overflow if l & r are to big
			if nums[mid] < target:
				l_ptr = mid + 1
			elif nums[mid] > target:
				r_ptr = mid - 1
			else:
				return mid
		return -1

# Ex 1:
assert Solution().search(nums = [-1, 0, 3, 5, 9, 12], target = 9) == 4

# Ex 2:
assert Solution().search(nums = [-1, 0, 3, 5, 9, 12], target = 2) == -1

# Test case 3:
assert Solution().search(nums = [9], target = 9) == 0

# Test case 4:
assert Solution().search(nums = [9], target = 10) == -1

# Test case 5:
assert Solution().search(nums = [2, 5, 7, 9, 11, 11, 11], target = 9) == 3

# Test case 6:
assert Solution().search(nums = [2, 5, 7, 9, 11, 11, 11], target = 11) == 4 or 5 or 6

# Test case 7:
assert Solution().search(nums = [2, 5, 7, 9, 11, 11, 11], target = 12) == -1
