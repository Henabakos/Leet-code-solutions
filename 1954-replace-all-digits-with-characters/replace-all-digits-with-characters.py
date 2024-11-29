class Solution:
    def replaceDigits(self, s: str) -> str:
        shift = []
        string = ""
        for i in s:
            if i.isdigit():
                shift.append(int(i))
            else:
                string += i    
        res = ""

        for i in range(len(shift)):
            res += string[i] + chr((ord(string[i]) - ord("a") + shift[i]) % 26 + ord("a"))
        
        for i in range(len(shift) , len(string)):
            res += string[i]
        return res
        