n = int(input())
s = input()
decrypted = []

i = 0
j = 1

while i < n:
    decrypted.append(s[i])
    i += j
    j += 1

print(''.join(decrypted))











"""

a b c d
0 1 2 3

a b b c c c d d d d
0 1 2 3 4 5 6 7 8 9

0 1 3 6 10 15 21 28 36 45
"""