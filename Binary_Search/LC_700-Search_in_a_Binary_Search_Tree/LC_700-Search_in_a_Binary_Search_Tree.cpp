// #include <bits/stdc++.h>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    // Iterative approach
    // T: O(log n) | O(h), M: O(1)
    // Where n is num of nodes, and h is height of resonably balanced tree
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

    /*
    // Recursive approach
    // T: O(log n) | O(h), M: O(1)
    // Where n is num of nodes, and h is height of resonably balanced tree
    TreeNode *searchBST(TreeNode *root, int val) {
        if (!root)
            return nullptr;
        
        if (root->val < val) 
            return searchBST(root->right, val); // increase curr node value
        else if (root->val > val) 
            return searchBST(root->left, val);  // decrease curr node value
        
        return root;    // Found value
    }
    */
};

int main() {
    return 0;
}