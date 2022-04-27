"""
Q-1 ) Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/
(7.5 marks)
(Easy)
Implement a first in first out (FIFO) queue using only two stacks. The
implemented queue should support all the functions of a normal queue (push,
peek, pop, and empty).
Implement the MyQueue class:
● void push(int x) Pushes element x to the back of the queue.
● int pop() Removes the element from the front of the queue and returns it.
● int peek() Returns the element at the front of the queue.
● boolean empty() Returns true if the queue is empty, false otherwise.
Notes:
● You must use only standard operations of a stack, which means only push
to top, peek/pop from top, size, and is empty operations are valid.
● Depending on your language, the stack may not be supported natively. You
may simulate a stack using a list or deque (double-ended queue) as long
as you use only a stack's standard operations.
Follow-up: Can you implement the queue such that each operation is amortized
O(1) time complexity? In other words, performing n operations will take overall
O(n) time even if one of those operations may take longer.
Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]
Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
"""


# Implementing Queue Using Two Stacks :
# Time Complexity : push O(1) , pop Amortized O(1)
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if self.peek() is not None:
            return self.s2.pop()

    def peek(self):
        if not self.empty():
            if len(self.s2) == 0:
                while len(self.s1) != 0:
                    self.s2.append(self.s1.pop())
            return self.s2[-1]

    def empty(self):
        return len(self.s1) == 0 and len(self.s2) == 0


obj = MyQueue()
obj.push(5)
obj.push(6)
obj.push(1)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.peek())
print(obj.empty())
