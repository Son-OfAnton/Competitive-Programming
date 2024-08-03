t = int(input())

for _ in range(t):
    n = int(input())
    rev = [i for i in range(n, 0, -1)]
    if n % 2 == 1:
        rev[n//2], rev[0] = rev[0], rev[n//2]

    print(*rev)