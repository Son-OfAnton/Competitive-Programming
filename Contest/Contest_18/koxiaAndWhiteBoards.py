# https://codeforces.com/gym/442099/problem/A

from heapq import heapify, heappop, heappush

t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    heapify(a)

    for num in b:
        heappop(a)
        heappush(a, num)

    print(sum(a))



    
