class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        int_indices={}

        for i ,num in enumerate(nums):
            complement=target-num
            
            if complement in int_indices:
                return [int_indices[complement],i]
            int_indices[num]=i
        
