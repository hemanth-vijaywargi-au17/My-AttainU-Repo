'''
Q-1 ) write a program to take input a Binary tree and tell if that binary tree is
balanced or not?
https://leetcode.com/problems/balanced-binary-tree/
(5 marks)
(Easy)
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by
no more than 1.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # If root is empty
        if root==None:
            return True
        
        # Building a utility function to calculate if node is a leaf
        def is_leaf(node):
            if node.left == None and node.right==None:
                return True
            return False
        
        # A recursive function
        # Calculates if a certain node is balanced
        # 1) Checks the height of left and right children
        # 2) If unbalanced, returns "-1", otherwise returns height
        
        def get_height(node):
            
            # If the node is a leaf, height is by default 1
            if is_leaf(node):
                return 1
            
            # Creating 2 variables for the child
            left  = node.left
            right = node.right
            
            # If node has a left Child
            if left!=None:
                h_left  = get_height(left)
                left_val = left.val
                # If left child is unbalanced
                if h_left == -1:
                    return -1
            # If node doesn't have a left child
            else:
                h_left = 0
                left_val = None
            
            # If node has a right child
            if right!=None:
                h_right = get_height(right)
                right_val = right.val
                # If right child is unbalanced
                if h_right == -1:
                    return -1
            # If node doesn't have a right child
            else:
                h_right = 0
                right_val = None
            
            # If the left and right heights differ by more than 1 points
            if abs(h_left-h_right)>1:
                return -1
            
            # If everything went well
            return max(h_left, h_right)+1
        
        res = get_height(root)
        if res==-1:
            return False
        return True