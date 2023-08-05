import sys, threading

def main():
    def solve(s, i, dp):
        if i == len(s):
            return True

        if i in dp:
            return dp[i]
        
        possible = False
        if s[i:i+2] in {"aa", "bb"}:
            possible |= solve(s, i+2, dp)
        if s[i:i+3] in {"aaa", "bbb"}:
            possible |= solve(s, i+3, dp)

        dp[i] = possible
        return dp[i]

    t = int(input())
    for _ in range(t):
        s = input()
        canBeBuild = solve(s, 0, dict())
        print("YES" if canBeBuild else "NO")

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()