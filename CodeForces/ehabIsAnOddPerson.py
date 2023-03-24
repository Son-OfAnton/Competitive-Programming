# https://codeforces.com/problemset/problem/1174/B

n = int(input())
arr = list(map(int, input().split()))

seen_even, seen_odd = False, False

for num in arr:
    if num % 2:
        seen_odd = True
    else:
        seen_even = True

if seen_even and seen_odd:
    arr.sort()

# if all have same parity do nothing
print(*arr)
