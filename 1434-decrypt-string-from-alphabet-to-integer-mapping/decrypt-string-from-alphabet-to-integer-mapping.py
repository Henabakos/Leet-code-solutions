class Solution:
    def freqAlphabets(self, s: str) -> str:
        a=""
        li=[]
        j=len(s)-1
        allchar={}
        for i in range(26):
            if i<9:
                allchar[f'{i+1}'] = f'{chr(97+i)}'
            else:
                allchar[f'{i+1}#'] = f'{chr(97+i)}'
        for i in range(len(s)-1,-1,-1):
            if j>=0:
                if s[j]=="#":
                    for key,value in allchar.items():
                        if key==s[j-2:j+1]:
                            a+=value
                    j-=3
                else:
                    for key,value in allchar.items():
                        if key==s[j]:
                            a+=value
                    j-=1
            
        return a[::-1]