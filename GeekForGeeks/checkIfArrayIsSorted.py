# https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        
        if n == 1:
            return True
        
        for pointer in range(1, n):
            if arr[pointer] < arr[pointer - 1]:
                return False
                
        return True
