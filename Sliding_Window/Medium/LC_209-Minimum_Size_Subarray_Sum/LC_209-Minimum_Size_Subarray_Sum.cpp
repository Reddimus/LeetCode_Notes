#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;

class Solution {
public:
    // Sliding window approach
    // T: O(n), M: O(1), where n is size of nums
    int minSubArrayLen(int target, vector<int>& nums) {
        int curr_sum = 0, min_size = INT_MAX;
        int l_idx = 0, r_idx = 0;
        while (r_idx < nums.size()) {
            curr_sum += nums[r_idx];
            while (curr_sum >= target) {
                min_size = min(min_size, (r_idx+1 - l_idx));
                // Shrink the window
                curr_sum -= nums[l_idx];
                l_idx++;
            }
            r_idx++;    // Slide window
        }
        return (min_size < INT_MAX) ? min_size : 0;
    }

    /*
    // Prefix sums + binary search approach
    // T: O(n log n), M: O(n), where n is the length of nums
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();

        // Calculate prefix sums
        vector<int> prefix_sums(n+1, 0);
        for (int idx = 1; idx <= n; idx++) {
            prefix_sums[idx] = prefix_sums[idx - 1] + nums[idx - 1];
        }

        // Iterate through the prefix sums and find the minimal length subarray
        int min_size = INT_MAX;
        for (int r_idx = n; r_idx >= 1; r_idx--) {
            if (prefix_sums[r_idx] < target)
                break;  // no subarray variation in range [1:r_idx+1] will sum up to target
            // int l_idx = upper_bound(prefix_sums.begin(), prefix_sums.end(), prefix_sums[r_idx] - target) - prefix_sums.begin();
            int l_idx = searchUpperBound(prefix_sums, prefix_sums[r_idx] - target);
            min_size = min(min_size, r_idx+1 - l_idx);
            prefix_sums.pop_back(); // reduce prefix_sums size to speed up the binary search for l_idx
        }
        return (min_size < INT_MAX) ? min_size : 0;
    }

    int searchUpperBound(vector<int>& arr, int target) {
        int l_idx = 0, r_idx = arr.size();
        while (l_idx < r_idx) {
            int m_idx = l_idx + (r_idx - l_idx) / 2;
            if (arr[m_idx] <= target)
                l_idx = m_idx + 1;
            else
                r_idx = m_idx;
        }
        return r_idx;
    }
    */
};


int main() {
    Solution sol;
    int attempt, target;
    vector<int> nums;
    // Ex1
    target = 7, nums = {2, 3, 1, 2, 4, 3};
    attempt = sol.minSubArrayLen(target, nums);
    assert(attempt == 2);
    // Ex2
    target = 4, nums = {1, 4, 4};
    attempt = sol.minSubArrayLen(target, nums);
    assert(attempt == 1);
    // Ex3
    target = 11, nums = {1, 1, 1, 1, 1, 1, 1, 1};
    attempt = sol.minSubArrayLen(target, nums);
    assert(attempt == 0);
    // Ex4
    target = 1, nums = {1};
    attempt = sol.minSubArrayLen(target, nums);
    assert(attempt == 1);
    // Ex5
    target = 9, nums = {1};
    attempt = sol.minSubArrayLen(target, nums);
    assert(attempt == 0);
    // Ex6
    target = 1, nums = {9};
    attempt = sol.minSubArrayLen(target, nums);
    assert(attempt == 1);
}