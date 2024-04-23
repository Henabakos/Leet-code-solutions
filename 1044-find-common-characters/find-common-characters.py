class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common=Counter(words[0])
        for word in words:
            wrd_cnt=Counter(word)
            common &= wrd_cnt
        res=[]
        for elt,cnt in common.items():
            res+=[elt]*cnt
        return res
