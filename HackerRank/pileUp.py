# https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true

T = int(input())
for i in range(T):
    n = int(input())
    sideLength = list(map(int, input().split(' ')))
    left, right = 0, len(sideLength) - 1
    big_max = float('inf')
    pile_possible = True
                
    while left <= right:
        if sideLength[left] >= sideLength[right]:
            maxx = sideLength[left]
            left += 1
        else:
            maxx = sideLength[right]
            right -= 1
            
        if maxx > big_max:
            pile_possible = False
            break
        big_max = maxx
        
    if pile_possible:
        print("Yes")
    else:
        print("No")
        
        
    
    
