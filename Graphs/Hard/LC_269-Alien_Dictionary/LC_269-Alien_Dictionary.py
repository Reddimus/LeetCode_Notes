class Solution:
    def alienOrder(self, words: list[int]) -> str:
        return
    
# Example 1:
attempt = Solution().alienOrder(words=["wrt","wrf","er","ett","rftt"])
answer = "wertf"
assert attempt == answer, f"Expected {answer}, but got {attempt}"
# Example 2:
attempt = Solution().alienOrder(words=["z","x"])
answer = "zx"
assert attempt == answer, f"Expected {answer}, but got {attempt}"
# Example 3:
attempt = Solution().alienOrder(words=["z","x","z"])
answer = ""
assert attempt == answer, f"Expected {answer}, but got {attempt}"