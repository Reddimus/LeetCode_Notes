// #include <bits/stdc++.h>
#include <vector>
#include <iostream>
#include <cassert>

using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
	// Iterative solution
	// T: O(n), M: O(1), where n is size of linked list input
	ListNode* reverseList(ListNode* head) {
		ListNode *prev = NULL;
		ListNode *curr = head;

		while (curr) {
			ListNode *temp = curr->next;
			curr->next = prev;
			prev = curr;
			curr = temp;
		}
		return prev;
	}

	/*
	// Recursive solution
	// T & M: O(n), where n is size of linked list input
	ListNode* reverseList(ListNode* head) {
		if (!head || !head->next)
			return head;	// return NULL

		ListNode *newHead = reverseList(head->next);	// recursively call to the end
		head->next->next = head;	// point the next node back to the current node
		head->next = NULL;	// disconnect the current node

		return newHead;
	}
	*/

};

void testCase(ListNode *head, vector<int> ans) {
	vector<int> attempt;
	ListNode *curr = Solution().reverseList(head);
	while (curr) {
		attempt.push_back(curr->val);
		curr = curr->next;
	}
	// print attempt vector
	cout << "Attempt: ";
	for (int i = 0; i < attempt.size(); i++) {
		cout << attempt[i] << " ";
	}
	cout << endl;

	// print ans vector
	cout << "Ans: ";
	for (int i = 0; i < ans.size(); i++) {
		cout << ans[i] << " ";
	}
	cout << endl << endl;
	
	assert(attempt == ans);
}

int main() {
	ListNode *head;
	vector<int> ans;

	// Example 1
	head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
	ans = {5, 4, 3, 2, 1};
	testCase(head, ans);
	// Example 2
	head = new ListNode(1, new ListNode(2));
	ans = {2, 1};
	testCase(head, ans);
	// Example 3
	head = nullptr;
	ans = {};
	testCase(head, ans);

	return 0;
}