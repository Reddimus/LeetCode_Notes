#include <bits/stdc++.h>

using namespace std;

//  Definition for a binary tree node.
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
    // Where n is num of nodes, and h is height of a resonably balanced tree
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

    /*
    // Recursive approach
    // T & M: O(log n) | O(h)
    // Where n is num of nodes, and h is height of a resonably balanced tree
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
    */
};

int main() {
    return 0;
}