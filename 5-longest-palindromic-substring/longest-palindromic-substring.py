class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        li = []
        while left < len(s):
            right = len(s) -1
            while right >= left:
                if s[left] == s[right]:
                    a = s[left : right + 1]
                    b = a[::-1]

                    if a == b:
                        li.append(a)
                right -= 1
            left += 1
        
        max_len = -1
        a = ""

        for i in li:
            if len(i) > max_len:
                max_len = len(i)
                a = i
        return a

                