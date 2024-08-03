class UnionFind:
    def __init__(self, n):
        self.rep = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x != self.rep[x]:
            self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)

        if self.size[x_rep] < self.size[y_rep]:
            x_rep, y_rep = y_rep, x_rep
        self.rep[y_rep] = x_rep
        self.size[x_rep] += self.size[y_rep]

    def connected(self, x, y):
        return self.find(x) == self.find(y)
