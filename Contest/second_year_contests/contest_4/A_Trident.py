t = int(input())

for _ in range(t):
    n = int(input())
    perm = list(map(int, input().split()))

    for i in range(1, n-1):
        if perm[i-1] < perm[i] > perm[i+1]:
            print("YES")
            print(i, i+1, i+2)
            break
    else:    
        print("NO")
