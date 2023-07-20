/*
LeetCode #303 - Range Sum Query-Immutable prompt:

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right 
inclusive where left <= right.

Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between 
indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3


Constraints:
1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.
*/

#include <vector>
#include <cassert>
#include <string>

using namespace std;

class NumArray{
public:
    // initiliaze prefix array of nums with dummy value @ idx 0
    vector<int> prefix_nums = {NULL};
    // T: O(n), M: O(n), where n is size of nums
    NumArray(vector<int>& nums){
        int curr = 0;
        for (int num : nums){
            curr += num;
            prefix_nums.push_back(curr);
        }
    }
    // T: O(1), M: O(1)
    int sumRange(int left, int right){
        return prefix_nums[right + 1] - prefix_nums[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */

int main(){
    // Ex1
    vector<int> nums = {-2, 0, 3, -5, 2, -1};
    NumArray numArr = NumArray(nums);
    int attempt;
    assert(numArr.sumRange(0, 2) == 1); 
    assert(numArr.sumRange(2, 5) == -1);
    assert(numArr.sumRange(0, 5) == -3);
}