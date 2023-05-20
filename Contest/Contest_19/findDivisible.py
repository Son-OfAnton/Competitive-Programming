# https://codeforces.com/gym/443238/problem/B

t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    print(f"{l} {2*l}")
