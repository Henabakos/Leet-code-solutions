class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indx={}
        for i in range (len(s)):
            indx[s[i]]=i
        last=0
        li=[]
        max_=-1
        for i in range(len(s)):
            max_=max(max_,indx[s[i]])
            if i == max_:
                li.append((max_-last)+1)
                last=max_+1
        return li