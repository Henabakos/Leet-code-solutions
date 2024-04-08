class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split(' ')
        f=""
        for i in a:
            i=i[::-1]
            if f=="":
                f=f+i
            else:
                f=f+" "+i
            
        return f
        