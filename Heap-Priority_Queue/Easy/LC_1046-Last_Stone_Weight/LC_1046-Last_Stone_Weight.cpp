#include <bits/stdc++.h>

using namespace std;

// Heap/Priority Queue approach
// T: O(n log n), M: O(1)
// Where n is the length of stones list

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // Create stones max priority queue
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

int main() {
    vector<int> stones;
    int attempt, answer;

    // Example 1:
    stones = {2,7,4,1,8,1};
    attempt = Solution().lastStoneWeight(stones);
    answer = 1;
    assert(attempt == answer);
    // Example 2:
    stones = {1};
    attempt = Solution().lastStoneWeight(stones);
    answer = 1;
    assert(attempt == answer);
    // Test case 3:
    stones = {1, 1};
    attempt = Solution().lastStoneWeight(stones);
    answer = 0;
    assert(attempt == answer);
}