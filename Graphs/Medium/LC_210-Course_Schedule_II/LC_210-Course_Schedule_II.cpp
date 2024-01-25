#include <bits/stdc++.h>

using namespace std;

// Graphs Adjacency Lists - Depth First Search (DFS) | Topological Sort approach
// T & M: O(n + p), where n = num of courses & p = num of prerequesites

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // map (key) courses -> (val) list of prerequisites
        unordered_map<int, vector<int>> prereqs;
        for (vector<int>& courseAndPrereq : prerequisites)
            prereqs[courseAndPrereq[0]].push_back(courseAndPrereq[1]);

        vector<char> visited(numCourses);
        vector<int> topOrder;
        // Recursively mark/check and append deepest valid courses
        function<bool(int)> dfs = [&](int course) -> bool {
            if (visited[course] == 'c') // if cycle found
                return false;
            if (visited[course] == 'v') // if course in top order answer
                return true;

            visited[course] = 'c';  // mark for cycle detection
            for (const int& prereq : prereqs[course])
                if (!dfs(prereq))
                    return false;
            
            // Recursively append deepest course that can be completed
            visited[course] = 'v';  // unmark cycle and mark course in answer
            topOrder.push_back(course);
            return true;
        };

        for (int course = 0; course < numCourses; ++course)
            if (!dfs(course))
                return {};
        return topOrder;
    }
};

int main() {

    return 0;
}