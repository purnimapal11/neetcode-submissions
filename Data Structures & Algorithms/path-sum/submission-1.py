# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False 

        self.summ = 0 
        def func(node):
            if not node:
                return False
            self.summ += node.val
            if not node.left and not node.right:
                res = (self.summ == targetSum)
            else:
                res = func(node.left) or func(node.right)

            self.summ -= node.val #self.summ accumulates the sum for all nodes, so while backtracking we need to remove the current node.val 
            return res

        return func(root)