# [2428] https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_columns = len(grid[0])
        max_sum = 0

        for col_idx in range(n_columns - 2):
            for row_idx in range(n_rows - 2):
                        top = sum(grid[row_idx][col_idx:col_idx+3])
                        mid = grid[row_idx+1][col_idx+1]
                        bottom = sum(grid[row_idx+2][col_idx:col_idx+3])
                        max_sum = max(top + mid + bottom, max_sum)
        
        return max_sum
