# [LeetCode #700 - Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)

**Difficulty: `Easy`**

---

You are given the `root` of a binary search tree (BST) and an integer `val`.

Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

**Example 1:**  
![](tree1.jpg)  
Input:
```
root = [4,2,7,1,3]
val = 2
```
Output:
```
[2,1,3]
```

**Example 2:**  
![](tree2.jpg)  
Input:  
```
root = [4,2,7,1,3]
val = 5
```
Output:  
```
[]
```

---

**Constrains:**
- The number of nodes in the tree is in the range `[1, 5000]`.
- `1 <= Node.val <= 10^7`
- `root` is a binary search tree.
- `1 <= val <= 10^7`

**Follow up:**
- Can you implement the solution `iteratively` and `recursively`?

---
**Hints:**
- How do you perform a binary search on an array?
    - In a sorted asending order array the left most element is the smallest and the right most element is the largest. In a balanced Binary Search Tree the left most node is the smallest and the right most node is the largest.

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Binary_Search/LC_700-Search_in_a_Binary_Search_Tree)

### Approach: Iterative

### Intuition
To search for a value in a binary search tree, we can compare the value with the root node. If the value is less than the root node's value, we know that the value must be in the left subtree. Similarly, if the value is greater than the root node's value, we know that the value must be in the right subtree. If the value is equal to the root node's value, we have found the value we are looking for and we return the root node. If we reach a leaf node and haven't found the value, we return `null`.

With in an iterative approach it is quite simple to right as it is similar to a binary search on a sorted ascending order array. We just need to compare the value with the current node and move left or right 
accordingly.

### Steps:
1. While the root node is not `null` or out of bounds:
    - If the value is greater than the root node's value, we know that the value must be in the right subtree. So we move the root node to the right.
    - Else if the value is less than the root node's value, we know that the value must be in the left subtree. So we move the root node to the left.
    - Else the value is equal to the root node's value, we have found the value we are looking for and we return the root node.
2. If we reach a leaf node and haven't found the value, we return `null` as the value does not exist in the tree.

### Complexity Analysis
- **Time Complexity:** `O(log N)` or `O(H)`  
- **Space Complexity:** `O(1)`  

Where `N` is the number of nodes in the tree, and `H` is the height of a reasonably balanced tree.

## Python Code
```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if val > root.val:
                root = root.right   # increase curr node value
            elif val < root.val:
                root = root.left    # decrease curr node value
            else:                # Found value
                return root
        return None
```

## C++ Code
```cpp
class Solution {
public:
    TreeNode *searchBST(TreeNode *root, int val) {
        while (root) {
            if (root->val < val) 
                root = root->right;     // increase curr node value
            else if (root->val > val)
                root = root->left;      // decrease curr node value
            else                    // Found value
                return root;
        }
        return nullptr;
    }
};
```

## Java Code
```java
class Solution {
    TreeNode searchBST(TreeNode root, int val) {
        while (root != null) {
            if (root.val < val) 
                root = root.right;     // increase curr node value
            else if (root.val > val)
                root = root.left;      // decrease curr node value
            else                    // Found value
                return root;
        }
        return null;
    }
}
```

---

### Approach: Recursive

### Intuition
To search for a value in a binary search tree, we can compare the value with the root node. If the value is less than the root node's value, we know that the value must be in the left subtree. Similarly, if the value is greater than the root node's value, we know that the value must be in the right subtree. If the value is equal to the root node's value, we have found the value we are looking for and we return the root node. If we reach a leaf node and haven't found the value, we return `null`.

With in a recursive approach it is a bit more complex. As we need to recurisvely search the left and right subtrees. We can do this by calling the function again with the left or right subtree as the root node. We can also do this by returning the function call with the left or right subtree as the root node. This will allow for a stack like data structure to be created and the function calls will be popped off the stack as the function returns.

### Steps:
1. If the root node is `null` or out of bounds, return `null`.
2. Recursively search the left subtree if the value is less than the root node's value.
    - If the current node is greater than the value, we know that the value must be in the left subtree. So we call the function again with the left subtree as the root node.
    - Else if the current node is less than the value, we know that the value must be in the right subtree. So we call the function again with the right subtree as the root node.
3. Otherwise the value is equal to the root node's value, we have found the value we are looking for and we return the root node.

### Complexity Analysis
- **Time Complexity:** `O(log N)` or `O(H)`  
- **Space Complexity:** `O(log N)` or `O(H)`  

Where `N` is the number of nodes in the tree, and `H` is the height of a reasonably balanced tree.

## Python Code
```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Search for value
        if root.val > val:
            return self.searchBST(root.left, val)   # decrease curr val
        elif root.val < val:
            return self.searchBST(root.right, val)  # increase curr val

        return root # Found value
```

## C++ Code
```cpp
class Solution {
public:
    TreeNode *searchBST(TreeNode *root, int val) {
        if (!root)
            return nullptr;
        
        if (root->val < val) 
            return searchBST(root->right, val); // increase curr node value
        else if (root->val > val) 
            return searchBST(root->left, val);  // decrease curr node value
        
        return root;    // Found value
    }
};
```

## Java Code
```java
    class Solution {
        TreeNode searchBST(TreeNode root, int val) {
            if (root == null)
                return null;
            
            if (root.val < val) 
                return searchBST(root.right, val); // increase curr node value
            else if (root.val > val)
                return searchBST(root.left, val);  // decrease curr node value
            
            return root;    // Found value
        }
    }
```