# https://codeforces.com/gym/426940/problem/A

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
size = 2*n
left = n - 1
right = n
found = False

while left >= 0 and right < size:
    if sum(nums[:n]) != sum(nums[n:]):
        found = True
        print(*nums)
        break
    else:
        nums[left], nums[right] = nums[right], nums[left]
        # print(nums)
        left -= 1
        right += 1
        
if not found:
    print(-1)
        
        
        
    
