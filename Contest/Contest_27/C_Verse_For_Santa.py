t = int(input())

def solve():
    n, s = map(int, input().split())
    parts = list(map(int, input().split()))

    def helper(i, total, skipped):
        if i >= n:
            return 0
        if total > s:
            return skipped
        helper(i+1, total + parts[i], 0)
        if skipped == 0:
            helper(i+1, total, i)

    return helper(0, 0, 0)






for _ in range(t):
    print(solve())