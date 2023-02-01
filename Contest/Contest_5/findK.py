# https://codeforces.com/gym/424075/problem/D

number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    length, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums.sort()
    
    left = 0
    right = 1
    found = False
    
    while right < length:
        diff = nums[right] - nums[left]
        
        if diff == k:
            print("YES")
            found = True
            break
        elif diff > k:
            left += 1
        else:
            right += 1
            
    if not found:       
        print("NO")
            
