class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def addNodetoEnd(self, x):
        if self.head is None:
            self.head = Node(x)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(x)

    def addNodetoBegin(self, x):
        if self.head is None:
            self.head = Node(x)
        else:
            new_node = Node(x)
            new_node.next = self.head
            self.head = new_node

    def removeNodeEnd(self):
        if self.head is None:
            print("LL is already Empty")
        elif self.head.next is None:
            self.head = None
        else:
            cur = self.head
            while cur.next.next != None:
                cur = cur.next
            cur.next = None

    def removeNodeBegin(self):
        if self.head is None:
            print("LL is already Empty")
        else:
            self.head = self.head.next

    def printLL(self):
        if self.head is None:
            print("LL is Empty")
        else:
            cur = self.head
            while cur != None:
                print(cur.val, end="  ")
                cur = cur.next
        print()


"""
Q-1 ) Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/
(5 marks)
(Medium)
Write a function to delete a node in a singly-linked list. You will not be given
access to the head of the list, instead you will be given access to the node
to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list.
Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list
should become 4 -> 1 -> 9 after calling your function.
"""

print("Q1) Delete a Node :")


def printlist(head):
    if head is None:
        print("LL is Empty")
    else:
        cur = head
        while cur != None:
            print(cur.val, end="  ")
            cur = cur.next
    print()


head = Node(5)

Node2 = Node(1)
head.next = Node2

Node3 = Node(4)
Node2.next = Node3

Node4 = Node(9)
Node3.next = Node4

printlist(head)


def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next


deleteNode(Node3)
printlist(head)

"""
Q-2 )Remove Duplicates from Sorted List (5 marks)
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
(Easy)
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.
Example 1:
Input: head = [1,1,2]
Output: [1,2]
Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

"""

print("Q2) Duplicate Remover (from a sorted List) :")

LL5 = Linked_List()

LL5.addNodetoEnd(1)
LL5.addNodetoEnd(1)
LL5.addNodetoEnd(2)
LL5.addNodetoEnd(2)
LL5.addNodetoEnd(2)
LL5.addNodetoEnd(2)
LL5.addNodetoEnd(3)

LL5.printLL()


def deleteDuplicates(head):
    cur = head
    while cur != None and cur.next != None:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


printlist(deleteDuplicates(LL5.head))

"""
Q-3 ) Merge In Between Linked Lists (5 marks)
https://leetcode.com/problems/merge-in-between-linked-lists/
(Medium)
You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their
place.
The blue edges and nodes in the following figure incidate the result:
Build the result list and return its head.
Example 1:
Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [0,1,2,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their
place. The blue edges and nodes in the above figure indicate the result.
"""

print("Q3) Merge In Between Linked Lists :")
ll6 = Linked_List()
ll7 = Linked_List()

list1 = [0, 1, 2, 3, 4, 5]
list2 = [10000, 10001, 100]
a = 3
b = 4

for i in range(len(list1)):
    ll6.addNodetoEnd(list1[i])

for i in range(len(list2)):
    ll7.addNodetoEnd(list2[i])

ll6.printLL()
ll7.printLL()


def mergeInBetween(list1, list2, a, b):
    cur = list1
    ctr = 0
    while ctr != b + 1 and cur != None:
        if ctr == a - 1:
            start = cur
        cur = cur.next
        ctr += 1
    end = cur

    cur = list2
    while cur.next != None:
        cur = cur.next
    cur.next = end

    start.next = list2

    return list1


printlist(mergeInBetween(ll6.head, ll7.head, 3, 4))
