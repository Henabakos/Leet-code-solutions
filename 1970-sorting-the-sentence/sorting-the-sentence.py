class Solution:
    def sortSentence(self, s: str) -> str:
        string_words = s.split(' ')
        print(string_words)

        result = [0]*len(string_words)
        print(result)

        for i in range(len(string_words)):
            a = int(string_words[i][-1])
            result[a - 1] = string_words[i][:-1]
        return " ".join(result)
            
            