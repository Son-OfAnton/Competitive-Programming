t = int(input())

for _ in range(t):
    encrypted_len, sensetive_len = map(int, input().split())
    encrypted = input()
    sensetive = input()
    flag = False

    for i in range(encrypted_len - sensetive_len + 1):
        flips = set()
        slice = encrypted[i:i+sensetive_len]
        print(slice)

        for j in range(sensetive_len):
            diff = abs(ord(slice[j]) - ord(sensetive[j]))
            flip = min(diff, 26 - diff)
            print(i, flip)  
            flips.add(flip)

        # print(flips)
        if len(flips) <= 2:
            print(flips)
            print("YES")
            print(i)
            break
    else:
        print("NO")