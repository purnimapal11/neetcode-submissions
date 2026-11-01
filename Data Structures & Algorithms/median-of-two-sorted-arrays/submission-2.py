class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = m, n
        
        if not nums1:
            nums1 = nums2[:]
            p = len(nums2)
        else:
            l = 0 
            r = len(nums1)-1
            p = 0

            while p < len(nums2) and l <= r:
                mid = l + (r-l // 2) 

                if nums1[mid] > nums2[p]:
                    r = mid -1 
                elif nums1[mid] < nums2[p]:
                    l = mid+1
                else:
                    nums1.insert(mid, nums2[p])
                    p += 1
                    l = 0
                    r = len(nums1) - 1
                if l > r:
                    nums1.insert(l, nums2[p])
                    p += 1
                    l = 0
                    r = len(nums1)-1
            
        size = len(nums1)
        ctr = (size-1 )// 2
        if size % 2 == 0:
            return ((nums1[ctr] + nums1[ctr+1]) / 2 )
        else:
            return nums1[ctr]


