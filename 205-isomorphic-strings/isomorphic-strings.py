class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        assign={}
        j=0
        sr=""
        for i in range(len(s)):
            if s[j] not in assign:
                assign[s[j]]=t[j]
                j+=1
            else:
                j+=1

        for k in t:
            for key,value in assign.items():
                if value==k:
                    sr+=key
        
        return sr==s
            
            