'''
Q-1 ) Diameter of a binary tree
https://leetcode.com/problems/diameter-of-binary-tree/description/
(5 marks)
(Easy)
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges
between them.
Example 1:
￼
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].
'''
class Node:
    def _init_(self,x):
        self.val=x
        self.left=None
        self.right=None

def find_height(root):
    global diameter
    if root is None:
        return 0
    left=find_height(root.left)
    right=find_height(root.right)
    if left+right>diameter:
        diameter = left+right
    return 1+max(left,right)
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
diameter=0
left=find_height(root)

print(diameter)