import java.util.*;

class KthLargest {
    int k;
    PriorityQueue<Integer> nums_pq = new PriorityQueue<Integer>();
    // // T: O(n*log k), M: O(n), where n is the length of nums and k is kth largest element
    public KthLargest(int k, int[] nums) {
        this.k = k;
        // heapify nums priority queue
        List<Integer> numsList = new ArrayList<>();
        for (int num: nums)
            numsList.add(num);
        nums_pq = new PriorityQueue<Integer>(numsList);
        // keep the top k largest elements in nums priority queue
        while (nums_pq.size() > k)
            nums_pq.poll();
    }
    // T: O(log k), M: O(1)
    public int add(int val) {
        nums_pq.add(val);
        // remove the smallest element in nums priority queue
        while (nums_pq.size() > k)
            nums_pq.poll();
        return nums_pq.peek();
    }

    /*
    // Heap class from scratch approach

    Heap nums_heap = new Heap();
    // T: O(n*log k), M: O(k), where n is the length of nums and k is kth largest element
    public KthLargest(int k, int[] nums) {
        this.k = k;
        // initialize nums priority queue
        nums_heap.heapify(nums);
        // keep the top k largest elements in nums priority queue
        while (nums_heap.heap.size() > k + 1)
            nums_heap.pop();
    }
    // T: O(log k), M: O(1)
    public int add(int val) {
        nums_heap.push(val);
        // remove the smallest element in nums priority queue
        while (nums_heap.heap.size() > k + 1)
            nums_heap.pop();
        return nums_heap.heap.get(1);
    }
    */
}

/*
// Heap class from scratch
class Heap {
    // Instance variables
    public ArrayList<Integer> heap;
    // Constructor
    public Heap() {
        // intialize heap with dummy value at index 0
        this.heap = new ArrayList<Integer>(Arrays.asList(0));
    }
    // Methods

    // T: O(log h), M: O(1), where h is the height of the heap
    public void push(int val) {
        // add val to end of heap
        this.heap.add(val);

        // percolate up
        int i = this.heap.size() - 1;
        // while parent node > current child node
        while (i > 1 && this.heap.get(i/2) > this.heap.get(i)) {
            Collections.swap(this.heap, i/2, i);
            i = i/2;    // update i to parent node
        }
    }

    // T: O(log h), M: O(1)
    // remove and return the root node
    public int pop() {
        if (this.heap.size() == 1)
            return this.heap.get(1);
        if (this.heap.size() == 2)
            return this.heap.remove(1);
        
        int root_popped = this.heap.get(1);
        // swap root with last node
        Collections.swap(this.heap, 1, this.heap.size() - 1);
        // remove last node
        this.heap.remove(this.heap.size() - 1);
        // percolate down from new root
        int i = 1;
        percolate_down(i);
        return root_popped;
    }

    // T: O(0*n/2 + 1*n/4 + 2*n/8 + ... + log n*n/n) = O(n), M: O(1)
    public ArrayList<Integer> heapify(int[] arr) {
        if (arr.length == 0)
            return new ArrayList<Integer>();
        // adjust structure property: give space for dummy node at index 0
        ArrayList<Integer> arrList = Arrays.stream(arr).boxed().collect(Collectors.toCollection(ArrayList::new));
        arrList.add(arrList.get(0));
        arrList.set(0, 0);
        // adjust order property: percolate down from last parent node
        this.heap = arrList;
        int curr = this.heap.size() / 2;
        while (curr > 0) {
            percolate_down(curr);
            curr--;
        }
        return arrList;
    }

    // T: O(log h), M: O(1)
    public void percolate_down(int i) {
        // while child node within range of heap
        while (2 * i < this.heap.size()) {
            // (if right child in heap range) and (curr node > right child) and (right child < left child)
            if (2*i+1 < this.heap.size() && this.heap.get(i) > this.heap.get(2*i+1) && this.heap.get(2*i+1) < this.heap.get(2*i)) {
                Collections.swap(this.heap, i, 2*i+1);
                i = 2*i+1;
            }
            else if (this.heap.get(i) > this.heap.get(2*i)) {
                Collections.swap(this.heap, i, 2*i);
                i = 2*i;
            }
            else
                break;
        }
        return;
    }
}
*/

class TestCases {
    // main method to test KthLargest class
    public static void main(String[] args) {
        // Run Test Cases:
        // Compile:     javac KthLargest.java
        // Run:         java -ea TestCases
        // Ex1:
        KthLargest kthLargest = new KthLargest(3, new int[]{4, 5, 8, 2});
        int attempt;
        attempt = kthLargest.add(3);   // return 4
        assert attempt == 4 : "Expected 4, got " + attempt;
        attempt = kthLargest.add(5);   // return 5
        assert attempt == 5 : "Expected 5, got " + attempt;
        attempt = kthLargest.add(10);  // return 5
        assert attempt == 5 : "Expected 5, got " + attempt;
        attempt = kthLargest.add(9);   // return 8
        assert attempt == 8 : "Expected 8, got " + attempt;
        attempt = kthLargest.add(4);   // return 8
        assert attempt == 8 : "Expected 8, got " + attempt;
    }
}