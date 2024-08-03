from math import ceil

t = int(input())

def check(wagon_size, return_hour, demand, delivery_time):
    for i, time in enumerate(delivery_time):
        trips = ceil(demand[i] / wagon_size)
        return_hour -= trips * time

        if return_hour < 0:
            return False
        
    return True
        



for _ in range(t):
    village_count, return_hour = map(int, input().split())
    demand = list(map(int, input().split()))
    delivery_time = list(map(int, input().split()))

    L, R = 1, max(demand)

    while L < R:
        mid = L + (R - L) // 2

        if check(mid, return_hour, demand, delivery_time):
            R = mid
        else:
            L = mid + 1

    print(L if check(L, return_hour, demand, delivery_time) else -1)