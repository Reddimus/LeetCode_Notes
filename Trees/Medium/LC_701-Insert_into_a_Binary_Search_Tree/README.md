# [LeetCode #701 - Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

**Difficulty: `Medium`**

---

You are given the `root` node of a binary search tree (BST) and a `value` to insert into the tree. Return the *root node of the BST after the insertion*. It is **guaranteed** that the new value does not exist in the original BST.

**Notice** that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return **any of them**.

### Example 1

![Example 1 Image](insertbst.jpg)

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

![Example 2 Image](bst.jpg)

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

---

### Constraints

- The number of nodes in the tree will be in the range `[0, 10^4]`.
- `-10^8 <= Node.val <= 10^8`
- All the values `Node.val` are unique.
- `-10^8 <= val <= 10^8`
- It's guaranteed that `val` does not exist in the original BST.

Follow up question: Can you solve this both `recursively` and `iteratively`?

---

### Hints:
1. Binary search for the insertion position. A Binary Search Tree (BST) has the smallest element as the left most node, while the largest element is the right most node. Solve [LeetCode 700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) first to get a better understanding of the BST structure.

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Trees/Medium/LC_701-Insert_into_a_Binary_Search_Tree)

### Approach: Iterative

### Intuition
We want to imagine we are searching for a node equal to the value we want to insert, in most cases the Binary Search Tree (BST) will not have a node with the same value we want to insert and we will be out of bounds. This out of bounds node will be the node we want to insert our new node into. To do this we will recall the previous node we visited and connect it to the new node.

To do this using an `Iterative approach` we will use a `while` loop to search for the null position to insert our new node. We will also need to keep track of the previous node we visited so we can connect it to the new node.

### Steps
1. Check for an edge case where BST is empty, if so `return a new node` with the value we want to insert.
2. Create two pointers `curr` and `prev` and set them both to the root node. Then traverse the BST using a `while` loop until `curr` is `null`.
    - `prev` will be the previous node we visited and will be constantly updated.
    - If our `curr` node is greater than the value we want to insert, we will move `curr` to the left child node to decrease the value of `curr`.
    - Else our `curr` node is less than or equal to the value we want to insert, we will move `curr` to the right child node to increase the value of `curr`.
3. Once we have found the null position to insert our new node, we will check if the previous node is greater than the value we want to insert.
    - If so, we will connect the previous node's left child to a new node with the value we want to insert.
    - Else we will connect the previous node's right child to a new node with the value we want to insert.
4. The desired node has been inserted, so we will return the root node of the BST.


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
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root)
            return new TreeNode(val);

        // Binary Search for insert null position
        TreeNode *prev = root, *curr = root;
        while (curr) {
            prev = curr;
            if (curr->val > val)
                curr = curr->left;
            else
                curr = curr->right;
        }

        // Connect previous node to the new position
        if (prev->val > val)
            prev->left = new TreeNode(val);
        else
            prev->right = new TreeNode(val);

        return root;
    }
};
```

### Java Code:
```java
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null)
            return new TreeNode(val);
        
        // Binary Search for insert null position
        TreeNode prev = root, curr = root;
        while (curr != null) {
            prev = curr;
            if (curr.val > val)
                curr = curr.left;
            else
                curr = curr.right;
        }

        // Connect previous node to the new position
        if (prev.val > val)
            prev.left = new TreeNode(val);
        else
            prev.right = new TreeNode(val);

        return root;
    }
}
```

### Approach: Recursive

### Intuition
We want to imagine we are searching for a node equal to the value we want to insert, in most cases the Binary Search Tree (BST) will not have a node with the same value we want to insert and we will be out of bounds. This out of bounds node will be the node we want to insert our new node into. To do this we will recall the previous node we visited and connect it to the new node.

To do this using a `Recursive approach` we will call our `insertIntoBST` to search for the null position to insert our new node. We will also need to keep track of the previous node we visited so we can connect it to the new node.

### Steps
1. If current node does not exist, we have found the null position to insert our new node, so we will `return a new node` with the value we want to insert.
2. Recursively Binary search for Insert position.
    - If our current node is greater than the value we want to insert, we will recursively call `insertIntoBST` on the left child node to decrease the value of the current node.
    - Else our current node is less than or equal to the value we want to insert, we will recursively call `insertIntoBST` on the right child node to increase the value of the current node.
3. Once we have popped out of our recursive calls/inserted our new node, we will `return the root node` of the BST.

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
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root)
            return new TreeNode(val);

        // Recursively search for null position, then connect previous node to new node
        if (root->val > val)
            root->left = insertIntoBST(root->left, val);    // decrease current node
        else
            root->right = insertIntoBST(root->right, val);  // increase current node

        return root;
    }
};
```

### Java Code:
```java
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null)
            return new TreeNode(val);

        // Recursively search for null position, then connect previous node to new node
        if (root.val > val)
            root.left = insertIntoBST(root.left, val);      // decrease current node
        else
            root.right = insertIntoBST(root.right, val);    // increase current node
        
        return root;
    }
}
```