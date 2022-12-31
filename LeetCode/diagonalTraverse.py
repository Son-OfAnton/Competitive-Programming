# https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row_size = len(mat)
        col_size = len(mat[0])
        sum_map = defaultdict(list)
        
        for i in range(row_size):
            for j in range(col_size):
                sum_map[i+j].append(mat[i][j])
                                        
        for _sum in sum_map.keys():
            if _sum % 2 == 0:
                sum_map[_sum].reverse()
        
        zig_zag_traverse = []

        for arr in sum_map.values():
            zig_zag_traverse.extend(arr)
            
        return zig_zag_traverse
                
# Numbers at the diagonals have one important property, i.e their indexes' sum
# is equal. So we will keep track numbers whose indexes' sum equal as values
# and the sum as keys. Then to create the zig-zag effect, we can see that we always
# start in the upward direction from the top left so for every indexes whose sum is
# even the direction is upward so we reverse those numbers. At last we concatenate
# the values of the map.
                
                
