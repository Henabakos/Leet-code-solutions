class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for j in range(len(arr2)):
            for i in range(len(arr1)):
                if arr1[i] == arr2[j]:
                    result.append(arr1[i])
                    arr1[i] = -1
        arr1.sort()
        for j in range(len(arr1)):
            if arr1[j] != -1:
                result.append(arr1[j])
        return result