class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        right = left = 0
        while right < len(nums) :
            if nums[right] == 0:
                k -= 1
            while k < 0:
                ans = max(ans,right - left)
                if nums[left] == 0:
                    k += 1
                left += 1
            right += 1
        ans = max(ans,right - left)
        return ans

