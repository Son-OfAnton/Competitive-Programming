from math import ceil

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    mult = k * ceil(n / k)
    # print(f"mult: {mult}")
    print(ceil(mult / n))