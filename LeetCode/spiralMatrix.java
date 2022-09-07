// 54. Spiral Matrix

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        
        List<Integer> spiral = new ArrayList<>();
        
        if(matrix.length == 0 || matrix[0].length == 0) 
            return spiral;
        
        int rowBegin = 0, colBegin = 0; 
        int rowEnd = matrix.length - 1;
        int colEnd = matrix[0].length - 1;
        
        
        while(rowBegin <= rowEnd && colBegin <= colEnd){
            
            for(int i = colBegin; i <= colEnd; i++) {
                spiral.add(matrix[rowBegin][i]);
            }
            rowBegin++;
            
            for(int i = rowBegin; i <= rowEnd; i++) {
                spiral.add(matrix[i][colEnd]);
            }
            colEnd--;
            
            if(rowBegin <= rowEnd) {
                for(int i = colEnd; i >= colBegin; i--) {
                    spiral.add(matrix[rowEnd][i]);
                }
            }
            rowEnd--;
            

            if(colBegin <= colEnd) {
                for(int i = rowEnd; i >= rowBegin; i--) {
                    spiral.add(matrix[i][colBegin]);
                }
            }
            colBegin++;
        }
        return spiral;
    }
}


      
