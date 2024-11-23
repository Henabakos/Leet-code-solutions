class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        answer = []

        for row in matrix:
            answer.append(row[:])

        for oldrow in range(len(matrix)):
            for oldcol in range(len(matrix[0])):

                matrix[oldcol][len(matrix)-1 - oldrow] = answer[oldrow][oldcol]
        