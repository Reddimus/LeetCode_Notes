/*
Leetcode #238 - Product of Array Except Self Prompt:
Easy

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
*/

import java.util.*;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] pes_nums = new int[nums.length];
        Arrays.fill(pes_nums, 1);

        // Fill pes_nums with prefix products
        int prefix = 1;
        for (int idx = 0; idx < nums.length; idx++) {
            // starts with a static 1 and ends with 2nd to last prefix product
            pes_nums[idx] = prefix;
            prefix *= nums[idx];
        }

        // Fill pes_nums with postfix products ontop of prefix products
        int postfix = 1;
        for (int idx = nums.length - 1; idx > -1; idx--) {
            // starts from right to left with same element and ends with 2nd to last postfix product
            pes_nums[idx] *= postfix;
            postfix *= nums[idx];
        }

        return pes_nums;
    }
}

class TestCases {
    public static void main(String[] args) {
        // In terminal:
        // Compile:     "javac Solution.java"
        // Test cases:  "java -ea TestCases"
        Solution sol = new Solution();
        int[] attempt;
        // Ex 1
        attempt = sol.productExceptSelf(new int[]{1, 2, 3, 4});
        assert Arrays.equals(attempt, new int[]{24, 12, 8, 6}) : "Expected [24, 12, 8, 6], got " + Arrays.toString(attempt);
        // Ex 2
        attempt = sol.productExceptSelf(new int[]{-1, 1, 0, -3, 3});
        assert Arrays.equals(attempt, new int[]{0, 0, 9, 0, 0}) : "Expected [0, 0, 9, 0, 0], got " + Arrays.toString(attempt);
        // Test case 3
        attempt = sol.productExceptSelf(new int[]{1, 2});
        assert Arrays.equals(attempt, new int[]{2, 1}) : "Expected [2, 1], got " + Arrays.toString(attempt);
    }
}