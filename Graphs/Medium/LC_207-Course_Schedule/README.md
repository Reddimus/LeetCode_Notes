# [LeetCode #207 - Course Schedule](https://leetcode.com/problems/course-schedule/)

**Difficulty: `Medium`**

---

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array prerequisites where` prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

---

**Example 1:**  
Input:
```
numCourses = 2, prerequisites = [[1,0]]
```
Output:
```
true
```
Explanation: THere are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

**Example 2:**  
Input:
```
numCourses = 2, prerequisites = [[1,0],[0,1]]
```
Output:
```
false
```
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

**Constraints:**
- `1 <= numCourses <= 10^5`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- All the pairs prerequisites[i] are **unique**.

---

### Hints:
- **Check for Cycles**: In your search algorithm to check if a course path can finish, make sure to keep track of the courses you've visited to avoid repeated work. If you visit a course that is already in the path, then you know there's a cycle and the path is invalid.
- **Optimize search with Path Elimination**: In your search algorithm, prioritize exploring deepest valid course first. Once a course's prerequisites are validated, remove it from the path. This approach minimizes repeated checks and efficiently confirms path completion.

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Graphs/Medium/LC_207-Course_Schedule)

### Graphs Adjacency Lists - Depth First Search (DFS) | Topological Sort approach

#### Intuition
In solving the course schedule problem, we aim to determine if all courses can be completed without encountering any cyclic dependencies in the prerequisites. The core of our approach lies in building an adjacency list that maps each course to its list of prerequisites, which represents the graph structure of course dependencies. We then use Depth First Search (DFS) to traverse this graph. The key aspect of our DFS is to mark courses as seen during traversal to detect cycles - if we revisit a course already marked as seen, it indicates a cycle, and hence, the course path cannot be completed. After validating a course's prerequisites, we remove it from the adjacency list, effectively reducing the graph's size and making subsequent searches more efficient. This strategy allows us to explore the graph deeply, eliminating valid paths and quickly identifying any cyclic dependencies. Our goal is to iterate through each course and confirm that a path exists from it to all its prerequisites without encountering cycles. If we can do this for all courses, then it's possible to finish the course schedule; otherwise, it's impossible. This method not only checks course completion feasibility but also optimizes the search process by focusing on the deepest courses first and removing them once validated, preventing redundant checks.

#### Steps:
1. **Build adjacency list**:
	- Map each course to a list of its prerequisites
	- `Key = course`
	- `Value = list of prerequisites`
2. **Create Depth First Search (DFS) function to mark and check if course path can be completed**:
	- `dfs(course)`
		- If `course` is already marked as seen, return `false` (infinite loop found)
		- If `course` does not have any prerequisites, return `true` (course path can be completed)
		- Mark `course` as seen
		- For each `prereq` in `course`'s prerequisites:
			- If `dfs(prereq)` returns `false`, return `false` (course path cannot be completed)
		- Remove `course` from `prereqs` map
		- Return `true` (course path can be completed)
3. **Iterate through each course in `prereqs` map**:
	- If `dfs(course)` returns `false`, return `false` (course path cannot be completed)
4. **Return `true` (course path can be completed)**

#### Complexity Analysis
- **Time Complexity:** `O(N + P)`  
- **Space Complexity:** `O(N + P)`

Where `N` is the number of courses and `P` is the number of prerequisites.

#### Python Code
```python
class Solution:
	def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
		prereqs = {}	# map (key) courses -> (val) list of prerequisites
		for course, prereq in prerequisites:
			prereqs[course] = prereqs.get(course, []) + [prereq]

		seen = set()
		# Recursively mark and check if course path can be completed
		def dfs(course: int) -> bool:
			if course in seen:
				return False	# Infinite loop found
			if course not in prereqs:
				return True		# Course does not have prerequisite
			
			seen.add(course)
			for prereq in prereqs[course]:
				if not dfs(prereq):
					return False
			
			# Recursively remove deepest valid course
			seen.remove(course)
			del prereqs[course]
			return True
			
		for course in list(prereqs.keys()):
			if not dfs(course):
				return False
		return True
```

#### C++ Code
```cpp
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
```

#### Java Code
```java
class Solution {
    private Map<Integer, ArrayList<Integer>> prereqs = new HashMap<>();
    private Set<Integer> visited = new HashSet<>();

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // map (key) courses -> (val) list of prerequesites
        for (int[] crsPre : prerequisites) {
            prereqs.putIfAbsent(crsPre[0], new ArrayList<>());
            prereqs.get(crsPre[0]).add(crsPre[1]);
        }

        for (int course = 0; course < numCourses; ++course)
            if (!dfs(course))
                return false;
        return true;
    }

    // Recursively mark and check if course path can be completed
    private boolean dfs(int course) {
        if (visited.contains(course))
            return false;   // Infinite loop found
        if (!prereqs.containsKey(course))
            return true;    // Course does not have prerequisite

        visited.add(course);
        for (int pre : prereqs.get(course)) {
            if (!dfs(pre))
                return false;
        }

        // Recursively remove deepest valid course
        visited.remove(course);
        prereqs.remove(course);
        return true;
    }
}
```