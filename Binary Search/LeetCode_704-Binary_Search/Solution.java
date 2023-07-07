/*
LeetCode #704 - Binary Search prompt:

Given an array of integers nums which is sorted in ascending order, and an 
integer target, write a function to search target in nums. If target 
exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:
1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.
*/

class Solution {
    // Binary search
    // T: O(log n), M: O(1), where n is size of nums
    public int search(int[] nums, int target) {
        int l_idx = 0, r_idx = nums.length - 1;
        while (l_idx <= r_idx){
            // mid = left + half sub dist
            int m_idx = l_idx + ((r_idx - l_idx) / 2);
            // if number not within +-mid range throw away subarray range
            if (nums[m_idx] < target)
                l_idx = m_idx + 1;
            else if (nums[m_idx] > target)
                r_idx = m_idx - 1;
            // else mid element = target
            else
                return m_idx;
        }
        return -1;
    }

    public static void main(String[] args){
        // In terminal:
        // Compile:         "javac Solution.java"
        // Run test cases:  "java -ea Solution"
        Solution sol = new Solution();
        // Ex 1:
        int attempt = sol.search(new int[]{-1, 0, 3, 5, 9, 12}, 9);
        assert attempt == 4 : "Expected 4 but got " + attempt;
        // Ex 2:
        attempt = sol.search(new int[]{-1, 0, 3, 5, 9, 12}, 2);
        assert attempt == -1 : "Expected -1 but got " + attempt;
        // Test case 3:
        attempt = sol.search(new int[]{9}, 9);
        assert attempt == 0 : "Expected 0 but got " + attempt;
        // Test case 4:
        attempt = sol.search(new int[]{9}, 10);
        assert attempt == -1 : "Expected -1 but got " + attempt;
        // Test case 5:
        attempt = sol.search(new int[]{2, 5, 7, 9, 11, 11, 11}, 9);
        assert attempt == 3 : "Expected 3 but got " + attempt;
        // Test case 6:
        attempt = sol.search(new int[]{2, 5, 7, 9, 11, 11, 11}, 11);
        assert attempt == 4 || attempt == 5 || attempt == 6 : "Expected 4, 5, or 6 but got " + attempt;
        // Test case 7:
        attempt = sol.search(new int[]{2, 5, 7, 9, 11, 11, 11}, 12);
        assert attempt == -1 : "Expected -1 but got " + attempt;
    }
}
