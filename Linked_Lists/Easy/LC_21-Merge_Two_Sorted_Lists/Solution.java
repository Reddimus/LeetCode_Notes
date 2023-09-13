import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    // T: O(n + m), M: O(1), where n and m are the lengths of list1 and list2
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode();
        ListNode tail = dummy;

        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                tail.next = list1;
                list1 = list1.next;
            }
            else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }

        // Link remaining list to new Sorted list
        if (list1 != null)
            tail.next = list1;
        else if (list2 != null)
            tail.next = list2;
        
        return dummy.next;
    }
}

class TestCases {
    public static void assertMergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head1 = list1, head2 = list2;
        ArrayList<Integer> answer = new ArrayList<Integer>();
        while (list1 != null) {
            answer.add(list1.val);
            list1 = list1.next;
        }
        while (list2 != null) {
            answer.add(list2.val);
            list2 = list2.next;
        }
        Collections.sort(answer);

        // Reset list1 and list2
        list1 = head1;
        list2 = head2;

        ArrayList<Integer> attempt = new ArrayList<Integer>();
        ListNode mergedList = new Solution().mergeTwoLists(list1, list2);
        while (mergedList != null) {
            attempt.add(mergedList.val);
            mergedList = mergedList.next;
        }

        System.out.println("Attempt: " + attempt);
        System.out.println("Answer: " + answer + "\n");
        assert answer.equals(attempt);
    }

    public static void main(String[] args) {
        // Run test cases
        // Compile:     javac Solution.java
        // Run:         java -ea TestCases
        ListNode list1, list2;
        // Example 1
        list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
        list2 = new ListNode(1, new ListNode(3, new ListNode(4)));
        assertMergeTwoLists(list1, list2);
        // Example 2
        list1 = null;
        list2 = null;
        assertMergeTwoLists(list1, list2);
        // Example 3
        list1 = null;
        list2 = new ListNode(0);
        assertMergeTwoLists(list1, list2);
    }
}