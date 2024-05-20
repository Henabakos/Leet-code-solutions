class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr1 = []
        for i in range(len(matrix[0])):
            arr = []
            for j in range(len(matrix)):
                arr.append(matrix[j][i])
            arr1.append(arr)
        return arr1
