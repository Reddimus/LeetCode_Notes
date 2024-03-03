# [LeetCode #1046 - Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)

**Difficulty: `Easy`**

---

You are given an array of integers `stones` where `stones[i]` is the weight of the `ith` stone.

We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

- If `x == y`, both stones are destroyed, and
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left.

Return *the weight of the last remaining stone*. If there are no stones left, return `0`.

**Example 1:**  
Input:  
```
stones = [2,7,4,1,8,1]
```
Output:  
```
1
```
Explanation:  
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,  
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,  
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,  
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.  

**Example 2:**  
Input:  
```
stones = [1]
```
Output:  
```
1
```

**Constraints:**
- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`

### Hints:
- There is a data structure that can "sort" an array in `O(n)` time, push and pop elements in `O(log n)` time, and allow max and min element access in `O(1)` time. This data structure would be best for smashing pairs of the heaviest stones and inserting the new stone.

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Heap-Priority_Queue/Easy/LeetCode_1046-Last_Stone_Weight)

### Heap - Priority Queue approach

#### Intuition:
In this problem, we are essentially asked to smash the heaviest stones together until there is at most one stone left. We can use a max heap to keep track of the heaviest stones and smash them together. The max heap will allow us to pop the heaviest stones in `O(log n)` time and push the result back into the heap in `O(log n)` time, all the while having a sorted order of the stones.

#### Steps:
1. **Create max Heap/Priority Queue**: 
    - Create a max heap from the list of stones.
2. **Smash Stones until there is 1 stone left**:
    - While there are more than 1 stone in the heap, pop the heaviest 2 stones and smash them together. Then push the result back into the heap.
3. **Return the weight of the last remaining stone**

#### Complexity Analysis
- Time Complexity: `O(n log n)`  
- Space Complexity: `O(1)`  

Where `N` is the length of the `stones` list.

## Python Code
```python
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Create stones max heap
        stones = [-weight for weight in stones]
        heapq.heapify(stones)
        # Smash stones until there is 1 stone left
        while len(stones) > 1:
            heaviest1, heaviest2 = heapq.heappop(stones), heapq.heappop(stones)
            heapq.heappush(stones, heaviest1 - heaviest2)
        return -stones[0]
```

## C++ Code
```cpp
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // Create stones max heap
        priority_queue<int> pq = priority_queue<int>(stones.begin(), stones.end());
        // Smash stones until there is 1 stone left
        while (pq.size() > 1) {
            int heaviest1 = pq.top(); pq.pop();
            int heaviest2 = pq.top(); pq.pop();
            pq.push(heaviest1 - heaviest2);
        }
        return pq.top();
    }
};
```

## Java Code
```java
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
```
