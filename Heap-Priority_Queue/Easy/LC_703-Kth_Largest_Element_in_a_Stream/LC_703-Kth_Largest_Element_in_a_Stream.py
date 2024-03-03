import heapq

# Heap / Priority Queue approach

class KthLargest:
    
    # T: O(n log n), M: O(n)
    # Where n is the length of nums and k is kth largest element
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        heapq.heapify(nums)
        self.hq = nums
        # keep the top k largest elements in nums heap
        while len(self.hq) > k:
            heapq.heappop(self.hq)
    
    # T: O(log n), M: O(1)
    def add(self, val: int) -> int:
        heapq.heappush(self.hq, val)
        # remove the smallest element in the heap
        if len(self.hq) > self.k:
            heapq.heappop(self.hq)
        return self.hq[0]
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

'''
class KthLargest:

    # Heap from scratch approach
    # T: O(n log k), M: O(k), where n is the length of nums and k is kth largest element
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums_heap = Heap()
        self.nums_heap.heapify(nums)
        while len(self.nums_heap.heap) > k + 1:
            self.nums_heap.pop()
    # T: O(log k), M: O(1) 
    def add(self, val: int) -> int:
        self.nums_heap.push(val)
        if len(self.nums_heap.heap) > self.k + 1:
            self.nums_heap.pop()
        return self.nums_heap.heap[1]
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Heap from scratch:
class Heap:
    def __init__(self):
        self.heap = [None]
    # T: O(log h), M: O(1), where h is the height of the heap
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        # Percolate up
        # while parent node > current child node
        while i > 1 and self.heap[i // 2] > self.heap[i]:
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
        self.percolate_down(i)
        return val_popped
    # T: O(h), M: O(1)
    def heapify(self, arr: list) -> list:
        if not arr:
            return []
        # adjust structure property: give space for dummy value at 0th index
        arr.append(arr[0])
        arr[0] = None
        # adjust order property: start from last parent node and percolate down
        self.heap = arr
        curr = len(self.heap) // 2
        while curr > 0:
            # percolate down
            i = curr
            self.percolate_down(i)
            curr -= 1
        return self.heap
    # T: O(log h), M: O(1)
    def percolate_down(self, i: int):
        while 2 * i < len(self.heap):
            # if 2*i+1 index in heap range and curr parent node > right child node and right child node < left child node 
            if (2*i+1 < len(self.heap)) and (self.heap[i] > self.heap[2*i+1]) and (self.heap[2*i+1] < self.heap[2*i]):
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2*i]:
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2 * i
            else:
                break
        return
'''

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
