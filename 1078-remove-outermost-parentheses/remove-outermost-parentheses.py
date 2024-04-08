class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        sr=""
        for i in range(len(s)):
            if not stack:
                c=i
            if s[i]=="(":
                stack.append(s[i])
            else:
                if len(stack)>1:
                    stack.pop()
                else:
                    stack.pop()
                    sr+=s[c+1:i]
        return sr
            

        