class Solution {
    // Iterative approach
    // T: O(log n) | O(h), M: O(1)
    // Where n is num of nodes, and h is height of resonably balanced tree
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

    /*
    class Solution {
        // Recursive approach
        // T: O(log n) | O(h), M: O(n)
        // Where n is num of nodes, and h is height of resonably balanced tree
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
    */
}