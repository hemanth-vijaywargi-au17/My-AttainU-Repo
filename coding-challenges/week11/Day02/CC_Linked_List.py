class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None

    def addNodetoEnd(self,x):
        if self.head is None:
            self.head=Node(x)
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=Node(x)
            
    def addNodetoBegin(self,x):
        if self.head is None:
            self.head=Node(x)
        else:
            new_node=Node(x)
            new_node.next=self.head
            self.head=new_node
            
    def removeNodeEnd(self):
        if self.head is None:
            print("LL is already Empty")
        elif self.head.next is None:
            self.head=None
        else:
            cur=self.head
            while cur.next.next != None:
                cur=cur.next
            cur.next=None
            
    def removeNodeBegin(self):
        if self.head is None:
            print("LL is already Empty")
        else:
            self.head=self.head.next
        
    def printLL(self):
        if self.head is None:
            print("LL is Empty")
        else:
            cur=self.head
            while cur!=None:
                print(cur.data,end="  ")
                cur=cur.next
        print()




"""
Q-1 ) Write a program to remove first node from a linked list:
(5 marks)
(Super Easy)
Example 1:
Input(elements in linked list)
2
5
6
8
3
Output(elements after removing head of the linked list)
5
6
8
3
"""

print("Q1) Removing Head of the Linked List")

LL1=Linked_List()

LL1.addNodetoEnd(2)
LL1.addNodetoEnd(5)
LL1.addNodetoEnd(6)
LL1.addNodetoEnd(8)
LL1.addNodetoEnd(3)
LL1.printLL()

LL1.removeNodeBegin()
LL1.printLL()



"""
Q-2 ) Convert Binary Number in a Linked List to Integer: (5 marks)
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
(Easy)
Given head which is a reference node to a singly-linked list. The value of each
node in the linked list is either 0 or 1. The linked list holds the binary
representation of a number.
Return the decimal value of the number in the linked list.
Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

"""

print("Q2) Convert Binary Number in a Linked List to Decimal :")

LL2=Linked_List()
LL2.addNodetoEnd(1)
LL2.addNodetoEnd(0)
LL2.addNodetoEnd(1)
LL2.printLL()

length=0
cur=LL2.head
while cur != None:
    length+=1
    cur=cur.next

decimal=0
m=1<<length-1
cur=LL2.head
while cur != None:
    decimal+= cur.data * m
    m=m>>1
    cur=cur.next
print("Decimal :",decimal)


"""
Q-3 ) Middle of the Linked List (5 marks)
https://leetcode.com/problems/middle-of-the-linked-list/
(Medium)
Given a non-empty, singly linked list with head node head, return a middle node
of linked list.
If there are two middle nodes, return the second middle node.
Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3. (The judge's serialization of this node is
[3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next
= NULL.

"""

print("Q3) Middle of the Linked List :")

LL3=Linked_List()
LL3.addNodetoEnd(1)
LL3.addNodetoEnd(2)
LL3.addNodetoEnd(3)
LL3.addNodetoEnd(4)
LL3.addNodetoEnd(5)
LL3.printLL()

length=0
cur=LL3.head
while cur != None:
    length+=1
    cur=cur.next
mid=(length//2)+1

ctr=1
cur=LL3.head
while ctr!=mid:
    cur=cur.next
    ctr+=1
print("Element at Middle :",cur.data)
