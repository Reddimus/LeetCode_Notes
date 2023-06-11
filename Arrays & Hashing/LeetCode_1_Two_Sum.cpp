/*
Leetcode #1 - Two sum prompt:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums [0] + nums [1] == 9, we return [0, 1].

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Example 3:
Input: nums = [3, 3], target = 6
Output: [0, 1]

Constraints:
• 2 <= nums.length <= 10^4
• -10^9 <= nums [i] <= 10^9
• -10^9 <= target <= 10^9
• Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
*/

#include <iostream>
#include <vector>
#include <cassert>
#include <unordered_map>

using namespace std;

class Solution{
public:
    // Difference/Hash map method
    // T: O(n), M: O(n), where n is size of nums
    vector<int> twoSum(vector<int>& nums, int target){
        unordered_map<int, int> prev;
        // map nums into hashmap and check if current diff was mapped prev
        for (int idx = 0; idx < nums.size(); idx++){
            int diff = target - nums[idx];
            if (prev.find(diff) != prev.end())
                return {idx, prev[diff]};
            prev[nums[idx]] = idx;
        }
        return {-1, -1};    // error
    }
    /*
    // Brute force method
    // T: O(n^2), M: O(1), where n is size of nums vector
    vector<int> twoSum(vector<int> nums, int target){
        // Check every possible combinations with overlap
        for (int idx0 = 0; idx0 < nums.size() - 1; idx0++){
            for (int idx1 = idx0 + 1; idx1 < nums.size(); idx1++){
                if (nums[idx0] + nums[idx1] == target)
                    return {idx0, idx1};
            }
        }
        return {-1, -1};    // error
    }
    */
};

int main(){
    Solution s;
    
    // Ex1
    vector<int> nums0 = {2, 7, 11, 15}; 
    int target0 = 9;
    vector<int> ans0 = {0, 1}, inv_ans0 = {1, 0};
    vector<int> attempt0 = s.twoSum(nums0, target0);
    assert((attempt0 == ans0) || (attempt0 == inv_ans0));
    // Ex2
    vector<int> nums1 = {3, 2, 4};
    int target1 = 6;
    vector<int> ans1 = {1, 2}, inv_ans1 = {2, 1};
    vector<int> attempt1 = s.twoSum(nums1, target1);
    assert((attempt1 == ans1) || (attempt1 == inv_ans1));
    // Ex3
    vector<int> nums2 = {3, 3};
    int target2 = 6;
    vector<int> ans2 = {0, 1}, inv_ans2 = {1, 0};
    vector<int> attempt2 = s.twoSum(nums2, target2);
    assert((attempt2 == ans2) || (attempt2 == inv_ans2));

    return 0;
}