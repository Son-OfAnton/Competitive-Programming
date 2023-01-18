# https://codeforces.com/gym/421441/problem/A

n = int(input())

for i in range(n):
    dim_1 = list(map(int, input().split()))
    dim_2 = list(map(int, input().split()))
    all_dim = dim_1 + dim_2
    
    max_side = max(all_dim)
    min_1 = min(dim_1)
    min_2 = min(dim_2)

    if max_side in dim_1 and max_side in dim_2 and min_1 + min_2 == max_side:
        print("Yes")
    else:
        print("No")
