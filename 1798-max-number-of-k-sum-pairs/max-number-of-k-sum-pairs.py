class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = cnt = 0
        right = len(nums) - 1

        while right > left :
            if nums[right] + nums[left] < k:
                left += 1
            elif nums[right] + nums[left] > k:
                right -= 1
            else:
                left += 1
                right -= 1
                cnt += 1
        return cnt
            