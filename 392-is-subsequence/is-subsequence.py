class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        left = 0
        right = 0
        cnt = 0

        while right < len(t) and left < len(s):
            if s[left] != t[right]:
                right += 1
            else:
                cnt += 1
                print(cnt)
                left += 1
                right += 1
        if cnt == len(s):
            return True
        else:
            return False


    
