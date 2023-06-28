/*
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
*/

class NumArray {
    // Prepare Prefix sum array
    // T: O(n), M: O(n), where n is size of nums
    private int[] prefix_nums;
    public NumArray(int[] nums) {
        this.prefix_nums = new int[nums.length];
        int curr_total = 0;
        for (int idx = 0; idx < nums.length; idx++){
            curr_total += nums[idx];
            this.prefix_nums[idx] = curr_total;
        }
    }
    // T: O(1)
    public int sumRange(int left, int right) {
        if (left <= 0)
            return this.prefix_nums[right];
        return this.prefix_nums[right] - this.prefix_nums[left - 1];
    }


    public static void main(String[] args) {
        // In terminal:
        // Compile:     "javac NumArray.java"
        // Test cases:  "java -ea NumArray"
        // Ex1
        NumArray nums = new NumArray(new int[]{-2, 0, 3, -5, 2, -1});
        int attempt = nums.sumRange(0, 2);
        assert attempt == 1 : String.format("Expected 1 but got %s", attempt);
        attempt = nums.sumRange(2, 5);
        assert attempt == -1 : String.format("Expected -1 but got %s", attempt);
        attempt = nums.sumRange(0, 5);
        assert attempt == -3 : String.format("Expected -3 but got %s", attempt);
    }
}