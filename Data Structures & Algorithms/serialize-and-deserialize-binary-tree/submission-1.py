# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.st = ""

        def dfs(node):
            if not node:
                self.st += "N,"
                return 
            self.st += str(node.val)+ ","
            # adding a delimiter is imp: 51 and 5, 1 are diff
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.st
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        size = len(data)
        self.i = 0
        def dfs():
            if self.i >= size:
                return 
            if data[self.i] == "N":
                self.i += 1
                return None
            
            root = TreeNode(int(data[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()
