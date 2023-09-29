class Solution:
    # Dynamic programming w/ 2 variables approach
    # T: O(n), M: O(1)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        # Start from 2
        n0, n1 = 0, 1
        for num in range(2, n+1):
            n0, n1 = n1, n0 + n1
        return n1
    
    '''
    # Dynamic programming w/ array approach
    # T: O(n), M: O(n)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        # Start from 2
        dp = [0, 1]
        for num in range(2, n+1):
            dp.append(dp[-2] + dp[-1])
        return dp[-1]
    '''

sol = Solution()

# Ex1
attempt = sol.fib(2)
assert attempt == 1, "Expected 1, but got: " + attempt
# Ex2
attempt = sol.fib(3)
assert attempt == 2, "Expected 2, but got: " + attempt
# Ex3
attempt = sol.fib(4)
assert attempt == 3, "Expected 3, but got: " + attempt
