# https://codeforces.com/gym/444512/problem/C

from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.rep = [i for i in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]

    def find(self, x):
        if x == self.rep[x]:
            return x
        else:
            self.rep[x] = self.find(self.rep[x])
            return self.rep[x]

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)

        if self.size[x_rep] < self.size[y_rep]:
            self.rep[x_rep] = y_rep
            self.size[y_rep] += self.size[x_rep]
        else:
            self.rep[y_rep] = x_rep
            self.size[x_rep] += self.size[y_rep]

    def connected(self, x, y):
        return self.find(x) == self.find(y)


def main():
    n, m = map(int, input().split())
    uf = UnionFind(n)

    for _ in range(m):
        group = list(map(int, input().split()))
        group_size = len(group)

        for i in range(2, group_size):
            uf.union(group[1], group[i])

    for i in range(1, n + 1):
        parent = uf.find(i)
        uf.size[parent]
        print(uf.size[parent], end=" ")


main()

