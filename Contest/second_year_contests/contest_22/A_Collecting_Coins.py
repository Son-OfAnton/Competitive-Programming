t = int(input())

for _ in range(t):
    a, b, c, n = map(int, input().split())
    total = a + b + c + n
    if total % 3 == 0 and a <= total // 3 and b <= total // 3 and c <= total // 3:
        print("YES")
    else:
        print("NO")