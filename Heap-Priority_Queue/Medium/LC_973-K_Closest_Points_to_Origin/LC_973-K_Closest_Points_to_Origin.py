from math import sqrt
import heapq

# Heap/Priority Queue approach
# T: O(k log n), M: O(n)

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # Build a heap of partially solved distances & indices of points
        distances = [(x * x + y * y, i) for i, (x, y) in enumerate(points)]
        heapq.heapify(distances)
        # Build the k closest points answer based off heap sorted distances
        return [points[i] for d, i in heapq.nsmallest(k, distances)]

'''
# Sorting approach
# T: O(n log n), M: O(n)
    
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # Build a list of partially solved distances & indices of points
        distances = [(x * x + y * y, i) for i, (x, y) in enumerate(points)]
        distances.sort(key=lambda e : e[0])
        # Build the k closest points answer based off sorted distances
        return [points[i] for d, i in distances[:k]]
'''

def assertKClosest(attempt: list[list[int]], answer: list[list[int]]):
    attempt.sort()
    answer.sort()
    assert attempt == answer, f"Expected {answer}, but got {attempt}"

# Example 1:
attempt = Solution().kClosest(points = [[1,3],[-2,2]], k = 1)
assertKClosest(attempt, answer=[[-2,2]])
# Example 2:
attempt = Solution().kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2)
assertKClosest(attempt, answer=[[3,3],[-2,4]])
# Test Case 3:
attempt = Solution().kClosest(points=[[9997,9997],[9996,9998]], k = 1)
assertKClosest(attempt, answer=[[9997,9997]])