class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        newStr=""
        for i in s:
            if i!="*":
                stack.append(i)
            else:
                stack.pop()
        for i in stack:
            newStr+=i
        return newStr