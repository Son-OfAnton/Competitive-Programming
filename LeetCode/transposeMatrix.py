# https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        resMatrix = []
        n_rows = len(matrix)
        n_columns = len(matrix[0])

        for col in range(n_columns):
            resMatrix.append([0] * n_rows)

        for row in range(n_rows):
            for col in range(n_columns):
                resMatrix[col][row] = matrix[row][col]

        return resMatrix

