import java.util.*;

class Solution {
    public static void sortbyColumn(int arr[][], int col)
    {
        Arrays.sort(arr, new Comparator<int[]>() {
            
          @Override              
          // Compare values according to columns
          public int compare(final int[] entry1, 
                             final int[] entry2) {
  
            
            if (entry1[col] > entry2[col])
                return 1;
            else
                return -1;
          }
        });
    }
    public int[][] kClosest(int[][] points, int k) {
        int[][] pd = new int[points.length][3];
        int[][] sp = new int[k][2];

        for (int i = 0; i < points.length; i++) {
            for (int j = 0; j < 2; j++) {
                pd[i][j] = points[i][j];
                pd[i][2] = (int) (Math.pow(points[i][0], 2) + Math.pow(points[i][1], 2));
            }
        }
        
        sortbyColumn(pd, 2);

        for (int i = 0; i < k; i++) {
            for (int j = 0; j < 2; j++) {
                sp[i][j] = pd[i][j];
            }
        }

        return sp;
    }
}
