class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt,total_sum=0,0
        prefix=defaultdict(int)
        prefix[0]=1
        for i in nums:
            total_sum+=i
            if total_sum - k in prefix:
                cnt+=prefix[total_sum - k]
            prefix[total_sum] += 1
        return cnt