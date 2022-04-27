"""
Q-3) Same Tree (5 marks)
https://leetcode.com/problems/same-tree/
Given the roots of two binary trees p and q, write a function to check if they
are the same or not.
Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false
"""

# Definition for a binary tree node.

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def check(p,q):

            if p is None and q is None:
                return True
            if (p is None and q is not None ) or (p is not None and q is None):
                return False
            if p.val!=q.val:
                return False

            return check(p.left,q.left) and check(p.right,q.right)

        return check(p,q)