# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))

        if not root:
            return 0

        left = height(root.left)
        right = height(root.right)

        diameter = left+right

        dialeft = self.diameterOfBinaryTree(root.left)
        diaright = self.diameterOfBinaryTree(root.right)

        return max(diameter, dialeft, diaright)






        