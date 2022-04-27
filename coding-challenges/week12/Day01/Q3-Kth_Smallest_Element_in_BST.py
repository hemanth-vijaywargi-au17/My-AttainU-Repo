"""
Q-3 ) Kth Smallest Element in a BST (5 marks)
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
(Medium)
Given the root of a binary search tree, and an integer k, return the kth
(1-indexed) smallest element in the tree.
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive Approach :
def inorder_list(root):
    
    res = []
    
    if root.left != None:
        res.extend(inorder_list(root.left))
   
    res.append(root.val)

    if root.right != None:
        res.extend(inorder_list(root.right))
    
    return res


# Iterative Approach :
def kthSmallest(root, k):
    
    current = root
    stack = [] 
    res = []

    while len(res) < k:

        if current is not None:

            stack.append(current)
            current = current.left

        elif(stack):

            current = stack.pop()
            res.append(current.val)
            current = current.right

        else:
            break

    return res[-1]


if __name__ == "__main__":

    root = Node(3, Node(1, None, Node(2)), Node(4))
    k = 2
    """
    Tree Visualized :
           3
         /   \
        1     4
         \      
          2            
    """

    # Driver Code for Recursive Method :
    list1 = inorder_list(root)
    
    print("Kth Smallest Element in BST :",list1[k-1])

    # Driver Code for Iterative Method :
    print("Kth Smallest Element in BST :",kthSmallest(root,k))

