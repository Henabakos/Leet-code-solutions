class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) -1 
        largest = 0

        while high >= low and high >= 0:
            mid = (low + high)//2
            if ord(letters[mid]) > ord(target):
                high = mid -1
                largest = letters[mid]
            else:
                low = mid + 1
        if largest ==  0:
            return letters[0]
        else:
            return largest
        