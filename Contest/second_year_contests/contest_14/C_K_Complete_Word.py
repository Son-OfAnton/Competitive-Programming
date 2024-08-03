t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    res = 0

    for i in range(n-k):
        if s[i] == s[i+k]:
            continue
        
        # print(i, i+k)
        res += 1

    print(res)

