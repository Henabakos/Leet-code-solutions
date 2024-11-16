class Solution:
    def reverse(self, x: int) -> int:
        word = str(x)
        left = 0
        right = len(word) - 1

        while word[right] == 0:
            right -= 1
        if x < 0:
            a = ""
            reversed_num = word[left + 1 : right + 1]
            a += reversed_num[::-1]
            return int(a) - 2 * int(a) if int(a) <= pow(2,31) else 0
        else:
            a = ""
            reversed_num = word[left : right + 1]
            a += reversed_num[::-1]
            return int(a) if int(a) <= pow(2,31) else 0
