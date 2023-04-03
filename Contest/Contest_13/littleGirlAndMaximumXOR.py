# https://codeforces.com/gym/436344/problem/F

l, r = map(int, input().split())

_max = l ^ r
pos = 0

while _max:
    _max >>= 1
    pos += 1

print((1 << pos) - 1)
