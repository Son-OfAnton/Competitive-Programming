t = int(input())

for _ in range(t):
    n = int(input())
    all = first = second = float('inf')
    
    for i in range(n):
        m, s = input().split()
        if s == '10':
            first = min(first, int(m))
        elif s == '01':
            second = min(second, int(m))
        elif s == '11':
            all = min(all, int(m))

    min_time = min(first + second, all)
    print(min_time if min_time != float('inf') else -1)

        
        