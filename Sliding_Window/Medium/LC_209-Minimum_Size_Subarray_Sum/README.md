## Problem:
### 209. Minimum Size Subarray Sum
**Medium**  

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return 0 instead.

#### Example 1:
**Input:** target = 7, nums = [2,3,1,2,4,3]  
**Output:** 2  
**Explanation:** The subarray [4,3] has the minimal length under the problem constraint.

#### Example 2:
**Input:** target = 4, nums = [1,4,4]  
**Output:** 1

#### Example 3:
**Input:** target = 11, nums = [1,1,1,1,1,1,1,1]  
**Output:** 0

#### Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

#### Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

## Sliding Window Approach
### Time Complexity: O(n), Space Complexity: O(1)

The solution employs a sliding window approach where the window is represented as a subarray across the `nums` list using `l_idx` (left index) and `r_idx` (right index). The window's size is manipulated by moving the indexes, and the goal is to find the minimum window size with a sum greater than or equal to the target.

### Key Steps:
1. Initialize `l_idx` and `r_idx` to 0, `curr_sum` to 0, and `min_size` to infinity.
2. Slide the window by incrementing `r_idx` and update `curr_sum`.
3. If `curr_sum` >= `target`, update `min_size` and decrease the window size by incrementing `l_idx`.
4. Return `min_size` if it's not infinity; otherwise, return 0.

### Python3 Implementation:
``` Python
class Solution:
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
```

### C++ Implementation:
```C++
class Solution {
public:
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
};
```

### Java Implementation:
```Java
```

### Breakdown of Test Cases:
#### Example Test Case 1:

- **Input:** target = 7, nums = [2,3,1,2,4,3]
- **Output:** 2
- **Explanation:** The subarray [4,3] has the minimal length under the problem constraint.
    - Window: [2], l_idx = 0, r_idx = 0, curr_sum = 2, min_size = inf
    - Window: [2, 3], l_idx = 0, r_idx = 1, curr_sum = 5, min_size = inf
    - Window: [2, 3, 1], l_idx = 0, r_idx = 2, curr_sum = 6, min_size = inf
    - Window: [2, 3, 1, 2], l_idx = 0, r_idx = 3, curr_sum = 8, min_size = 4
    - Window: [3, 1, 2], l_idx = 1, r_idx = 3, curr_sum = 6, min_size = 4
    - Window: [3, 1, 2, 4], l_idx = 1, r_idx = 4, curr_sum = 10, min_size = 4
    - Window: [1, 2, 4], l_idx = 2, r_idx = 4, curr_sum = 7, min_size = 3
    - Window: [2, 4], l_idx = 3, r_idx = 4, curr_sum = 6, min_size = 3
    - Window: [2, 4, 3], l_idx = 3, r_idx = 5, curr_sum = 9, min_size = 3
    - `Window: [4, 3], l_idx = 4, r_idx = 5, curr_sum = 7, min_size = 2`
    - Window: [3], l_idx = 5, r_idx = 5, curr_sum = 3, min_size = 2

#### Example Test Case 2:
- **Input:** target = 4, nums = [1,4,4]
- **Output:** 1
- **Explanation:** The subarray [4] has the minimal length.
    - Window: [1], l_idx = 0, r_idx = 0, curr_sum = 1, min_size = inf
    - Window: [1, 4], l_idx = 0, r_idx = 1, curr_sum = 5, min_size = 4
    - `Window: [4], l_idx = 1, r_idx = 1, curr_sum = 4, min_size = 1`
    - Window: [], l_idx = 2, r_idx = 1, curr_sum = 0, min_size = 1
    - `Window: [4], l_idx = 2, r_idx = 2, curr_sum = 4, min_size = 1`
    - Window: [], l_idx = 3, r_idx = 2, curr_sum = 0, min_size = 1

#### Example Test Case 3:
- **Input:** target = 11, nums = [1,1,1,1,1,1,1,1]
- **Output:** 0
- **Explanation:** No subarray has a sum greater than or equal to 11.
    - Window: [1], l_idx = 0, r_idx = 0, curr_sum = 1, min_size = inf
    - Window: [1, 1], l_idx = 0, r_idx = 1, curr_sum = 2, min_size = inf
    - Window: [1, 1, 1], l_idx = 0, r_idx = 2, curr_sum = 3, min_size = inf
    - Window: [1, 1, 1, 1], l_idx = 0, r_idx = 3, curr_sum = 4, min_size = inf
    - Window: [1, 1, 1, 1, 1], l_idx = 0, r_idx = 4, curr_sum = 5, min_size = inf
    - Window: [1, 1, 1, 1, 1, 1], l_idx = 0, r_idx = 5, curr_sum = 6, min_size = inf
    - Window: [1, 1, 1, 1, 1, 1, 1], l_idx = 0, r_idx = 6, curr_sum = 7, min_size = inf
    - Window: [1, 1, 1, 1, 1, 1, 1, 1], l_idx = 0, r_idx = 7, curr_sum = 8, min_size = inf

