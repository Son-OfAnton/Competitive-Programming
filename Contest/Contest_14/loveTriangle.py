# https://codeforces.com/gym/437178/problem/A

n = int(input())
love_list = list(map(int, input().split()))


for i in range(n):
    if love_list[love_list[love_list[i] - 1] - 1] == i + 1:
        print("YES")
        break
else:
    print("NO")
