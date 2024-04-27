class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixmod,result=0,0
        modgroup=[0]*k
        modgroup[0]=1
        for i in nums:
            prefixmod=(prefixmod + i % k + k) % k
            result+=modgroup[prefixmod]
            modgroup[prefixmod]+=1
        return result