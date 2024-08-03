string = input()
n = int(input())
precomputed = [0]

for i in range(1, len(string)):
    if string[i] == string[i-1]:
        precomputed.append(precomputed[-1] + 1)
    else:
        precomputed.append(precomputed[-1])

for _ in range(n):
    l, r = map(int, input().split())
    print(precomputed[r-1] - precomputed[l-1])
    