class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
           
        low, high = 1, x
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans