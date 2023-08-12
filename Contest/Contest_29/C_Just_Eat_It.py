t = int(input())

def all_pos_subarray_sum(arr):
    subarray_sum = 0
    
    for num in arr:
        subarray_sum += num
        if subarray_sum <= 0:
            return False
        
    return True

for _ in range(t):
    n = int(input())
    cakes = list(map(int, input().split()))
    adel = all_pos_subarray_sum(cakes) and all_pos_subarray_sum(cakes[::-1])

    print("YES" if adel else "NO")
