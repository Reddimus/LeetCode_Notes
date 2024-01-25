#include <bits/stdc++.h>

using namespace std;

// Graphs Adjacency Lists - Depth First Search (DFS) | Topological Sort approach
// T & M: O(n + p), where n = num of courses & p = num of prerequesites

class Solution {
public:
	bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
		// map (key) courses -> (val) list of prerequisites
		unordered_map<int, vector<int>> prereqs;
		for (vector<int>& courseAndPrereq : prerequisites)
			prereqs[courseAndPrereq[0]].push_back(courseAndPrereq[1]);
		
		unordered_set<int> seen;
		// Recursively mark and check if course path can be completed
		function<bool(int)> dfs = [&](int course) -> bool {
			if (seen.find(course) != seen.end())
				return false;	// Infinite loop found
			if (prereqs.find(course) == prereqs.end())
				return true;	// Course does not have prerequisite

			seen.insert(course);
			for (int& prereq : prereqs[course])
				if (!dfs(prereq))
					return false;

			// Recursively remove deepest valid course
			seen.erase(course);
			prereqs.erase(course);
			return true;
		};

		for (int course = 0; course < numCourses; ++course)
			if (!dfs(course))
				return false;
		return true;
	}
};

int main() {
	vector<vector<int>> prerequisites;
	bool attempt;

	// Example 1:
	prerequisites = {{1,0}};
	attempt = Solution().canFinish(2, prerequisites); 
	assert(attempt == true);
	// Example 2:
	prerequisites = {{1,0},{0,1}};
	attempt = Solution().canFinish(2, prerequisites);
	assert(attempt == false);
	// Test Case 3:
	prerequisites = {{1,0},{2,0},{3,1},{3,2}};
	attempt = Solution().canFinish(4, prerequisites);
	assert(attempt == true);

	return 0;
}