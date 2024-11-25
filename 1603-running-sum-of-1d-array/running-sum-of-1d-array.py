class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []

        for i in range(len(nums)):
            if prefix :
                prefix.append(prefix[-1] + nums[i])
            else:
                prefix.append(nums[i])
        return prefix
