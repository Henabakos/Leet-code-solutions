class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n=len(skill)//2
        i=0
        j=len(skill)-1
        c=set()
        for k in range(n):
            b=skill[i]+skill[j]
            c.add(b)
            i+=1
            j-=1
        if len(c)==1:
            i=0
            j=len(skill)-1
            sum=0
            for r in range(n):
                sum+=skill[i]*skill[j]
                i+=1
                j-=1
        else:
            return -1
        return sum


            

        