class Solution:
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
       
        unique_values = set(nums)
        
        max_val = max(unique_values)
        result_gcds = set()

      
        for g in range(1, max_val + 1):
            current_gcd = 0
            
            for multiple in range(g, max_val + 1, g):
                if multiple in unique_values:
                    current_gcd =gcd(current_gcd, multiple)
                
                    if current_gcd == g:
                        result_gcds.add(g)
                        break
        
       
        return len(result_gcds)