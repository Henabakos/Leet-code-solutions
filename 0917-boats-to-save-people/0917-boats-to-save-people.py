class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i,j=0,len(people)-1
        cnt=0
        cnt2=0
        people.sort()
        while i<= j:
            if people[i] + people[j] <= limit:
                cnt+=1
                j-=1
                i+=1
            else:
                cnt+=1
                j-=1

        return cnt

