'''
Q-3 )Increasing Order Search Tree (5 marks)
https://leetcode.com/problems/increasing-order-search-tree/
(Easy)
Given the root of a binary search tree, rearrange the tree in in-order so that the
leftmost node in the tree is now the root of the tree, and every node has no left
child and only one right child.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.final = []
    def inOrder(self,root):
        if not root:
            return
        self.inOrder(root.left)
        self.final.append(root.val)
        self.inOrder(root.right)
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.inOrder(root)
        newNode2 = TreeNode(self.final[0],None,None)
        newNode = newNode2
        for i in range(1,len(self.final)):
            newNode.right = TreeNode(self.final[i])
            newNode = newNode.right
        return newNode2