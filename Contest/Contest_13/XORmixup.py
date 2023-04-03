# https://codeforces.com/gym/436344/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        sub_XOR = 0
        
        for j in range(n):

            if i != j:
                sub_XOR ^= arr[j]

        if sub_XOR == arr[i]:
            print(arr[i])
            break
