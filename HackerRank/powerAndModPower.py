# https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import pow

base = int(input())
exponent = int(input())
mod = int(input())

powered = int(pow(base, exponent))
print(powered)
print(powered % mod)
