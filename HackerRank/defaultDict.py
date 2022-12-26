# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

from collections import defaultdict

n_and_m = input().split()
n = int(n_and_m[0])
m = int(n_and_m[1])

dic_A = defaultdict(list)

for i in range(n):
    dic_A[input()].append(i+1)
    
B = []

for i in range(m):
    B.append(input())
    
for char in B:
    if char in dic_A:
        for index in dic_A[char]:
            print(str(index), end=" ")
        print()
    else:
        print(-1)
            
