"""
Q-3) Maximum Depth of Binary Tree(or height of a BT): (5 marks)
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:
Input: root = [1,null,2]
Output: 2
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    if root == None:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right))+1


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
"""
Tree Visualized :
            3
          /   \
         9    20
             /  \      
            15   7
Max Height (or) Depth of Above Binary Tree = 3
"""
print(maxDepth(root))
