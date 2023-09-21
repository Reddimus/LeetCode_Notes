# LeetCode 700 - Search in a Binary Search Tree

https://leetcode.com/problems/search-in-a-binary-search-tree/

Given the `root` of a binary search tree (BST) and an integer `val`. 

Find the node in the BST where the node's value equals `val`. Return the subtree rooted with that node. If such a node does not exist, return `null`.

### Example 1
![Example 1 Image](https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg)
```
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
```

### Example 2
![Example 2 Image](https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg)
```
Input: root = [4,2,7,1,3], val = 5
Output: []
```

## Constraints
- The number of nodes in the tree is in the range `[1, 5000]`.
- `1 <= Node.val <= 10^7`
- `root` is a binary search tree.
- `1 <= val <= 10^7`

# Solution Explanation

https://github.com/Reddimus/LeetCode_Notes/blob/main/Trees/Easy/LC_700-Search_in_a_Binary_Search_Tree

### Intuition
We can search a binary search tree by comparing the value we are searching for with the value of the current node. If the value is less than the current node, we search the left subtree to look for a smaller value. If the value is greater than the current node, we search the right subtree to look for a larger value. We can do this recursively or iteratively.

## Approach: Recursive

### Algorithm
1. If the root is `null`, return `null`.
2. If the root's value is less than the value we are searching for, search the right subtree.
3. If the root's value is greater than the value we are searching for, search the left subtree.
4. If the root's value is equal to the value we are searching for, return the root.

### Complexity Analysis
- **Time Complexity:** `O(log n)` | `O(h)
- **Space Complexity:** `O(n)`

**Where `n` is the number of nodes, and `h` is the height of a reasonably balanced tree.**

### Python Code:
```python
class Solution: 
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        return root
```

### C++ Code:
```cpp
class Solution {
public:
    TreeNode *searchBST(TreeNode *root, int val) {
        if (!root)
            return NULL;
        
        if (root->val < val) 
            return searchBST(root->right, val);
        else if (root->val > val) 
            return searchBST(root->left, val);
        return root;
    }
};
```

### Java Code:
```java
class Solution {
    TreeNode searchBST(TreeNode root, int val) {
        if (root == null)
            return null;
        
        if (root.val < val) 
            return searchBST(root.right, val);
        else if (root.val > val)
            return searchBST(root.left, val);
        return root;
    }
}
```

## Approach: Iterative

### Algorithm
1. While the root is not `null`, compare the value we are searching for with the value of the current node.
2. If the value is less than the current node, search the left subtree.
3. If the value is greater than the current node, search the right subtree.
4. If the value is equal to the current node, return the current node.
5. If the value is not found after looping through the entire tree, return `null`.

### Complexity Analysis
- **Time Complexity:** `O(log n)` | `O(h)
- **Space Complexity:** `O(1)`

**Where `n` is the number of nodes, and `h` is the height of a reasonably balanced tree.**

### Python Code:
```python
class Solution: 
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
            else:
                return root
        return None
```

### C++ Code:
```cpp
class Solution {
public:
    TreeNode *searchBST(TreeNode *root, int val) {
        while (root) {
            if (root->val < val) 
                root = root->right;
            else if (root->val > val)
                root = root->left;
            else
                return root;
        }
        return NULL;
    }
};
```

### Java Code:
```java
class Solution {
    TreeNode searchBST(TreeNode root, int val) {
        while (root != null) {
            if (root.val < val) 
                root = root.right;
            else if (root.val > val)
                root = root.left;
            else
                return root;
        }
        return null;
    }
}
```