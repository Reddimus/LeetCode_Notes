import java.util.*;

// Graphs Adjacency Lists - Depth First Search (DFS) | Topological Sort approach
// T & M: O(n + p), where n = num of courses & p = num of prerequesites

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