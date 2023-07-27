/*
LeetCode #1046 - Last Stone Weight prompt:
Easy

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them 
together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
*/

import java.util.*;

class Solution {
    // Heap approach
    // T: O(n*log n), M: O(n), where n is the length of stones
    public int lastStoneWeight(int[] stones) {
        // heapify list of stones in descending order
        List<Integer> stonesList = new ArrayList<>();
        for (int stone: stones) {
            stonesList.add(stone);
        }
        PriorityQueue<Integer> stones_pq = new PriorityQueue<>(stonesList.size(), Collections.reverseOrder());
        stones_pq.addAll(stonesList);
        // smash stones until there is at most one stone left
        while (stones_pq.size() > 1) {
            int biggest = stones_pq.poll();
            int sec_biggest = stones_pq.poll();
            stones_pq.add(biggest - sec_biggest);
        }
        return stones_pq.peek();
    }
    /*
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
    */
}

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