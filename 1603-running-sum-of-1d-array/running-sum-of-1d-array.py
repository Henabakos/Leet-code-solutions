class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix=[0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        return prefix[1:]
        