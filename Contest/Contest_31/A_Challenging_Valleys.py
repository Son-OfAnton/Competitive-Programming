t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = []

    for i in range(n):
        if i == 0 or arr[i] != arr2[-1]:
            arr2.append(arr[i])
            
    count = 0
    new_n = len(arr2)
    for i in range(new_n ) :
        if (i == 0 or arr2[i-1] > arr2[i]) and (i == new_n - 1 or arr2[i] < arr2[i+1]):
            count += 1

    print("YES" if count == 1 else "NO")