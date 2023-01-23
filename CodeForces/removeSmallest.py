# https://codeforces.com/problemset/problem/1399/A

from collections import Counter

number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    arr_size = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    left = 0
    right = 1
    flag = False
    
    while right < arr_size:
        if arr[right] - arr[left] > 1:
            print("NO")
            flag = True
            break
        
        right += 1
        left += 1
        
    if not flag:
        print("YES")
        
