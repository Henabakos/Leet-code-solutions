class Solution:
    def gcd(a,b):
        if a == 0:
            return b
        return gcd(b%a , a)
        
    def findGCD(self, nums: List[int]) -> int:
        max_elt = max(nums)
        min_elt = min(nums)
        return gcd(max_elt , min_elt)
