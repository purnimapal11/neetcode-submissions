# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque()
        q.append(root)
        count = 1

        while q:
            qlen = len(q)
            res = []
            while qlen:

                node = q.popleft()           
                res.append(node.val)
                qlen -= 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if count%2 == 0:
                res.reverse()
            ans.append(res)
            count += 1
        return ans 