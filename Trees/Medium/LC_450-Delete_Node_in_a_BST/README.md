# [LeetCode #450 - Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

**Difficulty: `Medium`**

---

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the ***root node reference*** *(possibly updated) of the BST.*

Basically, the deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.

### Example 1

![Example 1 Image](del_node_1.jpg)

Input: 
```
root = [5,3,6,2,4,null,7]
key = 3
```
Output: 
```
[5,4,6,2,null,null,7]
```

**Explanation:** Given key to delete is 3. So we find the node with value 3 and delete it.  
One valid answer is `[5,4,6,2,null,null,7]`, shown in the above BST.  
Please notice that another valid answer is `[5,2,6,null,4,null,7]` and it's also accepted.  
![Example 1 supplement](del_node_supp.jpg)

### Example 2

Input: 
```
root = [5,3,6,2,4,null,7]
key = 0
```
Output: 
```
[5,3,6,2,4,null,7]
```
**Explanation:** The tree does not contain a node with value = 0.


### Example 3

Input: 
```
root = []
key = 0
```
Output: 
```
[]
```

---

### Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- Each node has a **unique** value.
- `root` is a valid binary search tree.
- `-10^5 <= key <= 10^5`

**Follow up question:** Could you solve it recursively and iteratively?

---

### Hints:
1. When deleting a node with 0 children - simply remove the node from the tree.
2. When deleting a node with 1 child - connect the parent of the soon to be deleted node with its only child.
3. When deleting a node with 2 children - find the **successor** of the node. This can be done by finding the leftmost node in the right subtree and swapping it with the node to be deleted. Or finding the rightmost node in the left subtree and swapping it with the node to be deleted.


# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Trees/Medium/LC_450-Delete_Node_in_a_BST)

### Approach: Recursive

### Intuition
When thinking about deleting a node in a Binary search tree there are three cases to consider:
1. The node to be deleted has no children
2. The node to be deleted has one child
3. The node to be deleted has two children

Of these three cases we can combine the first 2 cases into one, since the logic for deleting a node with one child is the same as deleting a node with no children. 

The third case is the most complicated, since we need to find the minimum node in the right subtree of the node to be deleted, and replace the node to be deleted with the minimum node or find the maximum node in the left subtree of the node to be deleted, and replace the node to be deleted with the maximum node.

We can solve this `recursively` by recursively binary searching for the node to be deleted, and then recursively deleting & replacing the subtree node. In this case deleting & replacing the subtree node also recursively searches for the subtree node to be replaced. This approach is more well known.

### Steps
1. Recursively binary search for the node to be deleted.
    - If the node to be deleted is not found, return `null`.
    - Else node found, proceed to case 1, 2, or 3.
2. Found node.
    - Case 1: Node with only one child or no child
        - If the node to be deleted has no children, return `null` (same as returning child pointer)
        - If the node to be deleted has one child, return the `child`.
    - Case 2: Node with two children:
        - Find the minimum valued node in the right subtree.
        - Replace the node to be deleted with the minimum node.
        - Recursively delete the minimum node.
3. Return the root node.

### Complexity Analysis
- **Time Complexity:** `O(log N) | O(H)`  
- **Space Complexity:** `O(log N) | O(H)`  

Where `N` is the number of nodes in the tree, `H` is the height of a reasonably balanced tree.

### Python Code:
```python
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        # Binary search for desired node
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Recursively delete & replace the minimum node of the right subtree
            min_node = self.searchMinNode(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, root.val)

        return root

    def searchMinNode(self, curr: Optional[TreeNode]) -> Optional[TreeNode]:
        while (curr and curr.left):
            curr = curr.left
        return curr
```

### C++ Code:
```cpp
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root)
            return nullptr;

        // Binary search for desired node
        if (root->val > key) {
            root->left = deleteNode(root->left, key);
        }
        else if (root->val < key) {
            root->right = deleteNode(root->right, key);
        }
        else {
            if (!root->right)
                return root->left;
            else if (!root->left)
                return root->right;

            // Recursively del & replace the min node of the right subtree
            TreeNode* minNode = searchMinNode(root->right);
            root->val = minNode->val;
            root->right = deleteNode(root->right, minNode->val);
        }

        return root;
    }
private:
    TreeNode* searchMinNode(TreeNode* curr) {
        while (curr && curr->left)
            curr = curr->left;
        return curr;
    }
};
```

### Java Code:
```java
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null)
            return null;

        // Binary search for desired node
        if (root.val > key) {
            root.left = deleteNode(root.left, key);
        }
        else if (root.val < key) {
            root.right = deleteNode(root.right, key);
        }
        else {
            if (root.left == null)
                return root.right;
            else if (root.right == null)
                return root.left;
            
            // Recursively del & replace the min node of the right subtree
            TreeNode minNode = searchMinNode(root.right);
            root.val = minNode.val;
            root.right = deleteNode(root.right, minNode.val);
        }

        return root;
    }

    private TreeNode searchMinNode(TreeNode curr) {
        while (curr != null && curr.left != null)
            curr = curr.left;
        return curr;
    }
}
```

### Approach: Iterative

