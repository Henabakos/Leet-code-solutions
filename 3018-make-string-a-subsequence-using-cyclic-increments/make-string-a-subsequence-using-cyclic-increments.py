class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        left = 0
        right = 0

        while left < len(str1) and right < len(str2):
            if str1[left] == str2[right] or chr((ord(str1[left]) - ord("a") + 1) % 26 + ord("a")) == str2[right]:
                print(chr((ord(str1[left]) - ord("a") + 1) % 26 + ord("a")))
                right += 1
                left += 1
            else:
                left += 1
        if right == len(str2):
            print(left , right)
            return True
        else:
            print(left , right)
            return False


