class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = Counter(nums)
        for key , value in majority.items():
            if value > len(nums)//2 :
                return key

