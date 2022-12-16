# https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        resMatrix = []
        n_rows = len(matrix)
        n_columns = len(matrix[0])

        for i in range(n_columns):
            resMatrix.append([0] * n_rows)

        for i in range(n_rows):
            for j in range(n_columns):
                resMatrix[j][i] = matrix[i][j]

        return resMatrix

