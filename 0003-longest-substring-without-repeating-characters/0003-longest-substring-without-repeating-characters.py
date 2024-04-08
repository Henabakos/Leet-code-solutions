class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack=[]
        cnt,i,j=0,0,0
        for k in range (len(s)):
            for b in range(k,len(s)):
                if s[b] not in stack:
                    stack.append(s[b])
                else:
                    break
            cnt=max(cnt,len(stack))
            stack=[]
        return cnt
        