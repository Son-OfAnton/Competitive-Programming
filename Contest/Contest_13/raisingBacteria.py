# https://codeforces.com/gym/436344/problem/B

target = int(input())

one_count = 0

while target:
    one_count += target & 1
    target >>= 1

print(one_count)
