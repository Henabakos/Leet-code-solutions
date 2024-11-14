class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        transpose_matrix = []

        for col_ in range(col):
            res = []
            for row_ in range(row):
                res.append(matrix[row_][col_])
            transpose_matrix.append(res)
        return transpose_matrix



               
        return matrix