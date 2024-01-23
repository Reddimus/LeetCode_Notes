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
- 

# [Solutions](https://github.com/Reddimus/LeetCode_Notes/tree/main/Graphs/Medium/LC_207-Course_Schedule)

### Graphs Adjacency Lists - Depth First Search (DFS) | Topological Sort approach

#### Intuition

#### Steps:
1.

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
```

#### Java Code
```java
```