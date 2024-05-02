class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        li=[]
        for ind,value in enumerate(nums):
            if value==target:
                li.append(ind)
        return li