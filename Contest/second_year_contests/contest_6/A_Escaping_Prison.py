t = int(input())

for _ in range(t):
    n, h = map(int, input().split())

    rope_len = 0
    for _ in range(n):
        w, l = map(int, input().split())
        rope_len += max(w, l)

    print("YES" if rope_len >= h else "NO")


