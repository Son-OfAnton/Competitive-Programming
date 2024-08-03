t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    yasser = sum(arr)

    max_ending_here = max_so_far = 0
    for num in arr[1:-1]:  
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
        

    print(max_so_far, max_ending_here, yasser)
    if max_so_far < yasser:
        print("YES")
    else:
        print("NO")