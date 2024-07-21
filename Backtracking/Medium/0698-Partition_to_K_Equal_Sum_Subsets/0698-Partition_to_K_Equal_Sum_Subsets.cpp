class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        const unsigned int numsSum = accumulate(nums.begin(), nums.end(), 0);
        const int8_t n = nums.size();
        if (numsSum % k > 0 || n < k) 
            return false;

        sort(nums.rbegin(), nums.rend());
        const int target = numsSum / k;
        bitset<16> visited;

        function<bool(int8_t, int, int)> backtrack = [&](int8_t i, int count, int currSum) -> bool {
            if (count == k) 
                return true;
            if (currSum == target) 
                return backtrack(0, count + 1, 0);

            for (int8_t idx = i; idx < n; ++idx) {
                // Skip duplicates if last same number was skipped
                if (visited[idx] || currSum + nums[idx] > target || 
                (idx > 0 && !visited[idx - 1] && nums[idx] == nums[idx - 1])) 
                    continue;

                visited[idx] = 1;

                if (backtrack(idx + 1, count, currSum + nums[idx])) 
                    return true;
                
                visited[idx] = 0;
            }
            return false;
        };

        return backtrack(0, 0, 0);
    }
};