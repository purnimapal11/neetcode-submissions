class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        
        for string in strs:
            count = [0]*26
            for st in string: 
                count[ord(st) - ord("a")] += 1 
            mydict[tuple(count)].append(string) # in python we can't have list as key 
        
        ans = []
        for key, value in mydict.items(): 
            in_ans = []
            for val in value:
                in_ans.append(val)
            ans.append(in_ans)
        return ans 





        