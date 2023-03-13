# https://codeforces.com/gym/431987/problem/A

number = input()

if int(number[0]) == 9:
    inverted = int(number[0])
else:
    inverted = min(9 - int(number[0]), int(number[0]))

for d in number[1:]:
    inverted *= 10
    inverted += min(9 - int(d), int(d))

print(inverted)
