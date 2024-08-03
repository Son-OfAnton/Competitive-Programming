from bisect import bisect_left

n = int(input())
pile = list(map(int, input().split()))
m = int(input())
worms = list(map(int, input().split()))

for i in range(1, n):
    pile[i] += pile[i-1]

for worm in worms:
    print(bisect_left(pile, worm)+1)

