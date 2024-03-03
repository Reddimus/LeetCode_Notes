import heapq

# Heap/Priority Queue approach
# T: O(n log n), M: O(1)
# Where n is the length of stones list

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Create stones max heap
        stones = [-weight for weight in stones]
        heapq.heapify(stones)
        # Smash stones until there is 1 stone left
        while len(stones) > 1:
            heaviest1, heaviest2 = heapq.heappop(stones), heapq.heappop(stones)
            heapq.heappush(stones, heaviest1 - heaviest2)
        return -stones[0]

# Ex1:
attempt = Solution().lastStoneWeight(stones = [2,7,4,1,8,1])
assert attempt == 1, f'Expected 1, but got {attempt}'
# Ex2:
attempt = Solution().lastStoneWeight(stones = [1])
assert attempt == 1, f'Expected 1, but got {attempt}'
# Test case 3:
attempt = Solution().lastStoneWeight(stones = [1, 1])
assert attempt == 0, f'Expected 0, but got {attempt}'
