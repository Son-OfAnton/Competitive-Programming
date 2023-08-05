t = int(input())
table = {
    1: [],
    2: [1],
    3: [7],
    4: [4],
    5: [5, 3, 2],
    6: [9, 6],
    7: [8]
}

dp = dict()
def solve(n):

for _ in range(t):
    n = int(input())
    solve(n)
    partition = []

    for i in range(1, n//2 + 1):
        partition.append([i, n-i])
