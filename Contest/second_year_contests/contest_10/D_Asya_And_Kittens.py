from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.p = [i for i in range(n + 1)]
        self.r = defaultdict(lambda: 1)

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)

        if self.r[x] > self.r[y]:
            self.p[y] = x
            self.r[x] += self.r[y]
        else:
            self.p[x] = y
            self.r[y] += self.r[x]

    def find(self, x):
        if self.p[x] == x:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

def dfs(s, p, adj):
    print(s, end=' ')
    for e in adj[s]:
        if e != p:
            dfs(e, s, adj)


def main():
    n = int(input())
    adj = defaultdict(list)
    dsu = DisjointSetUnion(n)

    for i in range(1, n):
        j, k = map(int, input().split())

        u = dsu.find(j)
        v = dsu.find(k)

        adj[u].append(v)
        adj[v].append(u)

        dsu.union(u, v)

    dfs(1, -1, adj)

if __name__ == "__main__":
    main()