#### Test Case 4:
- **Input:** target = 1, nums = [1]
- **Output:** 1
- **Explanation:** The subarray [1] has the minimal length.
    - `Window: [1], l_idx = 0, r_idx = 0, curr_sum = 1, min_size = 1`
    - Window: [], l_idx = 1, r_idx = 0, curr_sum = 0, min_size = 1

#### Test Case 5:
- **Input:** target = 9, nums = [1]
- **Output:** 0
- **Explanation:** No subarray has a sum greater than or equal to 9.
    - Window: [1], l_idx = 0, r_idx = 0, curr_sum = 1, min_size = inf

#### Test Case 6:
- **Input:** target = 1, nums = [9]
- **Output:** 1
- **Explanation:** The subarray [9] has the minimal length.
    - `Window: [9], l_idx = 0, r_idx = 0, curr_sum = 9, min_size = 1`
    - Window: [], l_idx = 1, r_idx = 0, curr_sum = 0, min_size = 1

## Prefix sums + binary search approach
### Time Complexity: O(n log n), Space Complexity: O(n)

The solution employs a prefix sums + binary search approach where the prefix sums are stored in a list `prefix_sums` and the subarray size is manipulated by searching for the left index of the subarray using binary search that best fits the target sum.

### Key Steps:
1. Initialize `prefix_sums` to a list of size `len(nums) + 1` and `min_size` to infinity.
2. Iterate through `nums` and store the prefix sums in `prefix_sums`.
3. Iterate through `prefix_sums` by decrementing and use binary search to find the left index of the subarray that best fits the target sum.
    - if prefix_sums[r_idx] < target sum, break out of the loop because no subbarray variation in range prefix_sums[1:r_idx+1] will fit the target sum.
    - pop the top element of prefix_sums to reduce the range of the binary search in the next iteration.
4. Return `min_size` if it's not infinity; otherwise, return 0.

### Python3 Implementation:
```Python
import bisect

class Solution:
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
            prefix_sums.pop()   # reduce size to speed up the binary search
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
```

### C++ Implementation:
```C++
class Solution {
public:
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
};
```

### Java Implementation:
```Java
```

### Breakdown of Test Cases:
#### Example Test Case 1:

- **Input:** target = 7, nums = [2,3,1,2,4,3]
- **Output:** 2
- **prefix_sums:** [0, 2, 5, 6, 8, 12, 15]
- **Explanation:** The subarray [4,3] has the minimal length under the problem constraint.
    - `prefix_sums[l_idx:r_idx+1] =  [12, 15], nums[l_idx-1:r_idx] =  [4, 3], min_size = 2`
    - prefix_sums[l_idx:r_idx+1] =  [6, 8, 12], nums[l_idx-1:r_idx] =  [1, 2, 4], min_size = 2
    - prefix_sums[l_idx:r_idx+1] =  [2, 5, 6, 8], nums[l_idx-1:r_idx] =  [2, 3, 1, 2], min_size = 2
    - break out of loop; prefix_sums = [2, 5, 6] < target sum

#### Example Test Case 2:
- **Input:** target = 4, nums = [1,4,4]
- **Output:** 1
- **prefix_sums:** [0, 1, 5, 9]
- **Explanation:** The subarray [4] has the minimal length.
    - `prefix_sums[l_idx:r_idx+1] =  [9], nums[l_idx-1:r_idx] =  [4], min_size = 1`
    - `prefix_sums[l_idx:r_idx+1] =  [5], nums[l_idx-1:r_idx] =  [4], min_size = 1`
    - break out of loop; prefix_sums = [1] < target sum

#### Example Test Case 3:
- **Input:** target = 11, nums = [1,1,1,1,1,1,1,1]
- **Output:** 0
- **prefix_sums:** [0, 1, 2, 3, 4, 5, 6, 7, 8]
- **Explanation:** No subarray has a sum greater than or equal to 11.
    - break out of loop; prefix_sums = [1, 2, 3, 4, 5, 6, 7, 8] < target sum


#### Test Case 4:
- **Input:** target = 1, nums = [1]
- **Output:** 1
- **prefix_sums:** [0, 1]
- **Explanation:** The subarray [1] has the minimal length.
    - `prefix_sums[l_idx:r_idx+1] =  [1], nums[l_idx-1:r_idx] =  [1], min_size = 1`

#### Test Case 5:
- **Input:** target = 9, nums = [1]
- **Output:** 0
- **prefix_sums:** [0, 1]
- **Explanation:** No subarray has a sum greater than or equal to 9.
    - break out of loop; prefix_sums = [1] < target sum

#### Test Case 6:
- **Input:** target = 1, nums = [9]
- **Output:** 1
- **prefix_sums:** [0, 9]
- **Explanation:** The subarray [9] has the minimal length.
    - `prefix_sums[l_idx:r_idx+1] =  [9], nums[l_idx-1:r_idx] =  [9], min_size = 1`
