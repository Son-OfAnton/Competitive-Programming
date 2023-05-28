# https://codeforces.com/gym/444512/problem/E

from heapq import heapify, heappop


class UnionFind:
    def __init__(self, n):
        self.rep = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.extra_conn_we_can_make = 0

    def find(self, x):
        if self.rep[x] != x:
            self.rep[x] = self.find(self.rep[x])

        return self.rep[x]

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)

        if x_rep != y_rep:
            if self.size[x_rep] < self.size[y_rep]:
                self.rep[x_rep] = y_rep
                self.size[y_rep] += self.size[x_rep]
            else:
                self.rep[y_rep] = x_rep
                self.size[x_rep] += self.size[y_rep]
        else:
            self.extra_conn_we_can_make += 1

        heap = [-s for person,
                s in enumerate(self.size) if self.rep[person] == person]
        heapify(heap)

        max_conn = 0
        for _ in range(self.extra_conn_we_can_make + 1):
            max_conn += abs(heappop(heap))

        print(max_conn - 1)


def main():
    n, d = map(int, input().split())
    uf = UnionFind(n)

    for _ in range(d):
        x, y = map(int, input().split())
        uf.union(x, y)


main()
