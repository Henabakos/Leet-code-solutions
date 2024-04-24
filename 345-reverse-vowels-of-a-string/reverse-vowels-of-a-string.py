class Solution:
    def reverseVowels(self, s: str) -> str:
        a=['a','e','i','o','u','A','E','I','O','U']
        i,j=0,len(s)-1
        s=list(s)
        b=""
        while i<j:
            if s[i] in a:
                if s[j]in a:
                    temp=s[i]
                    s[i]=s[j]
                    s[j]=temp
                    j-=1
                    i+=1
                else:
                    j-=1
            else:
                i+=1
        for i in s:
            b+=i
        return b


        