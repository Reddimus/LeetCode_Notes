'''
LeetCode #35 - Search Insert Position prompt:

Given a sorted array of distinct integers and a target value, return the index if 
the target is found. If not, return the index where it would be if it were inserted 
in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
'''

class Solution:
    # Binary Search approach
    # T: O(log n), M: O(1), where n is size of nums
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    '''
    # Other Binary Search approach
    # T: O(log n), M: O(1), where n is size of nums
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
        return lo
    '''

sol = Solution()
# Ex 1:
attempt = sol.searchInsert(nums = [1,3,5,6], target = 5)
assert attempt == 2, f'Expected 2 but got {attempt}'
# Ex 2:
attempt = sol.searchInsert(nums = [1,3,5,6], target = 2)
assert attempt == 1, f'Expected 1 but got {attempt}'
# Ex 3:
attempt = sol.searchInsert(nums = [1,3,5,6], target = 7)
assert attempt == 4, f'Expected 4 but got {attempt}'
# Test case 4:
attempt = sol.searchInsert(nums = [1], target = 0)
assert attempt == 0, f'Expected 0 but got {attempt}'
# Test case 5:
attempt = sol.searchInsert(nums = [1], target = 2)
assert attempt == 1, f'Expected 1 but got {attempt}'