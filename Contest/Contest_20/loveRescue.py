# https://codeforces.com/gym/444512/problem/D

from string import ascii_lowercase


class UnionFind:
    def __init__(self):
        self.rep = {i: i for i in ascii_lowercase}

    def find(self, x):
        if x == self.rep[x]:
            return x

        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)

        self.rep[x_rep] = y_rep

    def connected(self, x, y):
        return self.find(x) == self.find(y)


def main():
    n = int(input())
    valya = input()
    tolya = input()

    uf = UnionFind()
    pairs = []
    for i in range(n):
        v, t = valya[i], tolya[i]

        if not uf.connected(v, t):
            uf.union(v, t)
            pairs.append([v, t])

    return pairs


pairs = main()
print(len(pairs))
for x, y in pairs:
    print(x, y)
