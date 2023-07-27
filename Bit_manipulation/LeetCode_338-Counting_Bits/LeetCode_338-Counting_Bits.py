'''
LeeCode #338: Counting Bits prompt:
Easy

Given an integer n, return an array ans of length n + 1 such that for each i 
(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
0 <= n <= 105

Follow up:
- It is very easy to come up with a solution with a runtime of O(n log n). Can you 
    do it in linear time O(n) and possibly in a single pass?
- Can you do it without using any built-in function 
    (i.e., like __builtin_popcount in C++)?
'''

class Solution:
    # Optimized Bit Manipulation approach
    # T: O(n), M: O(n)
    def countBits(self, n: int) -> list[int]:
        cnt_bits = [0] * (n + 1)
        for idx in range(n + 1):
            cnt_bits[idx] = cnt_bits[idx >> 1] + (idx & 1)
        return cnt_bits
    
    '''
    # Optimized hammingWeight approach
    # T: O(n * k) or O(n * log n), M: O(n)
    def countBits(self, n: int) -> list[int]:
        return [self.hammingWeight(idx) for idx in range(n + 1)]

    # AND bit manipulation method
    # T: O(k), M: O(1), where k is num of 1s bits in binary representation of n
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= n - 1
            cnt += 1
        return cnt
    '''

    '''
    # Optimized Char count approach
    # T: O(n * i), M: O(n), where i is size index binary string representation
    def countBits(self, n: int) -> list[int]:
        return [bin(idx).count('1') for idx in range(n + 1)]
    '''

    '''    
    # Char count approach
    # T: O(n * i), M: O(n), where i is size index binary string representation
    def countBits(self, n: int) -> list[int]:
        cnt_bits = [0] * (n + 1)
        for idx in range(n + 1):
            cnt_bits[idx] = bin(idx).count('1')
        return cnt_bits
    '''

sol = Solution()
# Ex1
attempt = sol.countBits(2)
assert attempt == [0, 1, 1], f"Wrong Answer: {attempt}"
# Ex2
attempt = sol.countBits(5)
assert attempt == [0, 1, 1, 2, 1, 2], f"Wrong Answer: {attempt}"
# Test Case 3
attempt = sol.countBits(0)
assert attempt == [0], f"Wrong Answer: {attempt}"
# Test Case 4
attempt = sol.countBits(8)
assert attempt == [0, 1, 1, 2, 1, 2, 2, 3, 1], f"Wrong Answer: {attempt}"