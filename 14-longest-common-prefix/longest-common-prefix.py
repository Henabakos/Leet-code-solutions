class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        min_value = 1000
        for i in strs:
            if len(i) < min_value:
                min_value = len(i)
        for i in range(min_value):
            temp = strs[0][i]
            print(temp)
            for string in strs:
                if string[i] != temp:
                    return result
            result = result + temp
        return result

        