### Intuition
When thinking about deleting a node in a Binary search tree there are three cases to consider:
1. The node to be deleted has no children
2. The node to be deleted has one child
3. The node to be deleted has two children

Of these three cases we can combine the first 2 cases into one, since the logic for deleting a node with one child is the same as deleting a node with no children. 

The third case is the most complicated, since we need to find the minimum node in the right subtree of the node to be deleted, and replace the node to be deleted with the minimum node or find the maximum node in the left subtree of the node to be deleted, and replace the node to be deleted with the maximum node.

We can solve this `iteratively` by keeping track of the parent nodes of the desired node to be deleted and the subtree node. However, we need to keep in mind of edge cases such as when the node to be deleted is the root node, or when the subtree node is the root of the subtree.

### Steps
1. Find the node to be deleted and its parent.
    - If the node to be deleted is not found, return `root`.
    - Else node found, proceed to case 1, 2, or 3.
2. Case 1: Node with only one child or no child
    - If the desired node to be deleted is the root node, return the `child` or `null` (same as returning child pointer).
    - If the desired node is the parent's left child, set the parent's left pointer to the desired node's `child`. This disconnects the desired node from the tree and deletes it.
    - Else if the desired node is the parent's right child, set the parent's right pointer to the desired node's `child`. This disconnects the desired node from the tree and deletes it.
3. Case 2: Node with two children
    - Find the minimum valued node in the right subtree.
    - Replace the node to be deleted with the minimum node.
    - Delete the minimum node from the right subtree by setting the minimum node's parent's pointer to the minimum node's right pointer.
        - Covers edge case when the minimum node has a right child.
        - Covers edge case when the minimum node is the root of the right subtree.



### Complexity Analysis
- **Time Complexity:** `O(log N) | O(H)`  
- **Space Complexity:** `O(1)`  

Where `N` is the number of nodes in the tree, `H` is the height of a reasonably balanced tree.

### Python Code:
```python
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Find node to be deleted and its parent
        parent, curr = None, root
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if not curr:  # Node to delete not found
            return root

        # Case 1: Node with only one child or no child
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right

            # Root is the desired node
            if not parent:  # Deleting the root node
                return child

            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child

        # Case 2: Node with two children
        else:
            # Find the minimum valued node in the right subtree
            min_parent, min_node = curr, curr.right
            while min_node.left:
                min_parent = min_node
                min_node = min_node.left

            # Reconnect min_parent to min_node's child or del non-parent min_node
            if min_parent != curr:
                min_parent.left = min_node.right
            else:
                min_parent.right = min_node.right

            # Replace node's value with its min_node's value
            curr.val = min_node.val

        return root
```

### C++ Code:
```cpp
class Solution {
public:
    // Iterative approach
    // T: O(log n) | O(h), M: O(1)
    // Where n is num of nodes, and h is height of a resonably balanced tree
    TreeNode* deleteNode(TreeNode* root, int key) {
        // Find node to be deleted and its parent
        TreeNode *parent = nullptr, *curr = root;
        while (curr && curr->val != key) {
            parent = curr;
            if (curr->val > key)
                curr = curr->left;
            else
                curr = curr->right;
        }

        if (!curr)  // Node to delete not found
            return root;

        // Case 1: Node with only one child or no child
        if (!curr->left || !curr->right) {
            TreeNode *child = (curr->left) ? curr->left : curr->right;

            // Root is the desired node; del root
            if (!parent)
                return child;

            if (parent->left == curr)
                parent->left = child;
            else
                parent->right = child;
        }

        // Case 2: Node with two children
        else {
            // Find the minimum valued node in the right subtree
            TreeNode *minParent = curr, *minNode = curr->right;
            while (minNode && minNode->left) {
                minParent = minNode;
                minNode = minNode->left;
            }

            // Reconnect minParent to minNode's child or nullptr
            if (minParent != curr)
                minParent->left = minNode->right;
            else
                minParent->right = minNode->right;

            // Replace desired node's val with minNode's val
            curr->val = minNode->val;
        }

        return root;
    }
};
```

### Java Code:
```java
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        // Find node to be deleted and its parent
        TreeNode parent = null, curr = root;
        while (curr != null && curr.val != key) {
            parent = curr;
            if (curr.val > key)
                curr = curr.left;
            else
                curr = curr.right;
        }

        if (curr == null)   // Node to delete not found
            return root;

        // Case 1: Node with only one child or no child
        if (curr.left == null || curr.right == null) {
            TreeNode child = (curr.left != null) ? curr.left : curr.right;

            // Root is the desired node; del root
            if (parent == null)
                return child;

            if (parent.left == curr)
                parent.left = child;
            else
                parent.right = child;
        }
        // Case 2: Node with two children
        else {
            // Find the minimum valued node in the right subtree
            TreeNode minParent = curr, minNode = curr.right;
            while (minNode != null && minNode.left != null) {
                minParent = minNode;
                minNode = minNode.left;
            }

            // Reconnect minParent to minNode's child or nullptr
            if (minParent != curr)
                minParent.left = minNode.right;
            else
                minParent.right = minNode.right;

            // Replace desired node's val with minNode's val
            curr.val = minNode.val;
        }

        return root;
    }
}
```
