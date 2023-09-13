// #include <bits/stdc++.h>
#include <vector>
#include <cassert>
#include <algorithm>
#include <iostream>

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
    // T: O(n), M: O(1), where n is size of biggest linked list input
    ListNode* mergeTwoLists(ListNode *list1, ListNode *list2) {
        ListNode *dummy = new ListNode();
        ListNode *tail = dummy;

        while (list1 && list2) {
            if (list1->val < list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            tail = tail->next;
        }

        // Link remaining list to prev
        if (list1)
            tail->next = list1;
        else if (list2)
            tail->next = list2;
        
        return dummy->next;
    }
};

void assertMergeTwoLists(ListNode *list1, ListNode *list2) {
    vector<int> answer;
    ListNode *head1 = list1, *head2 = list2;
    while (list1) {
        answer.push_back(list1->val);
        list1 = list1->next;
    }
    while (list2) {
        answer.push_back(list2->val);
        list2 = list2->next;
    }
    sort(answer.begin(), answer.end());

    // reset list1 and list2 pointers
    list1 = head1;
    list2 = head2;

    vector<int> attempt;
    ListNode *mergedLists = Solution().mergeTwoLists(list1, list2);
    while (mergedLists) {
        attempt.push_back(mergedLists->val);
        mergedLists = mergedLists->next;
    }

    cout << "Attempt: ";
    for (auto i : attempt)
        cout << i << " ";
    cout << endl;
    cout << "Answer: ";
    for (auto i : answer)
        cout << i << " ";
    cout << endl;
    assert(attempt == answer);
}

int main() {
    ListNode *list1 = nullptr, *list2 = nullptr;
    // Ex1
    list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
    list2 = new ListNode(1, new ListNode(3, new ListNode(4)));
    assertMergeTwoLists(list1, list2);
    // Ex2
    list1 = new ListNode();
    list2 = new ListNode();
    assertMergeTwoLists(list1, list2);
    // Ex3
    list1 = new ListNode();
    list2 = new ListNode(0);
    assertMergeTwoLists(list1, list2);

    return 0;
}