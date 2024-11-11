class Solution:
    def gcd(a, b):
        if a == 0:
            return b
        return gcd( b%a , a)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        gcd_length = gcd(len1, len2)
        
        can = str1[:gcd_length]
        
        if can * (len1 // gcd_length) == str1 and can * (len2 // gcd_length) == str2:
            return can
        else:
            return ""


  