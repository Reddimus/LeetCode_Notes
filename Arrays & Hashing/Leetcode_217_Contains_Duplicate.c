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

#include <stdbool.h>				// for boolean outputs
#include <assert.h>					// for testcases
#include <stdlib.h>					// for qsort
// Non-standard C libraries
#include "../c_headers/uthash.h" 	// for hashing

// Hash table approach

// create a data structure where we can quickly look up a value
// Note: hash_table could be initialized inside containsDuplicate function for leetcode opitmization
typedef struct {
	int key;
	UT_hash_handle hh; // Makes this structure hashable
} hash_table;

hash_table *hash = NULL, *elem, *tmp;

// T: O(n), O(n), where n is size of nums arr
bool containsDuplicate(int* nums, int numsSize){
	bool flag = false;
	// Iterate through arr to look up duplicate vals and append new vals
	for(int idx = 0; idx < numsSize; idx++){
		// search hashmap if num has been mapped to set
		HASH_FIND_INT(hash, &nums[idx], elem);
        if (elem){
            flag = true;
            break;
        }
        elem = malloc(sizeof(hash_table));
        elem->key = nums[idx];
        HASH_ADD_INT(hash, key, elem);
	}
	// Free up the hash table; this portion can be removed for leetcode opitmization
	HASH_ITER(hh, hash, elem, tmp) {
		HASH_DEL(hash, elem); 
		free(elem);
	}

	return flag;
}

/*
// Sorting approach

// Comparision function to be used in qsort
int compare(const void *a, const void *b){
	return (*(int*)a - *(int*)b);
}

// T: O(n log n), M: O(1), where n is size of nums arr
bool containsDuplicate(int* nums, int numsSize){
	// Quick Sort from descending to ascending order
	// qsort has the following args: *base(arr), nitems, size, compariter
	qsort(nums, numsSize, sizeof(int), compare);
	// Iterate through sorted array if there is a neighboring digit with the same value then there is a duplicate
	for(int idx = 0; idx < numsSize - 1; idx++){
		if (nums[idx] == nums[idx + 1])
			return true;
	}
	return false;
}
*/

/*
// Brute force approach
// T: O((n * (n-1))/ 2) = O(n^2), M: O(1), where n is size of nums arr
bool containsDuplicate(int* nums, int numsSize){
	for (int idx0 = 0; idx0 < numsSize; idx0++){
		for (int idx1 = idx0 + 1; idx1 < numsSize; idx1++){
			if (nums[idx0] == nums[idx1]){
				return true;
			}
		}
	}
	return false;
}
*/

int main(){
	int ex1[4] = {1, 2, 3, 1};
	int ex1Size = sizeof(ex1) / sizeof(ex1[0]);
	// sizeof(arr) gives you the total size of the array in bytes, and 
	// sizeof(arr[0]) gives you the size of one element in bytes. So, 
	// the division gives you the total number of elements in the array.
	assert(containsDuplicate(ex1, ex1Size) == true);
	// Ex2
	int ex2[4] = {1, 2, 3, 4};
	int ex2Size = sizeof(ex2) / sizeof(ex2[0]);
	assert(containsDuplicate(ex2, ex2Size) == false);
	// Ex3
	int ex3[] = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
	int ex3Size = sizeof(ex3)/sizeof(ex3[0]);
	assert(containsDuplicate(ex3, ex3Size) == true);
	// Ex4
	int ex4[1] = {1};
	int ex4Size = sizeof(ex4)/sizeof(ex4[0]);
	assert(containsDuplicate(ex4, ex4Size) == false);

	return 0;
}