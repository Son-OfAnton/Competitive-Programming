# https://codeforces.com/gym/436344/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr_set = set(arr)
    res = None

    for i in range(n):
        pre = 0

        for j in range(n):
            if j == i:
                continue
            pre ^= arr[j]

        if pre in arr_set:
            res = pre
            break

    print(res)
