'''
LeetCode #217 - Contains Duplicate prompt:
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
	# Set approach
	# T: O(n), M: O(n), where n is size of nums arr
	def containsDuplicate(self, nums: list[int]) -> bool:
		hashset = set()
		for num in nums:
			if num in hashset:
				return True
			hashset.add(num)
		return False

	'''
	# Sorting approach
	# T: O(n log n), M: O(1), where n is size of nums arr
	def containsDuplicate(self, nums: list[int]) -> bool:
		nums.sort()
		for idx in range(len(nums) - 1):
			if nums[idx] == nums[idx + 1]:
				return True
		return False
	'''

	'''
	# Brute force approach; check every overlapping combination
	# T: O(n^2), M: O(1), where n is size of nums arr
	def containsDuplicate(self, nums: list[int]) -> bool:
		for idx0 in range(len(nums) - 1):
			for idx1 in range(idx0 + 1, len(nums)):
				if nums[idx0] == nums[idx1]:
					return True
		return False
	'''

s = Solution()
# Ex 1
assert s.containsDuplicate(nums = [1, 2, 3, 1]) == True, f"Expected True but got False"

# Ex 2
assert s.containsDuplicate(nums = [1, 2, 3, 4]) == False, f"Expected True but got False"

# Ex 3
assert s.containsDuplicate(nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True, f"Expected False but got True"

# Ex 3
assert s.containsDuplicate(nums = [1]) == False, f"Expected True but got False"
