class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        length = len(s)
        delta = [0]* length

        for shift in shifts:
            start , end , value = shift
            if value == 0:
                delta[start] += -1
                if end + 1 < length:
                    delta[end + 1] -= -1
            else:
                delta[start] += 1
                if end + 1 < length:
                    delta[end + 1] -= 1
        
        prefix = list(accumulate(delta))
        res = ""
        print(prefix)

        for i in range(length):
            res += chr((ord(s[i]) - ord("a") + prefix[i]) % 26 + ord("a"))
        return res




