class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums) - 1

        ans = 0

        while high >= low:
            mid = (low + high)//2

            if nums[mid] < target:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            return ans