# LeetCode #70 - Climbing Stairs

https://leetcode.com/problems/climbing-stairs/description/

`Easy`

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

## Example 1
**Input**: 
```
n = 2
```  
**Output**: 
```
2
```
**Explanation**: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

## Example 2
**Input**: 
```
n = 3
```  
**Output**: 
```
3
```  
**Explanation**: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

## Constraints
- `1 <= n <= 45`

## Hints
- Check test case 1->5 to see if you can find a pattern.

## Solution Explanation

https://github.com/Reddimus/LeetCode_Notes/tree/main/1-D_Dynamic_Programming/Easy/LC_70-Climbing_Stairs

### Approach: 1-D Dynamic Programming
#### Intuition
Start with the test cases given, then check more test cases to see if there is a pattern. You may want to brute force the problem by hand to see if you can find a pattern. There is a pattern seen from stairs 1->5. The number of ways to climb the stairs is the sum of the number of ways to climb the previous 2 stairs. This is a classic dynamic programming problem very similar to the Fibonacci sequence.

#### Algorithm
1. If `n` is less than or equal to 3, return `n` because the number of ways to climb the stairs is the same as the number of stairs.
2. Start from the 4th stair and use a bottom up approach to calculate the number of ways to climb the stairs.
3. Use 2 variables to keep track of the number of ways to climb the previous 2 stairs.
4. For each stair, calculate the number of ways to climb the current stair by adding the number of ways to climb the previous 2 stairs.
5. Shift the window right by updating the last 2 variables.
6. Return the number of ways to climb the last stair.

#### Complexity Analysis
- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
    - We only need 2 variables to keep track of the number of ways to climb the previous 2 stairs.
Where `n` is the number of stairs.

### Python Solution
```python
class Solution:
	def climbStairs(self, n: int) -> int:
		if n <= 3:
			return n
        
		# bottom up approach; start from 4th stair
		n1, n2 = 2, 3
		for i in range(4, n + 1):
            # shift window right/ update last 2 variables
			n1, n2 = n2, n1 + n2
		return n2
```

### C++ Solution
```cpp
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 3)
            return n;
        
        // Bottom up approach; start from 4th stair
        int n1 = 2, n2 = 3;
        for (int stairs = 4; stairs <= n; stairs++) {
            // Shift window right/ update last 2 variables
            int temp = n1 + n2;
            n1 = n2;
            n2 = temp;
        }
        return n2;
    }
};
```

### Java Solution
```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 3)
            return n;
        
        // Bottom up approach; start from 4th stair
        int n1 = 2, n2 = 3;
        for (int stairs = 4; stairs <= n; stairs++) {
            // Shift window right/ update last 2 variables
            int temp = n1 + n2;
            n1 = n2;
            n2 = temp;
        }
        return n2;
    }
}
```