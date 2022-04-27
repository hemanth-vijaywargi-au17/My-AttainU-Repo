"""
Q-2 ) Palindrome Linked List (5 marks)
https://leetcode.com/problems/palindrome-linked-list/
(Easy)
5612
448
Add to List
Share
Given the head of a singly linked list, return true if it is a palindrome.
Example 1:
Input: head = [1,2,2,1]
Output: true
Example 2:
Input: head = [1,2]
Output: false
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    res = []
    while head != None:
        res.append(head.val)
        head = head.next

    return res == res[::-1]


head = Node(1, Node(2, Node(1)))
print(isPalindrome(head))