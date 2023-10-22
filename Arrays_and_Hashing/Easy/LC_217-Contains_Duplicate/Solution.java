/*
Leetcode #217 - Contains Duplicate prompt:

Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1, 2, 3, 1]
Output: true

Example 2:
Input: nums = [1, 2 ,3, 4]
Output: false

Example 3:
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
*/

import java.util.*;

class Solution{
    // Set approach
    // T & M: O(n), where n is size of nums
    public boolean containsDuplicate(int[] nums){
        Set<Integer> nums_set = new HashSet<>();
        for (int num : nums){
            if (nums_set.contains(num))
                return true;
            nums_set.add(num);
        }
        return false;
    }

    // Sorting approach
    // T: O(n log n), M: O(1), where n is size of nums
    // public boolean containsDuplicate(int[] nums){
    //     Arrays.sort(nums);
    //     for (int idx = 0; idx < nums.length; idx++){
    //         // if sorted neighbor is duplicate
    //         if (nums[idx] == nums[idx + 1])
    //             return true;
    //     }
    //     return false;
    // }

    // Brute force method; check every overlapping combination
    // T: O(n^2), M: O(1), where n is size of nums
    // public boolean containsDuplicate(int[] nums){
    //     for (int idx0 = 0; idx0 < nums.length - 1; idx0++){
    //         for (int idx1 = idx0 + 1; idx1 < nums.length; idx1++){
    //             if (nums[idx0] == nums[idx1])
    //                 return true;
    //         }
    //     }
    //     return false;
    // }

    public static void main(String[] args){
        // In terminal:
        // Compile:     "javac Solution.java"
        // Test cases:  "java -ea Solution"
        Solution sol = new Solution();
        boolean attempt;
        // Ex1
        attempt = sol.containsDuplicate(new int[]{1, 2, 3, 1});
        assert attempt == true : "Expected true but got " + attempt;
        // Ex 2
        attempt = sol.containsDuplicate(new int[]{1, 2 ,3, 4});
        assert attempt == false : "Expected false but got " + attempt;
        // Ex 3
        attempt = sol.containsDuplicate(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2});
        assert attempt == true : "Expected true but got " + attempt;
    }
}