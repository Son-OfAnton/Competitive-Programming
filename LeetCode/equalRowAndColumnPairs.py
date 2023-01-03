# https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dimension = len(grid)
        cols = []
        
        for row in range(dimension):
            single_col = []
            for col in range(dimension):
                single_col.append(grid[col][row])
            cols.append(single_col)
        
        equal_pair_count = 0
        
        for column in cols:
            equal_pair_count += grid.count(column)
                
        return equal_pair_count
    
# Store each strip of columns in a list and cuont each 
# column's frequency in the grid rows.
