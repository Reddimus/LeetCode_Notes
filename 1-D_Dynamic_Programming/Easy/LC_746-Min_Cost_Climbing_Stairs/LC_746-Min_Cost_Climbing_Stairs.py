class Solution:
    # T: O(n), M: O(1), where n is amount of steps
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Bottom-up approach; start from 3rd step
        for idx in range(2, len(cost)):
            cost[idx] += min(cost[idx-1], cost[idx-2])
        return min(cost[len(cost)-1], cost[len(cost)-2])

    '''
    # T: O(n), M: O(1), where n is amount of steps
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Top-down approach; start from 3rd to last step
        for idx in range(len(cost)-3, -1, -1):
            cost[idx] += min(cost[idx+1], cost[idx+2])
        return min(cost[0], cost[1])
    '''

sol = Solution()

# Ex1
attempt = sol.minCostClimbingStairs([10, 15, 20])
assert attempt == 15, f"Expected 15, got {attempt}"
# Ex2
attempt = sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
assert attempt == 6, f"Expected 6, got {attempt}"
