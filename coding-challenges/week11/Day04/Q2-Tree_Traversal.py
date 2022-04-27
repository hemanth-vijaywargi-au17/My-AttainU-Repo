class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = Node(3)
root.left = Node(4)
root.right = Node(5)

root.left.left = Node(5)
root.left.right = Node(4)

root.right.right = Node(7)

"""
Tree Visualized :
           3
         /   \
        4     5
       / \     \
      5   4     7
"""

print("Preorder Traversal :")
def preorder(root):
    if root == None:
        return
    print(root.val, end="  ")
    preorder(root.left)
    preorder(root.right)

preorder(root)
print()


print("Inorder Traversal :")
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.val, end="  ")
    inorder(root.right)

inorder(root)
print()



print("Postorder Traversal :")
def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end="  ")

postorder(root)
print()
