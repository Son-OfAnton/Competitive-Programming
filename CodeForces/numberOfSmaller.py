# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

size_1, size_2 = list(map(int, input().split()))
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

ptr_1 = 0
res = []

for num in arr_2:
    while ptr_1 < size_1 and arr_1[ptr_1] < num:
        ptr_1 += 1

    res.append(ptr_1)

print(*res)
