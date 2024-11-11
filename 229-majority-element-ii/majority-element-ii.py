class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = Counter(nums)
        result = []
        for key , value in majority.items():
            if value > len(nums)//3:
                result.append(key)
        return result
