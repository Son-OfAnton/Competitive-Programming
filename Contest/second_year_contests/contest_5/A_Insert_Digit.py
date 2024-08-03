t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    num = input()
    
    for i in range(n):
        if int(num[i]) < d:
            num = num[:i] + str(d) + num[i:]
            break
    else:
        num = num + str(d)

    print(num)