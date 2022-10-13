# 1109. Corporate Flight Bookings

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * n
        for booking in bookings:
            first, last, seat = booking[0], booking[1], booking[2]
            answer[first - 1] += seat
            
            if last < n:
                answer[last] -= seat
            
        for i in range(1, n):
            answer[i] += answer[i - 1]
        
        return answer
      
      
# A naive java solution
# Time complexity: O(n^2)
# Space complexity: O(n)

#  class Solution {
#     public int[] corpFlightBookings(int[][] bookings, int n) {
#         int[] arr = new int[n];
#         for (int i = 0; i < bookings.length; i++) {
#             int[] row = bookings[i];
#             for (int j = row[0]; j <= row[1]; j++) {
#                 arr[j - 1] = arr[j - 1] + row[2];
#             }
#         }
#         return arr;
#     }
# }
