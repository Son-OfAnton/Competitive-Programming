# https://codeforces.com/gym/444512/problem/B

from collections import Counter, defaultdict


def main():
    vertices, edges = map(int, input().split())
    degree = defaultdict(int)

    for _ in range(edges):
        u, v = map(int, input().split())
        degree[u] += 1
        degree[v] += 1

    degree_count = defaultdict(int)
    for node in range(1, vertices + 1):
        degree_count[degree[node]] += 1

    arr = sorted(degree_count.values())
    if len(arr) == 3:
        x, y = arr[1], arr[2] // arr[1]
    else:
        x, y = arr[0] - 1, arr[1] // (arr[0] - 1)

    return x, y


t = int(input())
for _ in range(t):
    print(*main())
