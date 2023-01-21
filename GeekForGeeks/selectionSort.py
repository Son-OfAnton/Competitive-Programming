# https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            min = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min]:
                    min = j
            arr[min], arr[i] = arr[i], arr[min]
