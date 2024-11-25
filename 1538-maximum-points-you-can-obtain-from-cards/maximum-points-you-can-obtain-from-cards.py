class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefix = []
        rev_prefix = []

        for i in range(k):
            if prefix:
                prefix.append(prefix[-1] + cardPoints[i])
            else:
                prefix.append(cardPoints[i])
        
        for j in range(k):
            if rev_prefix:
                rev_prefix.append(rev_prefix[-1] + cardPoints[-1 - j])
            else:
                rev_prefix.append(cardPoints[-1])
        print(rev_prefix)
            
        current_sum = max(rev_prefix[-1] ,prefix[-1] )
        for i in range(len(rev_prefix) - 1):
            sum1 = prefix[i] + rev_prefix[-2 - i]
            current_sum = max(current_sum , sum1)
        return current_sum




        