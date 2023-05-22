'''
Location of data after transfers
X stores its data on different servers at different locations. From time to time, due to several 
factors, X needs to move its data from one location to another. This challenge involved keeping 
track of the locations of X's data and report them at the end of the year.

At the start of the year, X's data was located at n different locations. Over the course of the 
year, X's data was moved from one server to another m times. Precisely, in the ith operation, 
the data was moved from movedFrom[i] to movedTo[i]. Find the locations of the data after all m 
moving operations. Return the locations in ascending order.

Note: It is guaranteed that for any movement of data :

• There is data at movedFrom[i].
• There is no data at movedTo[i].

Example:
locations = [1, 7, 6, 8]

movedFrom = [1, 7, 2]

movedTo = [2, 9, 5]

Data begins at locations listed in locations. Over the course of the year, the data was moved 
three times.

Data was first moved from movedFrom[0] to movedTo[0], from 1 to 2. Next, it is moved from 7 
to 9, and finally from location 2 to 5.

In the end, the locations where data is present are [5,6,8,9] in ascending order.

**Input Format For Custom Testing **

The first line contains n, the number of elements in locations[].

Each line i of the n subsequent lines (where 0 <= i < n) contains an integer, locations[i].

The next line contains m, the number of elements in movedFrom[].

Each line I of the m subsequent lines (where 0 <= i < m) contains an integer, movedFrom[i].

The next line contains m, the number of elements in movedTo[].

Each line i of the m subsequent lines (where 0 <= i < m) contains an integer, movedTo[i].

Return:
int[] : the locations storing data after all moves are made, in ascending order.

Test Cases:
Input: locations=[1,5,2,6] , movedFrom=[1,4,5,7] , movedTo=[4,7,1,3]
Output: [1,2,3,6]

Input: locations=[1,2,3] , movedFrom=[1,2] , movedTo=[5,6]
Output: [3,5,6]
'''

# Time complexity:  O(n) + O(m log m) = O(m log m), where m is the # of iters in each location swap
# Space complexity: O(n), where n is length of locations
class Solution:
    def findDataLocations(self, locations: list[int], movedFrom: list[int], movedTo: list[int]) -> list[int]:
        # append idxs and nums to dictionary
        loc_map = {}
        for idx, num in enumerate(locations):
            loc_map[num] = idx
        # iterate through the tasks (location swaps)
        for from_num, to_num in zip(movedFrom, movedTo):
            if from_num in loc_map:
                # swap locations
                loc_idx = loc_map[from_num]
                locations[loc_idx] = to_num
                # update map
                loc_map[to_num] = loc_idx
                del loc_map[from_num]
        locations.sort()
        return locations

# Example 1:
assert Solution().findDataLocations([1, 7, 6, 8], [1, 7, 2], [2, 9, 5]) == [5,6,8,9], f"Expected {[5,6,8,9]}, but got {Solution().findDataLocations([1, 7, 6, 8], [1, 7, 2], [2, 9, 5])}"

# Example 2:
assert Solution().findDataLocations([1,5,2,6], [1,4,5,7], [4,7,1,3]) == [1,2,3,6], f"Expected {[1,2,3,6]}, but got {Solution().findDataLocations([1,5,2,6], [1,4,5,7], [4,7,1,3])}"

# Example 3:
assert Solution().findDataLocations([1,2,3], [1,2], [5,6]) == [3,5,6], f"Expected {[3,5,6]}, but got {Solution().findDataLocations([1,2,3], [1,2], [5,6])}"
