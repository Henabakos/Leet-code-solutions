class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()[::-1]
        sr=""
        for i in a:
            sr=sr+i+" "
        return sr[:len(sr)-1]