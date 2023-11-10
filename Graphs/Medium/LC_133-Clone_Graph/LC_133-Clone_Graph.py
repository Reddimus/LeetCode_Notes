import collections
from typing import Optional

class Node:
    def __init__(self, val: int = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Depth First Search (DFS) recursive approach
# T: O(V + E), M: O(V), where V = vertice(s), E = edge(s)
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

'''
# Breadth First Search (BFS) iterrative approach
# T: O(V + E), M: O(V), where V = vertice(s), E = edge(s)
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
'''
