# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

size_1, size_2 = list(map(int, input().split()))
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

ptr_1 = 0
ptr_2 = 0
merged_arr = []

while ptr_1 < size_1 and ptr_2 < size_2:
    if arr_1[ptr_1] < arr_2[ptr_2]:
        merged_arr.append(arr_1[ptr_1])
        ptr_1 += 1
        
    else:
        merged_arr.append(arr_2[ptr_2])
        ptr_2 += 1
        
if ptr_1 == size_1:
    merged_arr.extend(arr_2[ptr_2:])
else:
    merged_arr.extend(arr_1[ptr_1:])
        
print(*merged_arr)
