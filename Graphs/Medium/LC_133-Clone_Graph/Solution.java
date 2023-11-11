import java.util.*;
import java.io.*;

class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }

    public Node(int _val, ArrayList _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}

// Depth First Search (DFS) recursive approach
// T: O(V + E), M: O(V), where V = vertice(s), E = edge(s)
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

/*
// Breadth First Search (BFS) iterrative approach
// T: O(V + E), M: O(V), where V = vertice(s), E = edge(s)
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
*/