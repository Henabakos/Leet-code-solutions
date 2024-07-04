class Solution:
    def minDifference(self, nums: List[int]) -> int:

        if len(nums) <= 4:
            return 0
        
        nums.sort()

        min_dif = float("inf")

        for l in range(4):
            r = len(nums) - 4 + l
            min_dif = min(min_dif,nums[r]-nums[l])
        return min_dif
       