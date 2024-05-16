class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        n = len(p)-1
        right = n
        indx=[]
        hash_p = {}
        for i in p:
            if i in hash_p:
                hash_p[i] += 1
            else:
                hash_p[i] = 1
        while right < len(s):
            if Counter(s[left : right + 1]) == hash_p:
                indx.append(left)
                left +=1
                right +=1
            else:
                left += 1
                right += 1
                print(left,right)
        return indx