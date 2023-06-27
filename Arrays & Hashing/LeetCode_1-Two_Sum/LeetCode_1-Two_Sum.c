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

#include <stdio.h>      // NULL
#include <stdlib.h>     // calloc()
#include <assert.h>     // testcases
#include <uthash.h>     // hashmaps

typedef struct {
    int key;
    int val;

    UT_hash_handle hh; // Makes this structure hashable
} hash_table;

hash_table *hash = NULL, *elem, *tmp;

// Difference/Hashmap approach
// T: O(n), M: O(n), where n is size of nums
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int* indices = calloc((*returnSize = 2), sizeof(int));
    for (int idx = 0; idx < numsSize; idx++){
        int diff = target - nums[idx];
        HASH_FIND_INT(hash, &diff, elem);
        if (elem){
            indices[0] = idx, indices[1] = elem->val;
            break;
        }

        elem = malloc(sizeof(hash_table));
        elem->key = nums[idx];
        elem->val = idx;
        HASH_ADD_INT(hash, key, elem);
    }

    // Free up the hash table; this portion can be removed for leetcode opitmization
    HASH_ITER(hh, hash, elem, tmp) {
        HASH_DEL(hash, elem); 
        free(elem);
    }
    return indices;
}

/*
// Brute force method
// T: O(n^2), M: O(1), where n is size of nums
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int* indices = calloc((*returnSize = 2), sizeof(int));
    for (int idx0 = 0; idx0 < numsSize - 1; idx0++){
        for (int idx1 = idx0 + 1; idx1 < numsSize; idx1++){
            if (target == nums[idx0] + nums[idx1]){
                indices[0] = idx0, indices[1] = idx1;
                return indices;
            }
        }
    }
    // Error
    return NULL;
}
*/

void assertArr(int* arr0, int* arr1, int len){
    // sort both arrs
    if (len == 2){
        if (arr0[0] > arr0[1]){
            int tmp = arr0[0];
            arr0[0] = arr0[1];
            arr0[1] = tmp;
        }
        if (arr1[0] > arr1[1]){
            int tmp = arr1[0];
            arr1[0] = arr1[1];
            arr1[1] = tmp;
        }
    }
    // Compare each element iteratevly
    for (int idx = 0; idx < len; idx++)
        assert(arr0[idx] == arr1[idx]);
}

int main(){
    // Ex1
    // Input
    int nums1[4] = {2, 7, 11, 15};
    int numsSize1 = 4, target1 = 9, returnSize1;
    // Expected output(s)
    int ans1[2] = {0, 1};
    // output
    int* attempt1 = twoSum(nums1, numsSize1, target1, &returnSize1);
    // Test
    assertArr(attempt1, ans1, returnSize1);

    // Ex2
    // Input
    int nums2[3] = {3, 2, 4};
    int numsSize2 = 3, target2 = 6, returnSize2;
    // Expected output(s)
    int ans2[2] = {1, 2};
    // output
    int* attempt2 = twoSum(nums2, numsSize2, target2, &returnSize2);
    // Test
    assertArr(attempt2, ans2, returnSize2);

    // Ex3
    // Input
    int nums3[2] = {3, 3};
    int numsSize3 = 2, target3 = 6, returnSize3;
    // Expected output(s)
    int ans3[2] = {0, 1};
    // output
    int* attempt3 = twoSum(nums3, numsSize3, target3, &returnSize3);
    // Test
    assertArr(attempt3, ans3, returnSize3);
}
