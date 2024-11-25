class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ""

        for i in s:
            if  i.isalpha() or i.isdigit():
                reverse += i.lower()
        print(reverse[::-1])
        if reverse[::-1] == reverse:
            return True
        return False 