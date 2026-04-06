# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        


        def helper(root):
            if not root:
                return float('inf'), float('-inf'), True


            leftmin, leftmax, isleftvalid = helper(root.left)
            rightmin, rightmax, isrightvalid = helper(root.right)
            

            currmin = min(leftmin, rightmin, root.val)
            currmax = max(leftmax, rightmax, root.val)

            curr_satisfy_property =  leftmax < root.val and rightmin > root.val
            
            return currmin, currmax, (isleftvalid and isrightvalid and curr_satisfy_property)

        left, right, isBST = helper(root)
        return isBST