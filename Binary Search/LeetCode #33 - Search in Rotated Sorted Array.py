'''
LeetCode #33 - Seach in Rotated Sorted Array prompt:
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown 
pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], 
nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For 
example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become 
[4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return 
the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity. 

Example 1:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4

Example 2:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4
'''
class Solution:
	# Time complexity: 	O(log n)
	# Space complexity: O(1)
	def search(self, nums: list[int], target: int) -> int:
		l_ptr, r_ptr = 0, len(nums) - 1

		while l_ptr <= r_ptr:
			# midpoint = left + half dist
			mid_pt = l_ptr + (r_ptr - l_ptr) // 2
			if target == nums[mid_pt]:
				return mid_pt
			# left sorted portion
			if nums[l_ptr] <= nums[mid_pt]:
				# if target not in left sorted range
				if target > nums[mid_pt] or target < nums[l_ptr]:
					l_ptr = mid_pt + 1
				else:
					r_ptr = mid_pt - 1
			# right sorted portion
			else:
				# if target not in right sorted range
				if target < nums[mid_pt] or target > nums[r_ptr]:
					r_ptr = mid_pt - 1
				else:
					l_ptr = mid_pt + 1
		return -1
	'''
	# Time complexity: 	O(log n)
	# Space complexity: O(1)
	def search(self, nums: list[int], target: int) -> int:
		l_ptr, r_ptr = 0, len(nums) - 1
		while l_ptr <= r_ptr:
			# midpoint = left + half_len
			mid_pt = l_ptr + (r_ptr - l_ptr) // 2
			l_num, r_num, mid_num = nums[l_ptr], nums[r_ptr], nums[mid_pt]
			# check left unshifted section
			if (l_num < target and target < mid_num):
				r_ptr = mid_pt - 1
			# check right unshifted section
			elif (mid_num < target and target < r_num):
				l_ptr = mid_pt + 1
			elif l_num == target:
				return l_ptr
			elif r_num == target:
				return r_ptr
			elif mid_num == target:
				return mid_pt
			# check left shifted section
			elif mid_num > r_num:
				l_ptr = mid_pt + 1
			# check right shifted section
			elif mid_num < l_num:
				r_ptr = mid_pt - 1
			# not found
			else:
				return -1
	'''

# Ex 1:
assert Solution().search(nums = [4, 5, 6, 7, 0, 1, 2], target = 0) == 4

# Ex 2:
assert Solution().search(nums = [4, 5, 6, 7, 0, 1, 2], target = 3) == -1

# Ex 3:
assert Solution().search(nums = [1], target = 0) == -1

# Testcase 4:
assert Solution().search(nums = [0, 1, 2, 3], target = 3) == 3

# Testcase 5:
assert Solution().search(nums = [0, 1, 2, 3], target = 0) == 0

# Testcase 6:
assert Solution().search(nums = [0, 1, 2, 3], target = -1) == -1

# Test case 7:
assert Solution().search(nums = [7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6], target = 0) == 2 or 3

# Test case 8:
assert Solution().search(nums = [7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6], target = 100) == -1

# Test case 8:
assert Solution().search(nums = [7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6], target = 6) == 14 or 15

# Test case 9:
assert Solution().search(nums = [7, 7, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6], target = 7) == 0 or 1