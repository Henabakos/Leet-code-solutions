class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n>2:
            greater=n
        else:
            greater=2
        while(True):
            if greater%n==0 and greater%2==0:
                return greater
            greater+=1
        return greater