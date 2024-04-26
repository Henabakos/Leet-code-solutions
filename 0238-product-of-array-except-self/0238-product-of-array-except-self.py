class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        ans=[]
        a=1
        b=1
        for i in nums:
            a*=i
            right.append(a)
        for i in range(len(nums)-1,-1,-1):
            b*=nums[i]
            left.append(b)
        left=left[::-1]

        for i in range(len(nums)):
            a=i-1
            b=i+1
            if a<0:
                ans.append(1*left[b])
            elif b==len(nums):
                ans.append(1*right[a])
            else:
                ans.append(left[b]*right[a])
        return ans


