
# LeetCode Problem #112 - Path Sum

https://leetcode.com/problems/path-sum/description/

`Easy`

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the numbers along the path equals `targetSum`.

### Example 1:

![Example 1 Tree](https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg)

Input: 
```
root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
targetSum = 22
```  
Output: 
```
true
```

### Example 2:

![Example 2 Tree](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

Input: 
```
root = [1,2,3]
targetSum = 5
```  
Output: 
```
false
```

### Example 3:

Input: 
```
root = [] 
targetSum = 0
```  
Output: 
```
false
```

## Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`
