class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        chacker={"}":"{",")":"(","]":"["}

        for i in s:
            if i in chacker:
                if stack and stack[-1]==chacker[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack)==0
