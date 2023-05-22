'''
LeetCode #153 - Find Minimum in Rotated Sorted Array prompt:

Suppose an array of length n sorted in ascending order is rotated 
between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] 
might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 
time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the 
minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was 
rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was 
rotated 4 times. 

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
'''

class Solution:
    # Time complexity:  O(log n)
    # Space complexity: O(1)
    def findMin(self, nums: list[int]) -> int:
        l_ptr, r_ptr = 0, len(nums) - 1
        curr_min = float("inf")
        while l_ptr < r_ptr:
            # midpoint = left + half len
            mid_pt = l_ptr + (r_ptr - l_ptr) // 2
            curr_min = min(curr_min, nums[mid_pt])
            # right has the min 
            if nums[mid_pt] > nums[r_ptr]:
                l_ptr = mid_pt + 1
            # left has the min 
            else:
                r_ptr = mid_pt - 1 
        return min(curr_min, nums[l_ptr])

# Ex 1:
assert Solution().findMin(nums = [3, 4, 5, 1, 2]) == 1

# Ex 2:
assert Solution().findMin(nums = [4, 5, 6, 7, 0, 1, 2]) == 0

# Ex 3:
assert Solution().findMin(nums = [11, 13, 15, 17]) == 11

# Test case 4:
assert Solution().findMin(nums = [0, 1, 2, 3, 4, 5, 6, 7]) == 0

# Test case 5: 
assert Solution().findMin(nums = [4, 5, 5, 0, 0, 2, 2]) == 0

# Test case 6:
assert Solution().findMin(nums = [-5, -3, -2, 0, 1, 2, 4]) == -5

# Test case 7:
assert Solution().findMin(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3]) == 1

# Test case 8:
assert Solution().findMin(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3

# Test case 9:
assert Solution().findMin(nums = [2, 1]) == 1

# Test case 10:
assert Solution().findMin(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1

# Test case 11:
assert Solution().findMin(nums = [2, 3, 4, 5, 1]) == 1

# Test case 12:
assert Solution().findMin(nums = [1]) == 1

# Test case 13:
assert Solution().findMin(nums =[5, 1, 2, 3, 4]) == 1