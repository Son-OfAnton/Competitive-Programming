# https://codeforces.com/gym/430380/problem/A

people_no = int(input())
names = list(input().split())
queries = int(input())

for _ in range(queries):
    new_comer = input()
    left, right = 0, people_no - 1

    while left <= right:
        mid = left + (right - left) // 2
        
        if names[mid] < new_comer:
            left = mid + 1
        elif names[mid] > new_comer:
            right = mid - 1
    
    print(left)
