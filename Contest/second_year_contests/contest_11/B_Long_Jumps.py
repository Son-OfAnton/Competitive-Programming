t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * n

    for i in range(n-1, -1, -1):
        dp[i] = arr[i]
        j = i + arr[i]

        if j < n:
            dp[i] += dp[j]

    print(max(dp))
