from itertools import accumulate


def solve():
    n, p = map(int, input().split())
    arr = list(map(int, input().split()))
    pre = [0]
    for pos in arr:
        pre.append(pos + pre[-1])

    def helper():
        L = 0
        R = 1
        start, song_n = None, float('inf')
        seen = set()
        total = 0
        while True:
            total += pre[R] - pre[L]
            while pre[R] - pre[L] >= p:
                if total >= p or start in seen:
                    return (start, song_n)
                seen.add(start)
                if R - L < song_n:
                    start = L + 1
                    song_n = R - L
                L += 1
            R = (R + 1) % (n+1)



    
    print(*helper())


solve()
