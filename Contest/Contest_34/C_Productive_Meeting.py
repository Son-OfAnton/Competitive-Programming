t = int(input())

for _ in range(t):
    n = int(input())
    if n == 1:
        print(0)
    sociability = input().split()
    arr = []
    for i, soc in enumerate(sociability):
        arr.append([int(soc), i])
    
    arr.sort()

    talks = []
    L, R = n - 2, n - 1

    while L >= 0:
        # print(talks, arr)
        if arr[L][0] == 0 or arr[R][0] == 0:
            if arr[L][0] == 0:
                L -= 1
            if arr[R][0] == 0:
                # L -= 1
                # R -= 1
                R = L
                L -= 1
        else:
            arr[L][0] -= 1
            arr[R][0] -= 1
            talks.append((arr[L][1]+1, arr[R][1]+1))

    # print(talks)
    print(len(talks))
    for person_1, person_2 in talks:
        print(person_1, person_2)