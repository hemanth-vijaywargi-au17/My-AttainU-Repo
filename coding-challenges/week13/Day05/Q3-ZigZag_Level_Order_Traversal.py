class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root):

    if not root:
        return []

    ans = []
    level = [root]

    while level:
        mid = [node.val for node in level]

        if len(ans) % 2 == 0:
            ans.append(mid)
        else:
            ans.append(mid[::-1])

        level = [child for node in level for child in (
            node.left, node.right) if child]

    return ans


if __name__ == "__main__":
    root = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))),
                Node(10, None, Node(14)))

    """
    Tree Visualized :
           8
         /   \
        3    10
       / \     \
      1   6    14
         / \   
        4   7  
    """
    print(zigzagLevelOrder(root))
