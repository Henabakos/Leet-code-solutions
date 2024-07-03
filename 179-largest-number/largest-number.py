class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i] = str(n)
        
        def compare(n1,n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums = sorted(nums,key=cmp_to_key(compare))
        nums = "".join(nums)
        if nums[0] == '0':
            return '0'
        else:
            return nums
         

