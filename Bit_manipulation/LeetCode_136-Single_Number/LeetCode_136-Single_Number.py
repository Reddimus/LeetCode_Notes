'''
LeetCode #136 - Single Number prompt:

Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant 
extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

class Solution:
    # T: O(n), M: O(1), where n is the length of nums
    def singleNumber(self, nums: list[int]) -> int:
        curr = 0
        for num in nums:
            curr ^= num     # XOR
        return curr
    
    '''
    # Hash set solution
    # T: O(n), M: O(n), where n is the length of nums
    def singleNumber(self, nums: list[int]) -> int:
        single_num = set()
        for num in nums:
            if num in single_num:
                single_num.remove(num)
            else:
                single_num.add(num)
        return single_num.pop()
    '''
sol = Solution()
# Ex1
attempt = sol.singleNumber([2,2,1])
assert attempt == 1, f"Expected 1, got {attempt}"
# Ex2
attempt = sol.singleNumber([4,1,2,1,2])
assert attempt == 4, f"Expected 4, got {attempt}"
# Ex3
attempt = sol.singleNumber([1])
assert attempt == 1, f"Expected 1, got {attempt}"