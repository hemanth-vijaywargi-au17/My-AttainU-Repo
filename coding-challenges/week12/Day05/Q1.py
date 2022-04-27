'''
(Maximum marks -15)
Q-1 ) Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
(5 marks)
(Easy)
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two
subtrees of every node never differs by more than one.
'''
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        node = TreeNode()
        if len(nums) == 0:
            return None
        if len(nums)  == 1: 
            node.val = nums[0]
            return node
        
        mid = math.floor(len(nums)/2)
        left = self.sortedArrayToBST(nums[:mid]) 
        right = self.sortedArrayToBST(nums[mid +1:])
        
        node.val = nums[mid] 
        node.left = left
        node.right = right
        
        return node