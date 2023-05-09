# https://codeforces.com/gym/439769/problem/A


n, dest = map(int, input().split())
arr = list(map(int, input().split()))

path_cell = 0

while path_cell < dest - 1:
    path_cell += arr[path_cell]

if path_cell == dest - 1:
    print("YES")
else:
    print("NO")
