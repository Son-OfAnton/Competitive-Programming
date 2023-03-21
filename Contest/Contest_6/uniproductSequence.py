# https://codeforces.com/gym/425418/problem/B

n = int(input())
a = list(map(int, input().split()))

neg_count = 0
zero_count = 0
coin = 0

for i in range(n):
    if a[i] < 0:
        neg_count += 1
        coin += (- 1 - a[i])
    elif a[i] > 0:
        coin += a[i] - 1
    else:
        zero_count += 1
        coin += 1

# if there are odd number of -1 we have to change
#  one of them into +1 by spending 2 coins
# if there are zeros converting one of them into -1
# will do the trick so no need to add 2
if neg_count % 2 == 1 and zero_count == 0:
    coin += 2

print(coin)
