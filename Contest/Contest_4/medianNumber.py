# https://codeforces.com/gym/422945/problem/A

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    nums.sort()
    size = len(nums)
    
    print(nums[size//2])
    
    
    
# Just used basic math fact. 

