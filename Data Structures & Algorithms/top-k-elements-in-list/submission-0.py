class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {} 

        for num in nums:
            if num in mydict:
                mydict[num] += 1
            else:
                mydict[num] = 1 
        
        items = mydict.items()
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

                    # Step 3: Create a new dictionary from the sorted items
        sorted_dict = dict(sorted_items)
        ans = []
        for key, val in sorted_dict.items():
            if len(ans) < k:
                ans.append(key)
        
        return ans 

            
        