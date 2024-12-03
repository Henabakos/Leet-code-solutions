class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        i = 0
        for sp in spaces:
            res.append(s[i:sp])
            i = sp
        res.append(s[i:])
        ans = " ".join(res)
        return ans
        
