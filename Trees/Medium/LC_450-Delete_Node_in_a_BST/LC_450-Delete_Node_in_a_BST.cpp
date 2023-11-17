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
    // Recursive approach
    // T & M: O(log n) | O(h)
    // Where n is num of nodes, and h is height of a resonably balanced tree
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

    /*
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
    */
private:
    TreeNode* searchMinNode(TreeNode* curr) {
        while (curr && curr->left)
            curr = curr->left;
        return curr;
    }
};

int main () {
    return 0;
}