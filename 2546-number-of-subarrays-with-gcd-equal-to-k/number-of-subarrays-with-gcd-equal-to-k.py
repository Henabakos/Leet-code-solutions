class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x


        cnt = 0

        for i in range(len(nums)):
            curr = nums[i]

            for j in range(i, len(nums)):
                
                curr = gcd(curr, nums[j])
                if curr == k:
                    cnt += 1
                if curr < k:
                    break
        return cnt