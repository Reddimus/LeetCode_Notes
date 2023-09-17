#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    // T: O(n), M: O(1), where n is amount of steps
    int minCostClimbingStairs(vector<int>& cost) {
        // Bottom-up approach; start from 3rd step
        for (int i = 2; i < cost.size(); ++i) {
            cost[i] += min(cost[i - 1], cost[i - 2]);
        }
        return min(cost[cost.size() - 1], cost[cost.size() - 2]);
    }

    /*
    // T: O(n), M: O(1), where n is amount of steps
    int minCostClimbingStairs(vector<int>& cost) {
        // Top-down approach; start from 3rd to last step
        for (int i = cost.size() - 3; i >= 0; --i) {
            cost[i] += min(cost[i + 1], cost[i + 2]);
        }
        return min(cost[0], cost[1]);
    }
    */
};

int main() {
    Solution sol;
    vector<int> cost;

    // Ex 1
    cost = {10, 15, 20};
    assert(sol.minCostClimbingStairs(cost) == 15);
    // Ex 2
    cost = {1, 100, 1, 1, 1, 100, 1, 1, 100, 1};
    assert(sol.minCostClimbingStairs(cost) == 6);
}