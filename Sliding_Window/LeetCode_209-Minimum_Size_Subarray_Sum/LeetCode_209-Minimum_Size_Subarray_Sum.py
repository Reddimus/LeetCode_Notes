import bisect

class Solution:
    # Sliding window approach
    # T: O(n), M: O(1), where n is the length of nums
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_size = float('inf')
        l_idx, curr_sum = 0, 0
        for r_idx in range(len(nums)):
            curr_sum += nums[r_idx]
            while curr_sum >= target:
                min_size = min(min_size, r_idx+1 - l_idx)
                # shrink the window
                curr_sum -= nums[l_idx]
                l_idx += 1
        return 0 if min_size == float('inf') else min_size
    
    '''    
    # Prefix sums + binary search approach
    # T: O(n log n), M: O(n), where n is the length of nums
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Calculate prefix sums
        n = len(nums)
        prefix_sums = [0] * (n + 1)
        for idx in range(1, n + 1):
            prefix_sums[idx] = prefix_sums[idx - 1] + nums[idx - 1]
                
        # Iterate through the prefix sums and find the minimal length subarray
        min_size = float('inf')
        for r_idx in range(n, 0, -1):
            if prefix_sums[r_idx] < target:
                # no subarray variation in range [1:r_idx+1] will sum up to target
                break
            # l_idx = bisect.bisect_right(prefix_sums, prefix_sums[r_idx] - target)
            l_idx = self.search_upper_bound(prefix_sums, prefix_sums[r_idx] - target)
            min_size = min(min_size, r_idx+1 - l_idx)
            prefix_sums.pop()   # reduce the size of the prefix sums array to speed up the binary search
        return 0 if min_size == float('inf') else min_size
    
    def search_upper_bound(self, arr: list[int], target: int) -> int:
        l_idx, r_idx = 0, len(arr)
        while l_idx < r_idx:
            m_idx = (l_idx + r_idx) // 2
            if arr[m_idx] <= target:
                l_idx = m_idx + 1
            else:
                r_idx = m_idx
        return r_idx
    '''

sol = Solution()
# Ex 1
attempt = sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])
assert attempt == 2, f'Expected 2 but got {attempt}'
# Ex 2
attempt = sol.minSubArrayLen(target = 4, nums = [1,4,4])
assert attempt == 1, f'Expected 1 but got {attempt}'
# Ex 3
attempt = sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])
assert attempt == 0, f'Expected 0 but got {attempt}'
# Test case 4
attempt = sol.minSubArrayLen(target = 1, nums = [1])
assert attempt == 1, f'Expected 1 but got {attempt}'
# Test case 5
attempt = sol.minSubArrayLen(target = 9, nums = [1])
assert attempt == 0, f'Expected 0 but got {attempt}'
# Test case 6
attempt = sol.minSubArrayLen(target = 1, nums = [9])
assert attempt == 1, f'Expected 1 but got {attempt}'