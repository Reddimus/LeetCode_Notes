# [LeetCode #703 - Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

**Difficulty: `Easy`**

---

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement `KthLargest` class:
- `KthLargest(int k, int[] nums)`: Initializes the object with the integer `k` and the stream of integers `nums`.
- `int add(int val)`: Appends the integer `val` to the stream and returns the element representing the `kth` largest element in the stream.

**Example 1:**  
Input:   
```
["KthLargest", "add", "add", "add", "add", "add"]
```
```
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
```
Output:  
```
[null, 4, 5, 5, 8, 8]
```

**Explanation**:  
```
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);  
kthLargest.add(3);      // return 4  
kthLargest.add(5);      // return 5  
kthLargest.add(10);     // return 5  
kthLargest.add(9);      // return 8  
kthLargest.add(4);      // return 8  
```

**Constraints:**
- `1 <= k <= 10^4`
- `0 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `-10^4 <= val <= 10^4`
- At most `10^4` calls will be made to `add`.
- It is guaranteed that there will be at least `k` elements in the array when you search for the `kth` element.

### Hints:
- Whene we initialize the class we want to keep the top `k` elements in a sorted order. 
- When we add a new element, we also want to check if the data structure is still size `k`. If the new data structuer size is greater than `k`, we want to remove the smallest element.

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Heap-Priority_Queue/Easy/LC_703-Kth_Largest_Element_in_a_Stream)

### Heap - Priority Queue approach

#### Intuition:
In this problem, we are essentially asked to keep track of the `kth` largest element given an unsorted list of integers. Although you may think of sorting the list and then finding the `kth` largest element, this is not the best approach as we add integers. Instead we can manipulate the properties of a heap/priority queue to solve this problem. The min heap keeps track of the smallest element of a list, whether we pop or push elements.

#### Steps:
1. **Initialization**: 
    - Create a `heap/priority queue` accessable to all methods in the class. Then heapify the list of given integers named `nums`. This will sort the list in `O(n)` time.
    - Keep the top `k` largest elements in the heap. While the heap size is greater than `k`, pop the smallest element from the heap.
2. **Add Method**:
    - When adding a new integer `val`, push it into the heap.
    - If the heap size is greater than `k`, pop the smallest element from the heap.
    - Return the smallest element in the heap.

#### Initialization Complexity Analysis
- Time Complexity: `O(N log N)`
- Space Complexity: `O(N)`  

#### Add method Complexity Analysis
- Time Complexity: `O(log N)`  
- Space Complexity: `O(1)`  

Where `N` is the number of elements in the heap. `K` is the size of `Kth` largest element.

## Python Code
```python
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        heapq.heapify(nums)
        self.hq = nums
        # keep the top k largest elements in nums heap
        while len(self.hq) > k:
            heapq.heappop(self.hq)

    def add(self, val: int) -> int:
        heapq.heappush(self.hq, val)
        # remove the smallest element in the heap
        if len(self.hq) > self.k:
            heapq.heappop(self.hq)
        return self.hq[0]
```

## C++ Code
```cpp
class KthLargest {
private:
    int k;
    priority_queue<int, vector<int>, greater<int>> pq;

public:
    KthLargest(int k, vector<int>& nums) : pq(nums.begin(), nums.end()) {
        this->k = k;
        // keep the top k largest elements in nums priority queue
        while (pq.size() > k)
            pq.pop();
    }
    int add(int val) {
        pq.push(val);
        // remove the smallest element in the priority queue
        while (pq.size() > k)
            pq.pop();
        return pq.top();
    }
};
```

## Java Code
```java
class KthLargest {
    int k;
    PriorityQueue<Integer> pq;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        // heapify nums priority queue
        List<Integer> numsList = new ArrayList<>(nums.length);
        for (int num : nums)
            numsList.add(num);
        pq = new PriorityQueue<Integer>(numsList);
        // keep the top k largest elements in nums priority queue
        while (pq.size() > k)
            pq.poll();
    }

    public int add(int val) {
        pq.add(val);
        // remove the smallest element in the priority queue
        while (pq.size() > k)
            pq.poll();
        return pq.peek();
    }
}
```