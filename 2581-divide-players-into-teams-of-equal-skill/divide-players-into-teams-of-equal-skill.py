class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) -1
        container = set()
        mul_container = list()
        cnt = 0
        while left < right:
            container.add(skill[left] + skill[right])
            mul_container.append(skill[left] * skill[right])
            left += 1
            right -= 1
        
        if len(container) == 1:
           return sum(mul_container)
        else:
            return -1
        
            