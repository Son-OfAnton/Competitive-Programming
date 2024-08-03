t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    flip = 0
    for i in range(n):
        if a[i] != b[i]:
            flip += 1

    # print(flip)

    a.sort()
    b.sort()

    flip_2 = 1
    for i in range(n):
        if a[i] != b[i]:
            flip_2 += 1

    print(min(flip, flip_2))
