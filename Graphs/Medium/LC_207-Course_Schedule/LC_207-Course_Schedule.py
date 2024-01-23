# Graphs Adjacency Lists - Depth First Search (DFS) | Topological Sort approach
# T & M: O(n + p), where n = num of courses & p = num of prerequesites

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

# Example 1:
attempt = Solution().canFinish(numCourses=2, prerequisites=[[1,0]])
answer = True
assert attempt == answer, f"Expected {answer} but got {attempt}"

# Example 2:
attempt = Solution().canFinish(numCourses=2, prerequisites=[[1,0],[0,1]])
answer = False
assert attempt == answer, f"Expected {answer} but got {attempt}"

# Test Case 3:
attempt = Solution().canFinish(5, [[1,0],[2,1],[3,2],[4,3]])
answer = True
assert attempt == answer, f"Expected {answer} but got {attempt}"