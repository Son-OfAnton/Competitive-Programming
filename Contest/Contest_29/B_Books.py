

n, t = map(int, input().split())
book = list(map(int, input().split()))

R = 0
total = 0
max_book = 0

for L in range(n):
    while R < n and total + book[R] <= t:
        total += book[R]
        R += 1
    
    max_book = max(max_book, R - L)
    total -= book[L]



print(max_book)
