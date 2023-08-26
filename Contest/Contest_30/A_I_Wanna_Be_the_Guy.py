n = int(input())

arr_1 = list(map(int, input().split()))[1:]
arr_2 = list(map(int, input().split()))[1:]
arr_1 += arr_2
all_levels = set(arr_1)

for level in range(1, n+1):
    if level not in all_levels:
        print('Oh, my keyboard!')
        exit()

print('I become the guy.')