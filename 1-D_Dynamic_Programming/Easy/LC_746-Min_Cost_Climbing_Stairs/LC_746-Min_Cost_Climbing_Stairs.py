class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for idx in range(len(cost) - 3, -1, -1):
            

sol = Solution()

# Ex1
attempt = sol.minCostClimbingStairs([10, 15, 20])
assert attempt == 15, f"Expected 15, got {attempt}"
# Ex2
attempt = sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
assert attempt == 6, f"Expected 6, got {attempt}"
