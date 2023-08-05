from collections import deque

def main():
    def solve(curr, path):
        while curr != parent[curr - 1] and parent[curr - 1] != -1:
            path.appendleft(curr)
            prev_curr = curr
            curr = parent[curr - 1]
            parent[prev_curr - 1] = -1

        if curr == parent[curr - 1]:
            parent[curr - 1] = -1
            path.appendleft(curr)
        
        return path
        


    t = int(input())
    for _ in range(t):
        n = int(input())
        parent = list(map(int, input().split()))
        if n == 1:
            print("1\n1\n1\n")
            continue

        parent_set = set(parent)
        leaves = []

        for i in range(1, n+1):
            if i not in parent_set:
                leaves.append(i)
        
        paths = []
        for leaf in leaves:
            paths.append(solve(leaf, deque()))
        
        print(len(paths))
        for path in paths:
            print(len(path))
            print(*path)
        print()

main()
