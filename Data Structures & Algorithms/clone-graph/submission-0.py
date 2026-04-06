"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dict1 = {}
        def dfs(node):
            if node in dict1:
                return dict1[node]
            
            x = Node(node.val)
            dict1[node] = x
            for n in node.neighbors:
                x.neighbors.append(dfs(n))
            return x

        if not node:
            return None
        return dfs(node)
