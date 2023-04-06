# https://www.eolymp.com/en/contests/9060/problems/78602

n = int(input())
adj_list = [[] for _ in range(n)]
k = int(input())

for oper in range(k):
    line = list(map(int, input().split()))

    if line[0] == 1:
        adj_list[line[1] - 1].append(line[2])
        adj_list[line[2] - 1].append(line[1])
    else:
        if adj_list[line[1] - 1]:
            print(*adj_list[line[1] - 1])
