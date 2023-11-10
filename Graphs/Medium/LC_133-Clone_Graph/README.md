
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

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Graphs/Medium/LC_133-Clone_Graph)

### Approach: Graphs - Depth First Search (DFS) Recursive Approach

#### Intuition

#### Complexity Analysis
- Time Complexity: `O()`
- Space Complexity: `O()`

Where 

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
```

## Java Code
```java
```

### Approach: Graphs - Depth First Search (BFS) Iterative Approach

#### Intuition

#### Complexity Analysis
- Time Complexity: `O()`
- Space Complexity: `O()`

Where

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
```

## Java Code
```java
```