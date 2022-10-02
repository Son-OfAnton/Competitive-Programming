# https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    # Write your code here
    result = [0] * 100
    
    for i in range(len(arr)):
        result[arr[i]] += 1
    
    return result
