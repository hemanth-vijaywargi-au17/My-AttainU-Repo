class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    if node == None:
        return None

    vi = set()
    hm = {}

    def dfs(node, vi, hm):
        vi.add(node)
        copyNode = Node(node.val, [])
        hm[node] = copyNode

        for dest in node.neighbors:
            if dest not in vi:
                dfs(dest, vi, hm)

            copyNode.neighbors.append(hm[dest])

    dfs(node, vi, hm)

    return hm[node]
