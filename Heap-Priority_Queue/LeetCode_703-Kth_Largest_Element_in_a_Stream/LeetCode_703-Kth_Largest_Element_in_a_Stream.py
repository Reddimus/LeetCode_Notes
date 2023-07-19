'''
LeetCode 703 - Kth Largest Element in a Stream prompt:

Design a class to find the kth largest element in a stream. Note that it is 
the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and 
the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the 
element representing the kth largest element in the stream.

Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
 
Constraints:
1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array 
when you search for the kth element.
'''

import heapq

class KthLargest:
    
    # T: O(n log k), M: O(k), where n is the length of nums and k is kth largest element
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        heapq.heapify(nums)
        self.nums_heap = nums
        while len(self.nums_heap) > k:
            heapq.heappop(self.nums_heap)
    # T: O(log k), M: O(1)
    def add(self, val: int) -> int:
        heapq.heappush(self.nums_heap, val)
        if len(self.nums_heap) > self.k:
            heapq.heappop(self.nums_heap)
        return self.nums_heap[0]
    '''
    # T: O(n log k), M: O(k), where n is the length of nums and k is kth largest element
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums_heap = Heap()
        for num in nums:
            self.nums_heap.push(num)
        while len(self.nums_heap.heap) > k + 1:
            self.nums_heap.pop()
    # T: O(log k), M: O(1) 
    def add(self, val: int) -> int:
        self.nums_heap.push(val)
        if len(self.nums_heap.heap) > self.k + 1:
            self.nums_heap.pop()
        return self.nums_heap.heap[1]
    '''
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Heap from scratch:
class Heap:
    def __init__(self):
        self.heap = [0]
    # T: O(log h), M: O(1), where h is the height of the heap
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        # Percolate up
        # while parent node > current child node
        while self.heap[i // 2] > self.heap[i] and i > 1:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i // 2
    # T: O(log h), M: O(1)
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        val_popped = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        # Percolate down
        i = 1
        while 2 * i < len(self.heap):
            # if curr parent node > right child node and 2*i+1 index in heap range and right child node < left child node 
            if (2*i+1 < len(self.heap)) and (self.heap[i] > self.heap[2*i+1]) and (self.heap[2*i+1] < self.heap[2*i]):
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2*i]:
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2 * i
            else:
                break
        return val_popped

# Example 1:
kth = KthLargest(3, [4, 5, 8, 2])
attempt = kth.add(3)
assert attempt == 4, f'Wrong output: {attempt} != 4'
attempt = kth.add(5)
assert attempt == 5, f'Wrong output: {attempt} != 5'
attempt = kth.add(10)
assert attempt == 5, f'Wrong output: {attempt} != 5'
attempt = kth.add(9)
assert attempt == 8, f'Wrong output: {attempt} != 8'
attempt = kth.add(4)
assert attempt == 8, f'Wrong output: {attempt} != 8'
# Test case 2:
kth = KthLargest(1, [])
attempt = kth.add(-3)
assert attempt == -3, f'Wrong output: {attempt} != -3'
attempt = kth.add(-2)
assert attempt == -2, f'Wrong output: {attempt} != -2'
attempt = kth.add(-4)
assert attempt == -2, f'Wrong output: {attempt} != -2'
attempt = kth.add(0)
assert attempt == 0, f'Wrong output: {attempt} != 0'
attempt = kth.add(4)
assert attempt == 4, f'Wrong output: {attempt} != 4'
# Test case 3:
kth = KthLargest(2, [0])
attempt = kth.add(-1)
assert attempt == -1, f'Wrong output: {attempt} != -1'
attempt = kth.add(1)
assert attempt == 0, f'Wrong output: {attempt} != 0'
attempt = kth.add(-2)
assert attempt == 0, f'Wrong output: {attempt} != 0'
attempt = kth.add(-4)
assert attempt == 0, f'Wrong output: {attempt} != 0'
attempt = kth.add(3)
assert attempt == 1, f'Wrong output: {attempt} != 1'