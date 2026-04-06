class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for string in strs:
            string1 = string
            string = "".join(sorted(string))
            if string in mydict:
                mydict[string].append(string1)
            else:
                mydict[string] = [string1]
        
        ans = []
        for key, value in mydict.items(): 
            in_ans = []
            for val in value:
                in_ans.append(val)
            ans.append(in_ans)
        return ans 





        