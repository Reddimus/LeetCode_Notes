#include <bits/stdc++.h>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

// Depth First Search (DFS) recursive approach
// T: O(V + E), M: O(V), where V = vertice(s), E = edge(s)
class Solution {
public:
    Node* cloneGraph(Node* node) {
        unordered_map<int, Node*> clones;	// map unique old node vals -> new nodes
        return node ? dfs(node, clones) : nullptr;
    }
private:
    Node* dfs(Node* node, unordered_map<int, Node*>& clones) {
        if (clones.find(node->val) != clones.end()) 
            return clones[node->val];	// deep copy already mapped

        Node* clone = new Node(node->val);	// create deep copy of current node
        clones[node->val] = clone;
        for (Node* nghbrNode : node->neighbors) 	// recursively connect nodes
            clone->neighbors.push_back(dfs(nghbrNode, clones));
        
        return clone;
    }
};

/*
// Breadth First Search (BFS) iterrative approach
// T: O(V + E), M: O(V), where V = vertice(s), E = edge(s)
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node)
            return nullptr;

        // Map unique old node vals -> new nodes
        unordered_map<int, Node*> clones;
        clones[node->val] = new Node(node->val);
        queue<Node*> q;
        q.push(node);   // queue old nodes in FCFS/FIFO order
        // While there are old nodes to traverse
        while (!q.empty()) {
            Node* currNode = q.front();
            q.pop();
            Node* currClone = clones[currNode->val];
            // link neighboring new nodes
            for (Node* nghbrNode : currNode->neighbors) {
                if (clones.find(nghbrNode->val) == clones.end()) {
                    clones[nghbrNode->val] = new Node(nghbrNode->val);
                    q.push(nghbrNode);
                }
                currClone->neighbors.push_back(clones[nghbrNode->val]);
            }
        }

        return clones[node->val];
    }
};
*/

int main() {
	return 0;
}