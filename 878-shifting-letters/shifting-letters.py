class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        shift = shifts[::-1]
        

        prefix = list(accumulate(shift))
        prefix = prefix[::-1]
        print(prefix)


        res = ""
        for i in range(len(prefix)):
            res += chr((ord(s[i]) - ord("a") + prefix[i]) % 26 + ord("a"))

        return res

        

