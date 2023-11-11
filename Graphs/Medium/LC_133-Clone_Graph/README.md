
# [LeetCode #133 - Clone Graph](https://leetcode.com/problems/clone-graph/)

**Difficulty: `Medium`**

---

Given a reference of a node in a [connected](https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph) undirected graph.

Return a [deep copy](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph. 

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```
class Node {
	public int val;
	public List<Node> neighbors;
}
```

---

### Test Case Format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `val == 1`, the second node with `val == 2`, and so on. The graph is represented in the test case using an adjacency list.

**An adjacency list** is a collection of unordered **lists** used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the **copy of the given node** as a reference to the cloned graph.

**Example 1**:  
![Clone Graph Example 1](https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png)

Input:  
```
adjList = [[2,4],[1,3],[2,4],[1,3]]
```

Output:  
```
[[2,4],[1,3],[2,4],[1,3]]
```

Explanation:  
There are 4 nodes in the graph.  
- 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
- 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
- 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
- 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

**Example 2**:  
![Clone Graph Example 2](https://assets.leetcode.com/uploads/2020/01/07/graph.png)

Input:  
```
adjList = [[]]
```

Output:  
```
[[]]
```

Explanation:  
Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

**Example 3**:

Input:  
```
adjList = []
```

Output:  
```
[]
```

Explanation:  
This an empty graph, it does not have any nodes.

---

### Constraints:

- The number of nodes in the graph is in the range `[0, 100]`.
- `1 <= Node.val <= 100`
- `Node.val` is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

---

### Hints:
1. Think of data structures that can quickly lookup existing nodes visited.
2. We can traverse the graph using [Breadth First Search (BFS)](https://en.wikipedia.org/wiki/Breadth-first_search) or [Depth First Search (DFS)](https://en.wikipedia.org/wiki/Depth-first_search).
3. A graph is a connected graph, which means that starting from any node, we can reach all nodes in the graph.

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Graphs/Medium/LC_133-Clone_Graph)

### Approach: Graphs - Depth First Search (DFS) Recursive Approach

### Intuition

The challenge in cloning a graph lies in creating an exact copy of the original graph's structure without getting trapped in cycles or duplicating nodes. The key here is to maintain a mapping between the original graph's nodes and the new cloned nodes. This mapping ensures that each original node corresponds to exactly one cloned node, thereby preserving the graph's structure and connectivity in the clone.

When we encounter a node during traversal, we have two scenarios:
1. **The node has not been visited:** We create a new node as the clone, add it to our mapping, and continue to recursively clone its neighbors.
2. **The node has been visited:** This means its clone already exists in our mapping. We use this cloned node directly to avoid duplication and infinite loops.

This process effectively does a deep copy, ensuring that each node and its connections are replicated accurately. We can start this process from the given node and continue until all nodes in the connected graph are cloned.

Imagine traversing the graph node by node. For each node, we check our mapping:
- If it's a new node, we create a clone and explore its neighbors, updating the mapping with new clones.
- If it's an already visited node, we use the existing clone from our mapping to maintain connections.

This approach respects the graph's structure, ensuring that the cloned graph mirrors the original graph in terms of node values and connections.

### Steps:
1. Initialize an empty hashmap representing the mapping from old nodes to new nodes.
2. Define a recursive function that can modify the existing hashmap to clone the graph.
	- If the current node is already in the hashmap, return the corresponding cloned node.
	- Otherwise, create a deep copy of the current node, add it to the hashmap, and recursively clone its neighbors.
3. Return the first cloned node from the recursive function if the given node exists, otherwise return `NULL`.

#### Complexity Analysis
- Time Complexity: `O(V + E)`  
- Space Complexity: `O(V)`  

Where `V` is the number of vertices (nodes) and `E` is the number of edges in the graph.

## Python Code
```python
class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        clones = {} # map unique old node vals -> new nodes
        
        def dfs(node: Optional[Node]) -> Optional[Node]:
            if node.val in clones:
                return clones[node.val] # deep copy already mapped

            clone = Node(node.val)  # create deep copy of current node
            clones[node.val] = clone
            for nghbr_node in node.neighbors:   # recursively connect nodes
                clone.neighbors.append(dfs(nghbr_node))
            
            return clone

        return dfs(node) if node else None

```

## C++ Code
```cpp
class Solution {
public:
    Node* cloneGraph(Node* node) {
        // map unique old node vals -> new nodes
        unordered_map<int, Node*> clones;
        return node ? dfs(node, clones) : nullptr;
    }
private:
    Node* dfs(Node* node, unordered_map<int, Node*>& clones) {
        if (clones.find(node->val) != clones.end()) 
            return clones[node->val];   // deep copy already mapped

        Node* clone = new Node(node->val);  // create deep copy of current node
        clones[node->val] = clone;
        for (Node* nghbrNode : node->neighbors)     // recursively connect nodes
            clone->neighbors.push_back(dfs(nghbrNode, clones));
        
        return clone;
    }
};
```

## Java Code
```java
class Solution {
    public Node cloneGraph(Node node) {
        // map unique old node vals -> new nodes
        HashMap<Integer, Node> clones = new HashMap<Integer, Node>();
        return (node != null) ? dfs(node, clones) : null;
    }

    private Node dfs(Node node, HashMap<Integer, Node> clones) {
        if (clones.containsKey(node.val))
            return clones.get(node.val);    // deep copy already mapped
        
        Node clone = new Node(node.val);    // create deep copy of current node
        clones.put(node.val, clone);
        for (Node nghbrNode : node.neighbors)   // recursively connect nodes
            clone.neighbors.add(dfs(nghbrNode, clones));
        
        return clone;
    }
}
```

### Approach: Graphs - Depth First Search (BFS) Iterative Approach

#### Intuition
The challenge in cloning a graph lies in creating an exact copy of the original graph's structure without getting trapped in cycles or duplicating nodes. The key here is to maintain a mapping between the original graph's nodes and the new cloned nodes while also keeping track of a queue. This mapping associated with our queue ensures that each original node corresponds to exactly one cloned node, thereby preserving the graph's structure and connectivity in the clone.

When we encounter a node during traversal, we do 2 things:
1. Read the current node from the queue.
2. Create a new node as the clone, add it to our mapping, and continue to clone its neighbors.

This process effectively does a deep copy, ensuring that each node and its connections are replicated accurately. We can start this process from the given node and continue until all nodes in the connected graph are cloned.

### Steps:
1. Initialize a hashmap with the first node's value as the key and a deep copy of the first node as the value.
2. Initialize a queue and add the first node to it.
3. While the queue is not empty:
	- Pop the first node from the queue.
	- For each neighbor of the current node:
		- If the neighbor is not in the hashmap, create a deep copy of it and add it to the hashmap.
		- Add the neighbor to the current node's clone's neighbors.
		- Add the neighbor to the queue.
4. Return the first cloned node from the hashmap.

#### Complexity Analysis
- Time Complexity: `O(V + E)`  
- Space Complexity: `O(V)`  

Where `V` is the number of vertices (nodes) and `E` is the number of edges in the graph.

## Python Code
```python
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        # Map unique old node vals -> new nodes
        clones = {node.val: Node(node.val, [])}
        q = collections.deque()
        q.append(node)  # queue old nodes in FCFS/FIFO order
        # While there are old nodes to traverse
        while q:
            curr_node = q.popleft()
            curr_clone = clones[curr_node.val]
            # link neighboring new nodes
            for ngbr_node in curr_node.neighbors:
                if ngbr_node.val not in clones:
                    clones[ngbr_node.val] = Node(ngbr_node.val, [])
                    q.append(ngbr_node)
                
                curr_clone.neighbors.append(clones[ngbr_node.val])

        return clones[node.val]
```

## C++ Code
```cpp
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
```

## Java Code
```java
class Solution {
    public Node cloneGraph(Node node) {
        if (node == null)
            return null;

        // Map unique old node vals -> new nodes
        HashMap<Integer, Node> clones = new HashMap<>();
        clones.put(node.val, new Node(node.val));
        // queue old nodes in FCFS/FIFO order
        Queue<Node> q = new LinkedList<>();
        q.add(node);
        // While there are old nodes to traverse
        while (!q.isEmpty()) {
            Node currNode = q.poll();
            Node currClone = clones.get(currNode.val);
            // link neighboring new nodes
            for (Node nghbrNode : currNode.neighbors) {
                if (!clones.containsKey(nghbrNode.val)) {
                    clones.put(nghbrNode.val, new Node(nghbrNode.val));
                    q.add(nghbrNode);
                }
                currClone.neighbors.add(clones.get(nghbrNode.val));
            }
        }

        return clones.get(node.val);
    }
}
```