'''
Leetcode #238 - Product of Array Except Self Prompt:
Given an integer array nums, return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
integer.

You must write an algorithm that runs in O(n) time and without using the 
division operation.

Example 1:
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Example 2:
Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
 
Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 
32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
'''

class Solution:
	def productExceptSelf(self, nums: list[int]) -> list[int]:
		# Time complexity: 	O(3n) = O(n) 
		# Space complexity: O(1)
		prod = [1] * len(nums)
		prefix = 1
		for idx in range(len(nums)):
			prod[idx] = prefix
			prefix *= nums[idx]
		postfix = 1
		for idx in range(len(nums) - 1, -1, -1):
			prod[idx] *= postfix
			postfix *= nums[idx]
		return prod

		'''
		# Time complexity: 	O(4n) = O(n) 
		# Space complexity: O(2n) = O(n)
		prefix, pre_arr = 1, [0] * len(nums)
		postfix, post_arr = 1, [0] * len(nums)
		for idx, num in enumerate(nums):
			prefix *= num
			pre_arr[idx] = prefix
			postfix *= nums[-idx - 1]
			post_arr[-idx - 1] = postfix

		print("pre_arr:", pre_arr)
		print("post_arr:", post_arr)

		prod_arr = []
		for idx in range(len(nums)):
			if idx != 0 and idx != len(nums) - 1:
				prod = pre_arr[idx - 1] * post_arr[idx + 1]
				prod_arr.append(prod)
			elif idx == 0:
				prod_arr.append(post_arr[idx + 1])
			elif idx == len(nums) - 1:
				prod_arr.append(pre_arr[idx - 1])
			print(prod_arr)
		return prod_arr
		'''

# Ex 1
assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

# Ex 2
assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
