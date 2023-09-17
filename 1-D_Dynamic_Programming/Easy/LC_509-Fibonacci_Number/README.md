
# LeetCode #509 - Fibonacci Number

https://leetcode.com/problems/fibonacci-number/description/

`Easy`

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1  
F(n) = F(n - 1) + F(n - 2), for n > 1.  

Given `n`, calculate `F(n)`.

## Example 1
**Input**: 
```
n = 2
```  
**Output**: 
```
1
```
**Explanation**: F(2) = F(1) + F(0) = 1 + 0 = 1.

## Example 2
**Input**: 
```
n = 3
```  
**Output**: 
```
2
```
**Explanation**: F(3) = F(2) + F(1) = 1 + 1 = 2.

## Example 3
**Input**: 
```
n = 4
```  
**Output**: 
```
3
```
**Explanation**: F(4) = F(3) + F(2) = 2 + 1 = 3.

## Constraints
- `0 <= n <= 30`

## Hints
- Use 2 variables to keep track of the previous 2 Fibonacci numbers.

## Solution Explanation

https://github.com/Reddimus/LeetCode_Notes/tree/main/1-D_Dynamic_Programming/Easy/LC_509-Fibonacci_Number

### Approach: 1-D Dynamic Programming
#### Intuition
For the most part the algorithm is given we look at the last 2 Fibonacci numbers and add them together to get the next Fibonacci number. We can use a bottom up approach to calculate the Fibonacci numbers.

#### Algorithm
1. If `n` is less than or equal to 1, return `n` because the Fibonacci number is the same as `n`.
2. Start from the 2nd Fibonacci number and use a bottom up approach to calculate the Fibonacci numbers.
3. Use 2 variables to keep track of the last 2 Fibonacci numbers.
4. For each Fibonacci number, calculate the next Fibonacci number by adding the last 2 Fibonacci numbers.
5. Shift the window right by updating the last 2 variables.
6. Return the last Fibonacci number.

#### Complexity Analysis
- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
    - We only need 2 variables to keep track of the last 2 Fibonacci numbers.
Where `n` is the number of Fibonacci numbers.

## Python Code
```python
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        # Start from 2
        n0, n1 = 0, 1
        for num in range(2, n+1):
            n0, n1 = n1, n0 + n1
        return n1
```

## C++ Code
```cpp
class Solution {
public:
    int fib(int n) {
        if (n <= 1)
            return n;
        
        // Start from 2
        int n0 = 0, n1 = 1;
        for (int num = 2; num <= n; num++) {
            int temp = n0 + n1;
            n0 = n1, n1 = temp;
        }
        return n1;
    }
};
```

## Java Code
```java
class Solution {
    public int fib(int n) {
        if (n <= 1)
            return n;
        
        // start from 2
        int n0 = 0, n1 = 1;
        for (int num = 2; num <= n; num++) {
            int temp = n0 + n1;
            n0 = n1;
            n1 = temp;
        }
        return n1;
    }
}
```
