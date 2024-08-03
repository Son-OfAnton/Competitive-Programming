t = int(input())

def solve():
    palindrome = input()

    if len(set(palindrome)) == 1:
        return -1
    else:
        return len(palindrome) - 1
    
for _ in range(t):
    print(solve())