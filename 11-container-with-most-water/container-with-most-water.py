class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        max_=0
        while(i!=j):
            min_=min(height[i],height[j])
            a=min_*(j-i)
            max_=max(a,max_)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_
       
        