class Solution:
    def gcd(a,b):
        if a == 0:
            return b
        return gcd(b%a , a)

    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        max_elt = nums[-1]
        min_elt = nums[0]
        return gcd(max_elt , min_elt)
