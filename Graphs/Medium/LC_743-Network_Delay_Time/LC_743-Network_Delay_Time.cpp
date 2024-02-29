#include <bits/stdc++.h>

using namespace std;

// Adjacency list Graphs - Dijkstra's algorithm approach
// T: O(E log V) = O(E log N), M: O(V + E) = O(N + E)
// Where E is the number of edges and V/N is the number of vertices/nodes

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Create adjacency list based on sorce node -> weight & target node
        vector<vector<pair<int, int>>> adjList(n + 1);
        for (const vector<int>& t : times) {
            const int &ui = t[0], &vi = t[1], &wi = t[2];
            adjList[ui].push_back({wi, vi});
        }

        // Perform dijkstras algorithm to keep track of time passed
        int time = 0, unvisited = n + 2;
        vector<int> shortest(n + 1, unvisited);
        priority_queue<pair<int, int>, 
                        vector<pair<int, int>>, 
                        greater<pair<int, int>>> pq;
        pq.push({time, k});
        while (!pq.empty()) {
            int w1 = pq.top().first, n1 = pq.top().second;
            pq.pop();
            // If the node's shortest path has already been mapped
            if (shortest[n1] != unvisited) 
                continue;
            shortest[n1] = w1;
            time = w1;
            --n;    // Keep track of number of nodes visited

            for (const pair<int, int>& wn2 : adjList[n1]) {
                const int &w2 = wn2.first, &n2 = wn2.second;
                if (shortest[n2] == unvisited) 
                    pq.push({w1 + w2, n2});
            }
        }
        // If all nodes are reachable return the tracked time
        return (n <= 0) ? time : -1;
    }
};

int main() {
    vector<vector<int>> times;
    int attempt, answer;

    // Example 1:
    times = {{2,1,1},{2,3,1},{3,4,1}};
    attempt = Solution().networkDelayTime(times, 4, 2);
    answer = 2;
    assert(attempt == answer);
    // Example 2:
    times = {{1,2,1}};
    attempt = Solution().networkDelayTime(times, 2, 1);
    answer = 1;
    assert(attempt == answer);
    // Example 3:
    times = {{1,2,1}};
    attempt = Solution().networkDelayTime(times, 2, 2);
    answer = -1;
    assert(attempt == answer);
    // Test case 4:
    times = {{1,2,1},{2,3,2},{1,3,2}};
    attempt = Solution().networkDelayTime(times, 3, 1);
    answer = 2;
    assert(attempt == answer);
    // Test case 5:
    times = {{1,2,1},{2,3,7},{1,3,4},{2,1,2}};
    attempt = Solution().networkDelayTime(times, 4, 1);
    answer = -1;
    assert(attempt == answer);
    // Test case 6:
    times = {{1,5,66},{3,5,55},{4,3,29},{1,2,9},{3,4,10},{3,1,3},{2,3,78},{1,4,98},{4,5,21},{5,2,19},{5,1,76},{4,1,65},{3,2,27},{5,3,23},{5,4,12},{2,1,36},{4,2,75},{2,4,11},{1,3,30},{2,5,8}};
    attempt = Solution().networkDelayTime(times, 5, 1);
    answer = 30;
    assert(attempt == answer);
    // Test case 7:
    times = {{1,2,1},{2,3,7},{1,3,4},{2,1,2}};
    attempt = Solution().networkDelayTime(times, 3, 1);
    answer = 4;
    assert(attempt == answer);
    return 0;
}