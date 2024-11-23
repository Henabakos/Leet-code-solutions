class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat

        answer = [[0 for i in range(c)] for j in range(r)]

        row,col = 0,0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if col == c:
                    col = 0
                    row += 1
                answer[row][col] = mat[i][j]
                col += 1

        return answer              