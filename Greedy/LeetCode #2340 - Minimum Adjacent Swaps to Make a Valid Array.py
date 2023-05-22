'''
LeetCode #2340 - Minimum Adjacent Swaps to Make a Valid Array prompt:

You are given a 0-indexed integer array nums.

Swaps of adjacent elements are able to be performed on nums.

A valid array meets the following conditions:

- The largest element (any of the largest elements if there are multiple) is at 
the rightmost position in the array.
- The smallest element (any of the smallest elements if there are multiple) is 
at the leftmost position in the array.

Return the minimum swaps required to make nums a valid array.

Example 1:
Input: nums = [3,4,5,5,3,1]
Output: 6
Explanation: Perform the following swaps:
- Swap 1: Swap the 3rd and 4th elements, nums is then [3,4,5,3,5,1].
- Swap 2: Swap the 4th and 5th elements, nums is then [3,4,5,3,1,5].
- Swap 3: Swap the 3rd and 4th elements, nums is then [3,4,5,1,3,5].
- Swap 4: Swap the 2nd and 3rd elements, nums is then [3,4,1,5,3,5].
- Swap 5: Swap the 1st and 2nd elements, nums is then [3,1,4,5,3,5].
- Swap 6: Swap the 0th and 1st elements, nums is then [1,3,4,5,3,5].
It can be shown that 6 swaps is the minimum swaps required to make a valid array.

Example 2:
Input: nums = [9]
Output: 0
Explanation: The array is already valid, so we return 0.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
'''

class Solution:
	# Time complexity:	O(n), where n is size of nums arr
	# Space complexity: O(1)
	def minimumSwaps(self, nums: list[int]) -> int:
		# store min_num & max_num
		max_num = max_idx = 0
		min_num = min_idx = float("infinity")
		for idx, num in enumerate(nums):
			if num < min_num:	# only care about min_num closest to begining of arr
				min_num = num
				min_idx = idx
			if num >= max_num:	# update max_num if closer to end of arr
				max_num = num
				max_idx = idx
		if min_idx > max_idx: 	# if condition met we swap min & max num at same time (-1)
			return (min_idx) + (len(nums) - 1 - max_idx) - 1
		return (min_idx) + (len(nums) - 1 - max_idx)

	def test_minSwaps(self, nums: list[int], exp: int) -> bool:
		ex = self.minimumSwaps(nums = nums)
		assert ex == exp, f'Expected {exp}, but got {ex}'

# Ex 1: 
Solution().test_minSwaps(nums = [3,4,5,5,3,1], exp = 6)

# Ex 2:
Solution().test_minSwaps(nums = [9], exp = 0)