class ListNode {
	int val;
	ListNode next;
	ListNode() {}
	ListNode(int val) { this.val = val; }
	ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
	// Iterative solution
	// T: O(n), M: O(1), where n is size of linked list input
	public ListNode reverseList(ListNode head) {
		ListNode prev = null, curr = head;

		while (curr != null) {
			ListNode temp = curr.next;
			curr.next = prev;
			prev = curr;
			curr = temp;
		}

		return prev;
	}
	
	/*
	// Recursive solution
	// T & M: O(n), where n is size of linked list input
	public ListNode reverseList(ListNode head) {
		if (head == null || head.next == null)
			return head;
		
		ListNode newHead = reverseList(head.next);	// recursively call to the end
		head.next.next = head;	// point the next node back to the current node
		head.next = null;	// disconnect the current node
		
		return newHead;
	}
	*/
}

class TestCases {
	static void assertLinkedList(ListNode head, ListNode expectedHead) {
		ListNode curr = head, expectedCurr = expectedHead;
		while (curr != null && expectedCurr != null) {
			assert curr.val == expectedCurr.val;
			curr = curr.next;
			expectedCurr = expectedCurr.next;
		}
	}
	public static void main(String[] args) {
		// Run test cases
		// Compile:     javac Solution.java
		// Run:         java -ea TestCases
		ListNode head, expectedHead;
		// Example 1
		head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
		expectedHead = new ListNode(5, new ListNode(4, new ListNode(3, new ListNode(2, new ListNode(1)))));
		assertLinkedList(new Solution().reverseList(head), expectedHead);
		// Example 2
		head = new ListNode(1, new ListNode(2));
		expectedHead = new ListNode(2, new ListNode(1));
		assertLinkedList(new Solution().reverseList(head), expectedHead);
		// Example 3
		head = null;
		expectedHead = null;
		assertLinkedList(new Solution().reverseList(head), expectedHead);
	}
}