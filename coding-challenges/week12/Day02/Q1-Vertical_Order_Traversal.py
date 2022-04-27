'''
Q-1 ) Print vertical order traversal, or Top view of a binary tree
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
(5 marks)
(Easy)
Given the root of a binary tree, calculate the vertical order traversal of the binary
tree.
For each node at position (row, col), its left and right children will be at positions
(row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0,
0).
The vertical order traversal of a binary tree is a list of top-to-bottom orderings for
each column index starting from the leftmost column and ending on the rightmost
column. There may be multiple nodes in the same row and same column. In such
a case, sort these nodes by their values.
Return the vertical order traversal of the binary tree.
'''
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.data = key 
        self.left = None
        self.right = None
  
# A utility function to find min and max distances with
# respect to root 
def findMinMax(node, minimum, maximum, hd):
      
    # Base Case
    if node is None:
        return 
      
    # Update min and max
    if hd < minimum[0] :
        minimum[0] = hd
    elif hd > maximum[0]:
        maximum[0] = hd
  
    # Recur for left and right subtrees
    findMinMax(node.left, minimum, maximum, hd-1)
    findMinMax(node.right, minimum, maximum, hd+1)
  
# A utility function to print all nodes on a given line_no
# hd is horizontal distance of current node with respect to root
def printVerticalLine(node, line_no, hd):
      
    # Base Case
    if node is None:
        return
      
    # If this node is on the given line number
    if hd == line_no:
        print (node.data)
  
    # Recur for left and right subtrees
    printVerticalLine(node.left, line_no, hd-1)
    printVerticalLine(node.right, line_no, hd+1)
  
def verticalOrder(root):
      
    # Find min and max distances with respect to root
    minimum = [0]
    maximum = [0]
    findMinMax(root, minimum, maximum, 0)
  
    # Iterate through all possible lines starting 
    # from the leftmost line and print nodes line by line
    for line_no in range(minimum[0], maximum[0]+1):
        printVerticalLine(root, line_no, 0)
        print 
           
  
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
  
print ("Vertical order traversal is")
verticalOrder(root)
  