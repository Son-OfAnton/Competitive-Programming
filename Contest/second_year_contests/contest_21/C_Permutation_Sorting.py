count = 0

def quick_sort(arr, low, high):
    global count
    if low < high:
        count += 1
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

t = int(input())

for _ in range(t):
    n = int(input())
    perm = list(map(int, input().split()))
    quick_sort(perm, 0, n-1)
    print(count)
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     perm = list(map(int, input().split()))

#     # print the count of operation of quick sort to sort the perm array
