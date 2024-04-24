class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i,j=0,1
        while(j<len(nums)):
            if nums[i]==nums[j]:
                nums[i]=nums[i]*2
                nums[j]=0
                i+=1
                j+=1
            else:
                j+=1
                i+=1
       
        k,f=0,1
      
        while f<=len(nums)-1:
            if nums[k]==0:
                if nums[f]!=0:
                    nums[k],nums[f]=nums[f],nums[k]
                    k+=1
                    f+=1
                else:
                    f+=1
            else:
                f+=1
                k+=1
        return nums