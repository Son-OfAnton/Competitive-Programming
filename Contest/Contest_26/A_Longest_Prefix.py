from collections import Counter

def solve(a, b):
    b_population = Counter(b)
    pre_len = 0

    for char in a:
        if b_population[char] == 0:
            break
        b_population[char] -= 1
        pre_len += 1
        
    return pre_len
        
t = int(input())

for _ in range(t):
    a, b = input().split()
    pre_len = solve(a, b)
    print(pre_len)