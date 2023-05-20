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
    groups = defaultdict(set)

    for _ in range(m):
        inp = list(map(int, input().split()))
        if inp[0] != 0:
            root = inp[1]
            for i in range(2, len(inp)):
                uf.union(root, inp[i])

    for i in range(1, n + 1):
        groups[uf.find(i)].add(i)

    for i in range(1, n + 1):
        print(len(groups[uf.find(i)]), end=" ")


main()
