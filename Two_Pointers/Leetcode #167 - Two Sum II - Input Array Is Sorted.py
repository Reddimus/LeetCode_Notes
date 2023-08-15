'''
Leetcode #167 - Two Sum II - Input Array Is Sorted prompt:

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers 
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array 
[index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same 
element twice.

Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

My example:
Input: numbers = [1, 3, 5, 9, 11], target = 14
Output: [1,4]

Constraints:
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
'''

class Solution:
	# Time complexity: 	O(n), where n is len of numbers arr
	# Space complexity: O(1)
	def twoSum(self, numbers: list[int], target: int) -> list[int]:
		l_ptr, r_ptr = 0, len(numbers) - 1
		while l_ptr < r_ptr:
			curr_sum = numbers[l_ptr] + numbers[r_ptr]
			if target > curr_sum:
				l_ptr += 1
			elif target < curr_sum:
				r_ptr -= 1
			# curr_sum == target sum
			else:
				return [l_ptr + 1, r_ptr + 1]
		return -1

# Ex 1:
assert Solution().twoSum(numbers = [2,7,11,15], target = 9) == [1, 2], f'Expected: {[1, 2]} but got {Solution().twoSum(numbers = [2,7,11,15], target = 9)}'

# Ex 2:
assert Solution().twoSum(numbers = [2,3,4], target = 6) == [1, 3], f'Expected {[1, 3]} but got {Solution().twoSum(numbers = [2,3,4], target = 6)}'

# Ex 3:
assert Solution().twoSum(numbers = [-1,0], target = -1) == [1, 2], f'Expected {[1, 2]} but got {Solution().twoSum(numbers = [-1,0], target = -1)}'

# My Ex:
assert Solution().twoSum(numbers = [1, 3, 5, 9, 11], target = 14) == [2, 5], f'Expected {[1, 4]} but got {Solution().twoSum(numbers = [-1,0], target = -1)}'