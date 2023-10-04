def digit_sum(num):
    total = 0
    num_str = str(num)
    for digit in num_str:
        total += int(digit)

    return total, num_str


m, s = map(int, input().split())



L = 10**(m-1)
R = 10**(m) - 1
print(R-L)
# mid = (R - L) // 2
# print(L, mid, R)


# while L < R:
#     mid = (R + L) // 2
#     print(L, mid, R)
#     total, num_str = digit_sum(mid)
    
#     if total == s:
#         print(mid, int(num_str[::-1]))
#         exit()
#     if total < s:
#         L = mid + 1
#     else:
#         R = mid - 1

# print(-1, -1, end='')
