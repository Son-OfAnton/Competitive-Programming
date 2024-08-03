from collections import defaultdict


t = int(input())
for _ in range(t):
    n = int(input())
    results = []
    palindromes = [num for num in range(1, n + 1) if str(num) == str(num)[::-1]]
    
    dp = [0] * (n + 1)
    dp[0] = 1  

    for p in palindromes:
        for i in range(p, n + 1):
            dp[i] = (dp[i] + dp[i - p]) % (10**9 + 7)

    results.append(dp[n])
    print(*results, sep='\n')
