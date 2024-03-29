# https://practice.geeksforgeeks.org/problems/heap-sort/1

class Solution:
    def heapify(self,arr, n, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
            
    def buildHeap(self,arr,n):
        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)
    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
