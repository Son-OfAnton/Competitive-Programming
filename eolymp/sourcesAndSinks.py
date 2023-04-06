# https://www.eolymp.com/en/contests/9060/problems/78605

n = int(input())
adj_list = []
source, sink = [], []

for i in range(n):
    adj_v = list(map(int, input().split()))
    
    if not any(adj_v):
        sink.append(i + 1)

    adj_list.append(adj_v)


for j in range(n):
    all_col_zero = True

    for i in range(n):
        if adj_list[i][j] != 0:
            all_col_zero = False

    if all_col_zero:
        source.append(j + 1)

print(len(source), end=" ", *source)
print()
print(len(sink), end=" ", *sink)
