# https://codeforces.com/problemset/problem/1688/A

t = int(input())

for _ in range(t):
    x = int(input())

    if x == 1:
        print(3)
    elif x & (x - 1) == 0:  # checking power of two
        print(x + 1)
    else:
        lowest_set_bit = x & -x
        print(lowest_set_bit)
