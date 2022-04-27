'''
Q-3 ) Binary Tree Tilt (5 marks)
https://leetcode.com/problems/binary-tree-tilt/
(Easy)
Given the root of a binary tree, return the sum of every tree node's tilt.
The tilt of a tree node is the absolute difference between the sum of all left
subtree node values and all right subtree node values. If a node does not have a
left child, then the sum of the left subtree node values is treated as 0. The rule is
similar if there the node does not have a right child
'''
class Solution:
    def findTilt(self, root: TreeNode,answer=True) -> int:
        if not root:return 0 if answer else (0,0)
        ls,ld=self.findTilt(root.left,False)
        rs,rd=self.findTilt(root.right,False)
        result=abs(ls-rs)+ld+rd
        if not answer:result=root.val+ls+rs,result
        return result
    
        #ls,rs means left sum and right sum