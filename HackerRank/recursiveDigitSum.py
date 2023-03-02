# https://www.hackerrank.com/challenges/recursive-digit-sum/problem

def superDigit(n, k):
    # Write your code here
    if len(n) == 1:
        return int(n)
    summ = 0
    for c in n:
        summ += int(c)
    
    summ *= k
    return superDigit(str(summ), 1)
