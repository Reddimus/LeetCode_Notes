'''
LeetCode #303 - Range Sum Query-Immutable prompt:

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right 
inclusive where left <= right.

Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between 
indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3


Constraints:
1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.
'''

class NumArray:
    # prepare Prefix sum array
    # T: O(n), M: O(n), where n is size of nums
    def __init__(self, nums: list[int]):
        self.prefix_nums = []
        curr_total = 0
        for num in nums:
            curr_total += num
            self.prefix_nums.append(curr_total)

    # T: O(1)
    def sumRange(self, left: int, right: int) -> int:
        if left <= 0:   # Edge case
            return self.prefix_nums[right]
        return self.prefix_nums[right] - self.prefix_nums[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Ex1
nums = NumArray([-2, 0, 3, -5, 2, -1])
attempt = nums.sumRange(0, 2)
assert attempt == 1, f'Expected 1 but got {attempt}'
attempt = nums.sumRange(2, 5)
assert attempt == -1, f'Expected -1 but got {attempt}'
attempt = nums.sumRange(0, 5)
assert attempt == -3, f'Expected -3 but got {attempt}'
