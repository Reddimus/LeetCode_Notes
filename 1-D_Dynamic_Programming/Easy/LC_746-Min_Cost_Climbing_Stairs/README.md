
# LeetCode #746 - Min Cost Climbing Stairs

https://leetcode.com/problems/min-cost-climbing-stairs/

`Easy`

You are given an integer array `cost` where `cost[i]` is the cost of `ith` step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `0`, or the step with index `1`.

Return the *minimum* cost to reach the top of the floor.

### Example 1
**Input**: 
```
cost = [10,15,20]
```
**Output**: 
```
15
```
**Explanation**: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

### Example 2
**Input**: 
```
cost = [1,100,1,1,1,100,1,1,100,1]
```
**Output**: 
```
6
```
**Explanation**: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

### Constraints

- `2 <= cost.length <= 1000`
- `0 <= cost[i] <= 999`

## Hints
- Start from 3rd or 3rd to last step.

## Solution Explanation

https://github.com/Reddimus/LeetCode_Notes/tree/main/1-D_Dynamic_Programming/Easy/LC_746-Min_Cost_Climbing_Stairs

### Approach: 1-D Dynamic Programming - Bottom-up & Top-down

#### Intuition
Constantly compare the cost of the previous step and the step before the previous step. Keep track of the minimum cost by adding the minimum cost of the previous step to the current step.

#### Complexity Analysis
- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

Where `n` is the amount of steps.


## Python Code
```python
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Bottom-up approach; start from 3rd step
        for idx in range(2, len(cost)):
            cost[idx] += min(cost[idx-1], cost[idx-2])
        return min(cost[len(cost)-1], cost[len(cost)-2])

    '''
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Top-down approach; start from 3rd to last step
        for idx in range(len(cost)-3, -1, -1):
            cost[idx] += min(cost[idx+1], cost[idx+2])
        return min(cost[0], cost[1])
    '''
```

## C++ Code
```cpp
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        // Bottom-up approach; start from 3rd step
        for (int i = 2; i < cost.size(); ++i) {
            cost[i] += min(cost[i - 1], cost[i - 2]);
        }
        return min(cost[cost.size() - 1], cost[cost.size() - 2]);
    }

    /*
    int minCostClimbingStairs(vector<int>& cost) {
        // Top-down approach; start from 3rd to last step
        for (int i = cost.size() - 3; i >= 0; --i) {
            cost[i] += min(cost[i + 1], cost[i + 2]);
        }
        return min(cost[0], cost[1]);
    }
    */
};
```

## Java Code
```java
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        // Bottom-up approach; start from 3rd step
        for (int i = 2; i < cost.length; i++) {
            cost[i] += Math.min(cost[i - 1], cost[i - 2]);
        }
        return Math.min(cost[cost.length - 1], cost[cost.length - 2]);
    }
    
    /*
    public int minCostClimbingStairs(int[] cost) {
        // Top-down approach; start from 3rd to last step
        for (int i = cost.length - 3; i >= 0; i--) {
            cost[i] += Math.min(cost[i + 1], cost[i + 2]);
        }
        return Math.min(cost[0], cost[1]);
    }
    */
}
```
