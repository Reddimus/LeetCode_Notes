import java.util.*;

// Heap/Priority Queue approach
// T: O(n*log n), M: O(n)
// Where n is the length of stones

class Solution {
    public int lastStoneWeight(int[] stones) {
        // Create stones max priority queue
        List<Integer> stonesList = new ArrayList<>(stones.length);
        for (int weight : stones)
            stonesList.add(weight);
        PriorityQueue<Integer> pq = new PriorityQueue<>(stonesList.size(), Collections.reverseOrder());
        pq.addAll(stonesList);
        // Smash stones until there is 1 stone left
        while (pq.size() > 1) {
            int heaviest1 = pq.poll();
            int heaviest2 = pq.poll();
            pq.add(heaviest1 - heaviest2);
        }
        return pq.peek();
    }
}

/*
class Solution {
    // Sorting approach
    // T: O(n^2 log n), M: O(n), where n is the length of stones
    public int lastStoneWeight(int[] stones) {
        // convert stones to a dynamic array
        List<Integer> stones_list = new ArrayList<Integer>();
        for (int stone : stones)
            stones_list.add(stone);
        // sort stones in ascending order to pop the two heaviest stones in O(1) time
        Collections.sort(stones_list);
        // smash stones until there is at most one stone left
        for (int idx = stones_list.size() - 1; idx > 0; idx--) {
            Collections.sort(stones_list);
            int new_stone = stones_list.get(idx) - stones_list.get(idx - 1);
            stones_list.remove(idx);
            stones_list.remove(idx - 1);
            stones_list.add(new_stone);
        }
        return stones_list.get(0);
    }
}
*/

class TestCases {
    public static void main(String[] args) {
        // Run test cases
        // Compile:     javac Solution.java
        // Run:         java -ea TestCases
        Solution sol = new Solution();
        int attempt;
        // Ex1
        attempt = sol.lastStoneWeight(new int[]{2,7,4,1,8,1});
        assert attempt == 1 : "Expected 1 but got " + attempt;
        // Ex2
        attempt = sol.lastStoneWeight(new int[]{1});
        assert attempt == 1 : "Expected 1 but got " + attempt;
        // Test Case 3
        attempt = sol.lastStoneWeight(new int[]{1, 1});
        assert attempt == 0 : "Expected 0 but got " + attempt;
    }
}