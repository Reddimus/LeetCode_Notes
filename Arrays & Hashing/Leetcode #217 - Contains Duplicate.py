'''
Leetcode #217 - Contains Duplicate prompt:
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1, 2, 3, 1]
Output: true

Example 2:
Input: nums = [1, 2 ,3, 4]
Output: false

Example 3:
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''

class Solution:
	# Time complexity: O(n)
	# Space complexity: O(n)
	def containsDuplicate(self, nums: list[int]) -> bool:
		hashset = set()
		for num in nums:
			if num in hashset:
				return True
			hashset.add(num)
		return False
	'''
	# Sorting
	# Time complexity: O(n log n) + O(n) = O(n log n)
	# Space complexity: O(1)
	def containsDuplicate(self, nums: list[int]) -> bool:
		nums.sort()
		for idx in range(len(nums)):
			if nums[idx] == nums[idx + 1]:
				return True
		return False
	'''
# Ex 1
assert Solution().containsDuplicate(nums = [1, 2, 3, 1]) == True

# Ex 2
assert Solution().containsDuplicate(nums = [1, 2, 3, 4]) == False

# Ex 3
assert Solution().containsDuplicate(nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
