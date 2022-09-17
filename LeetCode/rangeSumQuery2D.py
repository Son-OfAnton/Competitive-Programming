# 304. Range Sum Query 2D - Immutable

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for i in range(len(matrix)):
            self.prefix.append([0])
            for j in range(len(matrix[i])):
                self.prefix[i].append(matrix[i][j] + self.prefix[i][-1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        self.sum = 0
        for row in range(row1, row2+1):
            self.sum += self.prefix[row][col2+1] - self.prefix[row][col1]
        
        return self.sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
