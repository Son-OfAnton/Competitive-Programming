// https://www.hackerrank.com/challenges/insertionsort1/problem

def printArr(arr):
    for i in arr:
        print(i, end=' ')
    print()
            
def insertionSort1(n, arr):
    # Write your code here     
    temp = arr[n-1]
    
    for i in range(n-2, -1, -1):
        if arr[i] > temp:
            arr[i+1] = arr[i]
            printArr(arr)
        else:
            arr[i+1] = temp
            printArr(arr)
            break
        if i == 0 and arr[i] >= temp:
            arr[0] = temp
            printArr(arr)
