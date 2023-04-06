# https://www.eolymp.com/en/contests/9060/problems/78603

n = int(input())

adj_mat = []

for _ in range(n):
    line = list(map(int, input().split()))
    adj_mat.append(line)

for connectivity in adj_mat:
    neibours = []

    for i in range(n):
        if connectivity[i]:
            neibours.append(i + 1)

    print(len(neibours), *neibours)
