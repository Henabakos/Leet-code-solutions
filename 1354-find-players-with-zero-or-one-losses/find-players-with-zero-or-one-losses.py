class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost=defaultdict(int)

        for m in matches:
            lost[m[0]]+=0
            lost[m[1]]+=1

        zero=sorted(k for k,i in lost.items() if i==0)
        ones=sorted(k for k,i in lost.items() if i==1)
        return ([zero,ones])