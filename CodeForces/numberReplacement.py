# https://codeforces.com/problemset/problem/1744/A

num_of_test_cases = int(input())

for i in range(num_of_test_cases):
    arr_size = int(input())
    arr = list(map(int, input().split()))
    word = input()
    num_char_map = dict()
    response = True
    
    for index in range(arr_size):
        if arr[index] not in num_char_map:
            num_char_map[arr[index]] = word[index]
        else:
            if num_char_map[arr[index]] != word[index]:
                response = False 
                break
  
    if response:
        print("YES")
    else:
        print("NO")
