"""
https://leetcode.com/problems/implement-stack-using-queues/
Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue), as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
"""

# Using Two Queues :
# Time Complexity : push O(n) , pop O(1) , peek O(1)

class MyStack:

    def __init__(self):
        self.q1=[]
        self.q2=[]
        
    def push(self, x):
        self.q2.append(x)
        while len(self.q1)>0:
            self.q2.append(self.q1.pop(0))
        self.q1=self.q2
        self.q2=[]
        
    def pop(self):
        if not self.empty():
            return self.q1.pop(0)
       
    def top(self):
        if not self.empty():
            return self.q1[0]
            
    def empty(self):
        return len(self.q1)==0


obj = MyStack()
obj.push(1)
obj.push(2)
print("Popped :",obj.pop())
print("Top of Stack :",obj.top())
print("is empty ? :",obj.empty())


