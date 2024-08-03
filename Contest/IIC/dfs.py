import sys
import threading


def main():

    def dfs(n, dp):
        pass

    t = int(input())
    for _ in range(t):
        n = int(input())


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
