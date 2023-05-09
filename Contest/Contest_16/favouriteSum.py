# https://codeforces.com/gym/439769/problem/B

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    favs = set(map(int, input().split()))
    _sum = x * (x + 1) // 2

    neg_sum = 0

    for num in favs:
        if num <= x:
            neg_sum -= num

    print(_sum + 2 * neg_sum)
