# https://codeforces.com/gym/422945/problem/C

arr_size = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(arr)

left = -1
right = -1

for index in range(arr_size):
    if arr[index] != sorted_arr[index]:
        left = index
        break
    
for index in range(arr_size - 1, -1, -1):
    if arr[index] != sorted_arr[index]:
        right = index
        break
    
if left == -1:
    print("yes\n1 1")
    exit()
    
arr[left:right+1] = reversed(arr[left:right+1])

for index in range(arr_size):
    if arr[index] != sorted_arr[index]:
        print("no")
        exit()
        
print(f"yes\n{left+1} {right+1}")

    
