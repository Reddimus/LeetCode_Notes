/*
Leetcode #217 - Contains Duplicate prompt:
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1, 2, 3, 1]
Output: true

Example 2:
Input: nums = [1, 2 ,3, 4]
Output: false

Example 3:
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
*/

// C++ Standard Library includes everything for competitive programming
// #include <bits/stdc++.h>

#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

class Solution {
public:
	// Hashset approach
	// T: O(n), M: O(n), where n is size of nums vector
	bool containsDuplicate(vector<int>& nums) {
		unordered_set<int> nums_set;
		for (int num : nums){
			if (nums_set.find(num) != nums_set.end())
				return true;
			nums_set.insert(num);
		}
		return false;
	}
	
	/*
	// Hashmap approach
	// T: O(n), M: O(n), where n is size of nums vector
	bool containsDuplicate(vector<int>& nums){
		unordered_map<int, int> nums_mp;
		for (int num : nums){
			nums_mp[num]++;
			if (nums_mp[num] >= 2)
				return true;
		}
		return false;
	}
	*/

	/*
	// Sorting approach
	// T: O(n log n), M: O(1), where n is size of nums vector
	bool containsDuplicate(vector<int>& nums){
		sort(nums.begin(), nums.end());
		for (int idx = 0; idx < nums.size() - 1; idx++){
			if (nums[idx] == nums[idx + 1])
				return true;
		}
		return false;
	}
	*/

	/*
	// Brute force approach
	// T: O((n * (n-1))/ 2) = O(n^2), M: O(1), where n is size of nums vector
	bool containsDuplicate(vector<int>& nums){
		for (int idx0 = 0; idx0 < nums.size() - 1; idx0++){
			for (int idx1 = idx0 + 1; idx1 < nums.size(); idx1++){
				if (nums[idx0] == nums[idx1]){
					return true;
				}
			}
		}
		return false;
	}
	*/
};

int main(){
	Solution s;
	// Ex 1
	vector<int> ex1 = {1, 2, 3, 1};
	assert(s.containsDuplicate(ex1) == true);
	// Ex 2
	vector<int> ex2 = {1, 2, 3, 4};
	assert(s.containsDuplicate(ex2) == false);
	// Ex 3
	vector<int> ex3 = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
	assert(s.containsDuplicate(ex3) == true);
	// Ex 4
	vector<int> ex4 = {1};
	assert(s.containsDuplicate(ex4) == false);

	return 0;
}
