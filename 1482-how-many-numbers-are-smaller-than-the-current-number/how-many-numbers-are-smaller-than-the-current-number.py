class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter_controllers = []

        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    cnt += 1
            counter_controllers.append(cnt)
        return counter_controllers