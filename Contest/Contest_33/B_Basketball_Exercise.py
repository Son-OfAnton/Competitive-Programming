n = int(input())
row_1 = list(map(int, input().split()))
row_2 = list(map(int, input().split()))

for i in range(1, n):
    row_1[i] = max(row_1[i-1], row_2[i-1] + row_1[i])
    row_2[i] = max(row_2[i-1], row_1[i-1] + row_2[i])

print(row_1, row_2, end='\n')

res = max(row_1[-1], row_2[-1])
print(res)
