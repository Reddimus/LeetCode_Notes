/*
Leetcode #1 - Two sum prompt:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums [0] + nums [1] == 9, we return [0, 1].

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Example 3:
Input: nums = [3, 3], target = 6
Output: [0, 1]

Constraints:
• 2 <= nums.length <= 10^4
• -10^9 <= nums [i] <= 10^9
• -10^9 <= target <= 10^9
• Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
*/

import java.util.*;

class Solution {
    // Difference/Hashmap method
    // T & M: O(n), where n is size of nums
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> prev_map = new HashMap<>();
        for(int idx = 0; idx < nums.length; idx++) {
            int diff = target - nums[idx];
            if(prev_map.containsKey(diff))
                return new int[]{prev_map.get(diff), idx};
            prev_map.put(nums[idx], idx);
        }
        return new int[]{};
    }

    // Brute force method
    // Time: O(n^2), Memory: O(1), where n is size of nums
    /*
    public int[] twoSum(int[] nums, int target) {
        for(int idx_0 = 0; idx_0 < nums.length - 1; idx_0++) {
            for(int idx_1 = idx_0 + 1; idx_1 < nums.length; idx_1++) {
                if((nums[idx_0] + nums[idx_1]) == target)
                    return new int[]{idx_0, idx_1};
            }
        } 
        return new int[]{};
    }
    */

    public static void main(String[] args) {
        // In terminal:
        // Compile:     "javac Solution.java"
        // Test cases:  "java -ea Solution"
        Solution sol = new Solution();
        int[] attempt;
        // Example 1
        attempt = sol.twoSum(new int[]{2, 7, 11, 15}, 9);
        assert Arrays.equals(attempt, new int[]{0, 1}) || Arrays.equals(attempt, new int[]{1, 0}) : "Expected [0, 1] or [1, 0], but got " + Arrays.toString(attempt);
        // Example 2
        attempt = sol.twoSum(new int[]{3, 2, 4}, 6);
        assert Arrays.equals(attempt, new int[]{1, 2}) || Arrays.equals(attempt, new int[]{2, 1}) : "Expected [1, 2] or [2, 1], but got " + Arrays.toString(attempt);
        // Example 3
        attempt = sol.twoSum(new int[]{3, 3}, 6);
        assert Arrays.equals(attempt, new int[]{0, 1}) || Arrays.equals(attempt, new int[]{1, 0}) : "Expected [0, 1] or [1, 0], but got " + Arrays.toString(attempt);
    }
}
