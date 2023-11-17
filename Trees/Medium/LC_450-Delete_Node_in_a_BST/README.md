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

---

### Hints:
1. 


# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Trees/Medium/LC_450-Delete_Node_in_a_BST)

### Approach: 

### Intuition

### Steps
1. 

### Complexity Analysis
- **Time Complexity:** `O(
- **Space Complexity:** `O(

Where 

### Python Code:
```python
```

### C++ Code:
```cpp
```

### Java Code:
```java
```

### Approach: Iterative

### Intuition

### Steps
1. 

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
```
