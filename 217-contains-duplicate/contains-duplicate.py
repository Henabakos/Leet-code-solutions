class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _set = set(nums)
        if len(_set) != len(nums):
            return True
        return False

