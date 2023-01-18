# https://codeforces.com/gym/421441/problem/B

n = int(input())
nums = list(map(int, input().split()))

pos = []
neg = []
zero = []

for num in nums:
    if num > 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    else:
        zero.append(num)
        
if len(neg) % 2 == 0:
    zero.append(neg.pop())
if len(neg) > 2:
    pos.append(neg.pop())
    pos.append(neg.pop())
    
print(len(neg), end=" ")
for num in neg:
    print(num, end = " ")
print()

print(len(pos), end=" ")
for num in pos:
    print(num, end = " ")
print()

print(len(zero), end = " ")
for num in zero:
    print(num, end = " ")
print()

