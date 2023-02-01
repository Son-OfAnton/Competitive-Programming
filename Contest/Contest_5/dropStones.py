# https://codeforces.com/gym/424075/problem/E

cases = int(input())

for _ in range(cases):
    row_size, col_size = map(int , input().split())
    
    grid = []
    
    for _ in range(row_size):
        temp = list(input())
        grid.append(temp)
    
    for cx in range(col_size):
        floor = row_size
        for rx in range(row_size - 1, -1, -1):
            
            if grid[rx][cx] == '*':
                floor -= 1
                
                if rx != floor:
                    grid[floor][cx] = '*'
                    grid[rx][cx] = '.'
                    
            elif grid[rx][cx] == 'o':
                floor = rx
                   
    
    for rx in range(row_size):
        for cx in range(col_size):
            print(grid[rx][cx],end='')
        print()
    print()
