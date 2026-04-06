class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range (len(nums)+1)]
        mydict = {}

        for ele in nums:
            mydict[ele] = 1+ mydict.get(ele, 0)
        
        for key, val in mydict.items():
            bucket[val].append(key)
        ans = []
        for i in range(len(bucket)-1, 0 , -1):
            for j in bucket[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans
        
        
            
        