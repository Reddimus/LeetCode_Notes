'''
LeetCode #1700 - Number of Students Unable to Eat Lunch prompt:

The school cafeteria offers circular and square sandwiches at lunch break, 
referred to by numbers 0 and 1 respectively. All students stand in a queue. 
Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. 
The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of 
the stack, they will take it and leave the queue.

Otherwise, they will leave it and go to the queue's end.

This continues until none of the queue students want to take the top sandwich 
and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] 
is the type of the i^th sandwich in the stack (i = 0 is the top of the stack) 
and students[j] is the preference of the j^th student in the initial queue 
(j = 0 is the front of the queue). Return the number of students that are 
unable to eat.

Example 1:
Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.

Example 2:
Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Explanation: 
students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
students = [1,1,0,0,1], sandwiches = [0,0,0,1,1]
students = [1,0,0,1,1], sandwiches = [0,0,0,1,1]
students = [0,0,1,1,1], sandwiches = [0,0,0,1,1]
students = [0,1,1,1], sandwiches = [0,0,1,1]
students = [1,1,1], sandwiches = [0,1,1]
Output: 3

Constraints:
1 <= students.length, sandwiches.length <= 100
students.length == sandwiches.length
sandwiches[i] is 0 or 1.
students[i] is 0 or 1.
'''
class ListNode:
	def __init__(self, val = 0):
		self.val = val
		self.next = None

class Solution:
	# Time complexity: 	O(4n) = O(n)
	# Space complexity: O(n)
	def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
		# convert both lists into linked list
		stu_dummy, sand_dummy = ListNode(), ListNode()	# left node dummy
		stu_tail, sand_tail = stu_dummy, sand_dummy
		for student, sandwich in zip(students, sandwiches):
			stu_tail.next, sand_tail.next = ListNode(student), ListNode(sandwich)
			stu_tail, sand_tail = stu_tail.next, sand_tail.next
		# queue students and sandwhiches Linked Lists
		stu_curr, sand_curr = stu_dummy.next, sand_dummy.next
		max_repeats = 0
		while stu_curr or sand_curr:
			if stu_curr.val != sand_curr.val and max_repeats != len(students):
				stu_tail.next = stu_curr 	# point tail to new tail
				stu_tail = stu_curr			# store new tail
				stu_curr = stu_curr.next	# increment curr to store new head
				stu_tail.next = None		# point tail to null
				max_repeats += 1
			elif stu_curr.val == sand_curr.val and max_repeats != len(students):
				stu_prev, sand_prev = stu_curr, sand_curr	# store soon to be removed nodes
				stu_curr, sand_curr = stu_curr.next, sand_curr.next	# update current
				stu_prev.next, sand_prev.next = None, None 	# disconnect prev head nodes
				max_repeats = 0
			else:	# max_repeats reached
				len_stu = 0
				while stu_curr:
					stu_curr = stu_curr.next
					len_stu += 1
				return len_stu
		return 0

# Ex 1:
assert Solution().countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1]) == 0

# Ex 2:
assert Solution().countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]) == 3
