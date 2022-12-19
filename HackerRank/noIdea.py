# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

dimensions = str(input())
n = int(dimensions.split(' ')[0])
m = int(dimensions.split(' ')[1])
array = list(map(int, input().split(' ')))
A = set(map(int, input().split(' ')))
B = set(map(int, input().split(' ')))
happiness = 0

for i in array:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1

print(happiness)
