class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=1
        for k in range(len(nums)-1):
            if nums[i]==0:
                if nums[j]!=0:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
                    i+=1
                    j+=1
                else:
                    j+=1
            else:
                i+=1
                j+=1
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        