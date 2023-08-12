t = int(input())

def all_pos_subarray_sum(arr):
    max_sum = arr[0]
    summ = 0
    
    for num in arr:
        summ += num

        if summ > max_sum:
            max_sum = summ
       
        if summ <= 0:
            return False
        
    return True

for _ in range(t):
    n = int(input())
    cakes = list(map(int, input().split()))
    adel = all_pos_subarray_sum(cakes) and all_pos_subarray_sum(cakes[::-1])

    print("YES" if adel else "NO")
