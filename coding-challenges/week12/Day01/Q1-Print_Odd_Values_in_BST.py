"""
Q-1 ) Write a program to print nodes in a BST having odd values:
(Easy)
(5 marks)
Input:
Sample output:
3
1
7
13
"""
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_odd(root):
    if root == None:
        return
    inorder_odd(root.left)
    if root.val % 2 == 1:
        print(root.val, end="  ")
    inorder_odd(root.right)
    
if __name__ == "__main__":

    root = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))),
            Node(10, None, Node(14, Node(13))))
    """
    Tree Visualized :
           8
         /   \
       3     10
      / \      \
     1   6      14
        / \     /
       4   7   13
    """
    print("Odd Numbers in the BST (Inorder Traversal):")
    inorder_odd(root)

