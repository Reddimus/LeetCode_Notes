# [LeetCode #701 - Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

**Difficulty: `Medium`**

---

You are given the `root` node of a binary search tree (BST) and a `value` to insert into the tree. Return the *root node of the BST after the insertion*. It is **guaranteed** that the new value does not exist in the original BST.

**Notice** that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return **any of them**.

### Example 1

![Example 1 Image](https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg)

Input: 
```
root = [4,2,7,1,3]
val = 5
```
Output: 
```
[4,2,7,1,3,5]
```

**Explanation:** Another acceptable tree is:

![Example 2 Image](https://assets.leetcode.com/uploads/2020/10/05/bst.jpg)

### Example 2

Input: 
```
root = [40,20,60,10,30,50,70]
val = 25
```
Output: 
```
[40,20,60,10,30,50,70,null,null,25]
```

### Example 3

Input: 
```
root = [4,2,7,1,3,null,null,null,null,null,null]
val = 5
```
Output: 
```
[4,2,7,1,3,5]
```


## Constraints

- The number of nodes in the tree will be in the range `[0, 10^4]`.
- `-10^8 <= Node.val <= 10^8`
- All the values `Node.val` are unique.
- `-10^8 <= val <= 10^8`
- It's guaranteed that `val` does not exist in the original BST.

# [Solution](https://github.com/Reddimus/LeetCode_Notes/blob/main/Trees/Easy/LC_701-Insert_into_a_Binary_Search_Tree)

### Approach: Iterative

### Intuition


### Steps
1. 

### Complexity Analysis
- **Time Complexity:** `O(log N)` or `O(h)`  
- **Space Complexity:** `O(1)`  

Where `N` is the number of nodes in the tree, and `h` is the height of a reasonably balanced tree.

### Python Code:
```python
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)

        # Binary Search for insert null position
        curr, prev = root, root
        while curr:
            prev = curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        
        # Connect previous node to the new position
        if prev.val > val:
            prev.left = TreeNode(val=val)
        else:
            prev.right = TreeNode(val=val)

        return root
```

### C++ Code:
```cpp
```

### Java Code:
```java
```

### Approach: Recursive

### Intuition


### Steps
1. 

### Complexity Analysis
- **Time Complexity:** `O(log N)` or `O(h)`  
- **Space Complexity:** `O(log N)` or `O(h)`  

Where `N` is the number of nodes in the tree, and `h` is the height of a reasonably balanced tree.

### Python Code:
```python
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)
        
        # Recursively search for null position, then connect previous node to new node
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)      # decrease current node
        else:
            root.right = self.insertIntoBST(root.right, val)    # increase current node

        return root
```

### C++ Code:
```cpp
```

### Java Code:
```java
```