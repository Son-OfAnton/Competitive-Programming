n = int(input())
records = []

for i in range(n):
    records.append(input().split('#'))

for record in records:
    print(record[0] + " " + record[1] + " " + record[2])
