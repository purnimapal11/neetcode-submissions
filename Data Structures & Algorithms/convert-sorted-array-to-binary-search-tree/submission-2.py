class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def buildTree(l, r):

            if l > r:
                return 

            mid = (l+r)//2
            root = TreeNode(nums[mid])
            root.left = buildTree(l, mid-1)
            root.right = buildTree(mid+1, r)

            return root

        root = buildTree(0, len(nums)-1)
        return root