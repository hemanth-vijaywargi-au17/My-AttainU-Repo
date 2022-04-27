"""
Q-2 ) Binary Search Tree to Greater Sum Tree (5 marks)
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
(Easy)
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
such that every key of the original BST is changed to the original key plus
sum of all keys greater than the original key in BST.
As a reminder, a binary search tree is a tree that satisfies these constraints:
● The left subtree of a node contains only nodes with keys less than
the node's key.
● The right subtree of a node contains only nodes with keys greater
than the node's key.
● Both the left and right subtrees must also be binary search trees.
Note: This question is the same as 538:
https://leetcode.com/problems/convert-bst-to-greater-tree/
Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Example 2:
Input: root = [0,null,1]
Output: [1,null,1]
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.val, end="  ")
    inorder(root.right)


def greater_tree(root, root_sum=[0]):
    if root is None:
        return
    greater_tree(root.right)
    root.val += root_sum[0]
    root_sum[0] = root.val
    greater_tree(root.left)
    return root


if __name__ == "__main__":

    root = Node(4, Node(1, Node(0), Node(2, None, Node(3))),
                Node(6, Node(5), Node(7, None, Node(8))))

    """
    Tree Visualized :
           4
         /   \
        1     6
       / \   / \
      0   2 5   7
           \     \
            3      8
    """
    inorder(greater_tree(root))