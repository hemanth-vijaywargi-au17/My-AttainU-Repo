# Stack Using One Queue :
# Time Complexity : push O(n) , pop O(1) , peek O(1)
# Space Complexity is Less than the Two Queue Method.

class MyStack:

    def __init__(self):
        self.q=[]
        
        
    def push(self, x):
       self.q.append(x)
       for i in range(len(self.q)-1):
           self.q.append(self.q.pop(0))
        
        
    def pop(self):
        if not self.empty():
            return self.q.pop(0)
       
    def top(self):
        if not self.empty():
            return self.q[0]
            
    def empty(self):
        return len(self.q)==0


obj1 = MyStack()
obj1.push(3)
obj1.push(4)
print("Popped :",obj1.pop())
print("Top of Stack :",obj1.top())
print("Popped :",obj1.pop())
print("is empty ? :",obj1.empty())
