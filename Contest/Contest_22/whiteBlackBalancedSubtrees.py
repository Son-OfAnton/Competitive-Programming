# https://codeforces.com/gym/450068/problem/C

from collections import defaultdict
import sys, threading

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        nodes = list(map(int, input().split()))
        colors = input()
        graph = defaultdict(list)

        for child, parent in enumerate(nodes):
            graph[parent].append(child + 2)

        balanced_subtrees = 0

        def subtree_counter(parent):
            nonlocal balanced_subtrees

            white, black = 0, 0

            for child in graph[parent]:
                bottom_white, bottom_black = subtree_counter(child)
                white += bottom_white
                black += bottom_black

            if colors[parent - 1] == 'W':   white += 1
            else: black += 1

            if white == black:  balanced_subtrees += 1

            return [white, black]
        
        subtree_counter(1)

        print(balanced_subtrees)

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
