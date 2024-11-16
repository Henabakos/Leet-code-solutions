class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li = []
        a= ''
        for i in s: 
            if i == " ":
                if a != "" :
                    li.append(a)
                    a = ''
            else:
                a += i
        if a != "":
            li.append(a)

        
        return len(li[-1])


