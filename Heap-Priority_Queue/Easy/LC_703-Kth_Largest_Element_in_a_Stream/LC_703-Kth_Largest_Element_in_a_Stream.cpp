#include <bits/stdc++.h>

using namespace std;

// Heap / Priority Queue approach

class KthLargest {
private:
    int k;
    priority_queue<int, vector<int>, greater<int>> pq;
public:
    // T: O(n log n), M: O(n)
    // Where n is the length of nums and k is kth largest element
    KthLargest(int k, vector<int>& nums) : pq(nums.begin(), nums.end()) {
        this->k = k;
        // keep the top k largest elements in nums priority queue
        while(pq.size() > k) 
            pq.pop();
    }
    // T: O(log n), M: O(1)
    int add(int val) {
        pq.push(val);
        // remove the smallest element in the priority queue
        while (pq.size() > k) 
            pq.pop();
        return pq.top();
    }
};

int main(){
    vector<int> nums = {4, 5, 8, 2};
    KthLargest kthLargest(3, nums);
    assert(kthLargest.add(3) == 4);      // return 4  
    assert(kthLargest.add(5) == 5);      // return 5  
    assert(kthLargest.add(10) == 5);     // return 5  
    assert(kthLargest.add(9) == 8);      // return 8  
    assert(kthLargest.add(4) == 8);      // return 8  
    return 0;
}