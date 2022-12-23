# https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

A = set(map(int, input().split()))
n = int(input())

def strictSuperSet(A, n):
    for i in range(n):
        each_set = set(map(int, input().split()))
        
        if each_set.difference(A):
            print("False")
            return
    print("True")
        
strictSuperSet(A, n)
        
