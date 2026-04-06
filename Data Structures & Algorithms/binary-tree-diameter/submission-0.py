class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        largestheight = 0
        def dfs(node):
            nonlocal largestheight
            if not node:
                return 0

            leftheight = dfs(node.left)
            rightheight = dfs(node.right)

            curr = leftheight + rightheight
            largestheight = max(largestheight, curr)

            return max(leftheight, rightheight) + 1

        dfs(root)
        return largestheight