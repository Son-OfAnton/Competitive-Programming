# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

size_1, size_2 = list(map(int, input().split()))
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

ptr_1, ptr_2 = 0, 0
merged = []

while ptr_1 < size_1 and ptr_2 < size_2:
    if arr_1[ptr_1] <= arr_2[ptr_2]:
        merged.append(arr_1[ptr_1])
        ptr_1 += 1
    else:
        merged.append(arr_2[ptr_2])
        ptr_2 += 1

if ptr_1 == size_1:
    merged.extend(arr_2[ptr_2:])
else:
    merged.extend(arr_1[ptr_1:])

print(*merged)

