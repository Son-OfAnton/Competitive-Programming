# https://codeforces.com/gym/436344/problem/C

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    k_th_special = 0
    for i in range(k.bit_length()):
        if k & (1 << i):
            k_th_special += n ** i

    print(k_th_special % (10**9 + 7))
