def solve():
    n = int(input())
    if n == 2:
        print('NO')
        return
    print('YES' if n % 2 == 0 else 'NO')


solve()