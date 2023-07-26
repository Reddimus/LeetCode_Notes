'''
LeetCode #191 - Number of 1 Bits prompt:

Write a function that takes the binary representation of an unsigned integer and returns the number of 
'1' bits it has (also known as the Hamming weight).

Note:
- Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input 
    will be given as a signed integer type. It should not affect your implementation, as the integer's 
    internal binary representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in 
    Example 3, the input represents the signed integer. -3.

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Constraints:

The input must be a binary string of length 32.

Follow up: If this function is called many times, how would you optimize it?
'''

class Solution:
    # AND Bit manipulation solution
    # T: O(k), M: O(1), where k is the number of 1 bits in n
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= n - 1
            cnt += 1
        return cnt

    '''
    # Char count solution
    # T: O(n), M: O(1)
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
    '''

    '''
    # Char count solution
    # T: O(n), M: O(1)
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for bit in bin(n)[2:]:
            if bit == '1':
                cnt += 1
        return cnt
    '''

sol = Solution()
# Ex1
attempt = sol.hammingWeight(11)
assert attempt == 3, f"Expected 3, got {attempt}"
# Ex2
attempt = sol.hammingWeight(128)
assert attempt == 1, f"Expected 1, got {attempt}"
# Ex3
attempt = sol.hammingWeight(4294967293)
assert attempt == 31, f"Expected 31, got {attempt}"
