# https://codeforces.com/gym/425425/problem/A

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    board = list(map(int, input().split()))
    aman = [0] * n
    left = 0
    right = n - 1
    
    for i in range(n):
        if i % 2 == 0:
            aman[i] = board[left]
            left += 1
        else:
            aman[i] = board[right]
            right -= 1
            
    print(*aman)
