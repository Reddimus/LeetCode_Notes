'''
LeetCode #225 - Implement Stack using Queues prompt:

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support 
all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from 
front, size and is empty operations are valid.

Depending on your language, the queue may not be supported natively. You may simulate a queue using 
a list or deque (double-ended queue) as long as you use only a queue's standard operations.

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], 		[1], 	[2], 	[], 	[], 	[]]

Output
[null, 		null, 	null, 	2, 		2, 		false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
 

Follow-up: Can you implement the stack using only one queue?
'''
from collections import deque
# last-in-first-out (LIFO)
class MyStack:
	def __init__(self):
		self.q = deque()	# used as a normal queue

	def push(self, x: int) -> None:	# Pushes element x to the top of the stack.
		self.q.append(x)

	# Time complexity: O(n)
	def pop(self) -> int:	# Removes the element on the top of the stack and returns it.
		for i in range(len(self.q) - 1):	# keeps requeueing until top is reached
			self.push(self.q.popleft())		# pops bottom and pushes that bottom to top
		return self.q.popleft()

	# Time complexity: O(n)
	def top(self) -> int:	# Returns the element on the top of the stack.
		for i in range(len(self.q) - 1):	# keeps requeueing until top is reached
			self.push(self.q.popleft())
		top = self.q[0]
		self.push(self.q.popleft())	# push top to top
		return top

	def empty(self) -> bool:	# Returns true if the stack is empty, false otherwise.
		return len(self.q) == 0

	'''
class ListNode:
	def __init__(self, val = 0):
		self.val = val
		self.prev = None

class MyStack:
	def __init__(self):
		self.dummy = ListNode(0)	# right dummy

	def push(self, x: int):	# Pushes element x to the top of the stack.
		dummy = self.dummy
		top = ListNode(x)
		# if stack has top already
		if dummy.prev:
			prev_top = dummy.prev
			dummy.prev = top
			top.prev = prev_top
		else:
			dummy.prev = top
			top.prev = None

	def pop(self) -> int or None: 	# Removes the element on the top of the stack and returns it.
		dummy = self.dummy
		if dummy.prev: 		# if top exists
			top = dummy.prev
			if top.prev: 			# if node exists below top
				new_top = top.prev 	# assign new top
				dummy.prev = new_top
			else:
				dummy.prev = None
			top.prev = None
			return top.val
		return None

	def top(self) -> int or None: 	# Returns the element on the top of the stack.
		dummy = self.dummy
		if dummy.prev:
			return dummy.prev.val
		return None

	def empty(self) -> bool:	# Returns true if the stack is empty, false otherwise.
		dummy = self.dummy
		if dummy.prev:
			return False
		return True
	'''

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# Ex 1:
myStack = MyStack()
myStack.push(1)
myStack.push(2)
assert myStack.top() == 2
assert myStack.pop() == 2
assert myStack.empty() == False

# Test case 2:
myStack = MyStack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
assert myStack.top() == 3
