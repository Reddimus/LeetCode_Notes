import java.util.*;

class Solution {
    // Sliding window approach
    // T: O(n), M: O(1), where n is size of nums
    public int minSubArrayLen(int target, int[] nums) {
        int curr_sum = 0, min_size = Integer.MAX_VALUE;
        int l_idx = 0, r_idx = 0;
        while (r_idx < nums.length) {
            curr_sum += nums[r_idx];
            while (curr_sum >= target) {
                min_size = Math.min(min_size, r_idx+1 - l_idx);
                // Shrink the window
                curr_sum -= nums[l_idx];
                l_idx++;
            }
            r_idx++;    // Slide window
        }
        return min_size < Integer.MAX_VALUE ? min_size : 0;
    }

    /*
    // Prefix sums + binary search approach
    // T: O(n log n), M: O(n), where n is the length of nums
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;

        // Calculate prefix sums
        List<Integer> prefix_sums = new ArrayList<>();
        prefix_sums.add(nums[0]);
        for (int idx = 1; idx < n; idx++)
            prefix_sums.add(prefix_sums.get(idx - 1) + nums[idx]);
        
        // Iterate through the prefix sums and find the minimal length subarray
        int min_size = Integer.MAX_VALUE;
        for (int r_idx = n - 1; r_idx >= 0; r_idx--) {
            if (prefix_sums.get(r_idx) < target)
                break;  // no subarray variation in range [0:r_idx+1] will sum to target
            int l_idx = searchUpperBound(prefix_sums, prefix_sums.get(r_idx) - target);
            min_size = Math.min(min_size, r_idx+1 - l_idx);
            // reduce prefix_sums size to speed up the binary search for l_idx
            prefix_sums.remove(prefix_sums.size() - 1);
        }
        return min_size < Integer.MAX_VALUE ? min_size : 0;
    }

    public static int searchUpperBound(List<Integer> arr, int target) {
        int l_idx = 0, r_idx = arr.size();
        while (l_idx < r_idx) {
            int m_idx = l_idx + (r_idx - l_idx) / 2;
            if (arr.get(m_idx) <= target)
                l_idx = m_idx + 1;
            else
                r_idx = m_idx;
        }
        return r_idx;
    }
    */
}

class TestCases {
    public static void main(String[] args) {
        // In terminal:
        // Compile:     "javac MinSizeSubArr.java"
        // Test cases:  "java -ea TestCases"
        Solution sol = new Solution();
        int attempt;
        // Ex 1
        attempt = sol.minSubArrayLen(7, new int[]{2,3,1,2,4,3});
        assert attempt == 2 : "Expected 2, but got " + attempt;
        // Ex 2
        attempt = sol.minSubArrayLen(4, new int[]{1,4,4});
        assert attempt == 1 : "Expected 1, but got " + attempt;
        // Ex 3
        attempt = sol.minSubArrayLen(11, new int[]{1,1,1,1,1,1,1,1});
        assert attempt == 0 : "Expected 0, but got " + attempt;
        // Test case 4
        attempt = sol.minSubArrayLen(1, new int[]{1});
        assert attempt == 1 : "Expected 1, but got " + attempt;
        // Test case 5
        attempt = sol.minSubArrayLen(9, new int[]{1});
        assert attempt == 0 : "Expected 0, but got " + attempt;
        // Test case 6
        attempt = sol.minSubArrayLen(1, new int[]{9});
        assert attempt == 1 : "Expected 1, but got " + attempt;
    }
}